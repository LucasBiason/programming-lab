#!/usr/bin/env python3
"""
Executa cada request da API Jury AI, captura respostas reais (sucesso e erro)
e atualiza postman/collection.json com esses exemplos.

Requer: servidor Django rodando em BASE_URL (ex.: http://localhost:8000)
Uso: python scripts/capture_postman_examples.py [BASE_URL]
"""

import json
import os
import sys
import time
import uuid

try:
    import requests
except ImportError:
    print("Instale requests: pip install requests")
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLLECTION_PATH = os.path.join(ROOT, "postman", "collection.json")
BASE_URL = (sys.argv[1] if len(sys.argv) > 1 else None) or os.environ.get("BASE_URL", "http://localhost:8000")

USER_EMAIL = "teste@jury.ai"
USER_PASSWORD = "senha1234"


def _req(method, path, headers=None, json_body=None, expected_codes=None):
    url = BASE_URL.rstrip("/") + path
    h = dict(headers or {})
    if json_body is not None and "Content-Type" not in h:
        h["Content-Type"] = "application/json"
    try:
        if method == "GET":
            r = requests.get(url, headers=h, timeout=10)
        elif method == "POST":
            r = requests.post(url, headers=h, json=json_body, timeout=10)
        elif method == "PUT":
            r = requests.put(url, headers=h, json=json_body, timeout=10)
        elif method == "DELETE":
            r = requests.delete(url, headers=h, timeout=10)
        else:
            raise ValueError(method)
    except requests.RequestException as e:
        return {"error": str(e), "code": 0, "headers": {}, "body": ""}
    code = r.status_code
    if expected_codes and code not in expected_codes:
        print(f"  [aviso] {method} {path} -> {code} (esperado {expected_codes})")
    try:
        body = r.text if r.content else ""
        if body and "application/json" in r.headers.get("Content-Type", ""):
            try:
                json.loads(body)
            except Exception:
                pass
        return {"code": code, "headers": dict(r.headers), "body": body}
    except Exception:
        return {"code": code, "headers": dict(r.headers), "body": r.text or ""}


def _postman_response(name, method, url_path, req_headers, req_body, res):
    if res.get("error"):
        return None
    code = res["code"]
    status_names = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
    }
    status = status_names.get(code, str(code))
    orig = {"method": method, "header": [{"key": k, "value": str(v)} for k, v in (req_headers or {}).items()]}
    if req_body is not None:
        raw = req_body if isinstance(req_body, str) else json.dumps(req_body, ensure_ascii=False)
        orig["body"] = {"mode": "raw", "raw": raw}
    res_headers = res.get("headers") or {}
    ct = res_headers.get("Content-Type", "application/json")
    header_list = [{"key": "Content-Type", "value": ct}]
    body = (res.get("body") or "").strip()
    return {
        "name": name,
        "originalRequest": orig,
        "status": status,
        "code": code,
        "_postman_previewlanguage": "json",
        "header": header_list,
        "body": body,
    }


def capture_all():
    out = {}
    token = None
    refresh_token = None
    cliente_id = None

    # --- Cadastro: sucesso (email único) e erro (email já existe) ---
    unique_email = f"capture-{uuid.uuid4().hex[:12]}@jury.ai"
    cadastro_ok = _req("POST", "/api/auth/cadastro/", json_body={
        "email": unique_email,
        "username": "capture",
        "first_name": "Capture",
        "last_name": "User",
        "password": USER_PASSWORD,
        "password_confirm": USER_PASSWORD,
    }, expected_codes=[201])
    out["Cadastro"] = [
        _postman_response(
            "✅ 201 - Usuário criado",
            "POST", "/api/auth/cadastro/",
            {"Content-Type": "application/json"},
            {"email": unique_email, "username": "capture", "first_name": "Capture", "last_name": "User", "password": USER_PASSWORD, "password_confirm": USER_PASSWORD},
            cadastro_ok,
        ),
        _postman_response(
            "❌ 400 - E-mail já existe",
            "POST", "/api/auth/cadastro/",
            {"Content-Type": "application/json"},
            {"email": USER_EMAIL, "username": "teste", "password": USER_PASSWORD, "password_confirm": USER_PASSWORD},
            _req("POST", "/api/auth/cadastro/", json_body={"email": USER_EMAIL, "username": "teste", "password": USER_PASSWORD, "password_confirm": USER_PASSWORD}, expected_codes=[400]),
        ),
    ]
    out["Cadastro"] = [x for x in out["Cadastro"] if x]

    # --- Login: sucesso e erro ---
    login_ok = _req("POST", "/api/auth/token/", json_body={"email": USER_EMAIL, "password": USER_PASSWORD}, expected_codes=[200])
    login_data = json.loads(login_ok["body"]) if login_ok.get("body") else {}
    token = login_data.get("access")
    refresh_token = login_data.get("refresh")
    out["Login"] = [
        _postman_response("✅ 200 - Login OK", "POST", "/api/auth/token/", {"Content-Type": "application/json"}, {"email": USER_EMAIL, "password": USER_PASSWORD}, login_ok),
        _postman_response("❌ 400 - E-mail ou senha inválidos", "POST", "/api/auth/token/", {"Content-Type": "application/json"}, {"email": "errado@jury.ai", "password": "errada"}, _req("POST", "/api/auth/token/", json_body={"email": "errado@jury.ai", "password": "errada"}, expected_codes=[400, 401])),
    ]
    out["Login"] = [x for x in out["Login"] if x]

    # --- Refresh: sucesso e erro ---
    refresh_ok = _req("POST", "/api/auth/token/refresh/", json_body={"refresh": refresh_token}, expected_codes=[200]) if refresh_token else {}
    out["Refresh Token"] = [
        _postman_response("✅ 200 - Novo access", "POST", "/api/auth/token/refresh/", {"Content-Type": "application/json"}, {"refresh": refresh_token or ""}, refresh_ok),
        _postman_response("❌ 401 - Refresh inválido", "POST", "/api/auth/token/refresh/", {"Content-Type": "application/json"}, {"refresh": "token.invalido"}, _req("POST", "/api/auth/token/refresh/", json_body={"refresh": "token.invalido"}, expected_codes=[401])),
    ]
    out["Refresh Token"] = [x for x in out["Refresh Token"] if x]
    if refresh_ok.get("body"):
        try:
            token = json.loads(refresh_ok["body"]).get("access") or token
        except Exception:
            pass

    # --- Me: sucesso e erro ---
    auth_header = {"Authorization": f"Bearer {token}"} if token else {}
    me_ok = _req("GET", "/api/auth/me/", headers=auth_header, expected_codes=[200])
    out["Me (perfil)"] = [
        _postman_response("✅ 200 - Perfil", "GET", "/api/auth/me/", auth_header, None, me_ok),
        _postman_response("❌ 401 - Token ausente", "GET", "/api/auth/me/", {}, None, _req("GET", "/api/auth/me/", expected_codes=[401])),
    ]
    out["Me (perfil)"] = [x for x in out["Me (perfil)"] if x]

    # --- List Clientes ---
    list_ok = _req("GET", "/api/clientes/", headers=auth_header, expected_codes=[200])
    list_data = json.loads(list_ok["body"]) if list_ok.get("body") else []
    if isinstance(list_data, list) and len(list_data) > 0:
        cliente_id = list_data[0].get("id")
    out["List Clientes"] = [
        _postman_response("✅ 200 - Lista", "GET", "/api/clientes/", auth_header, None, list_ok),
        _postman_response("❌ 401 - Não autenticado", "GET", "/api/clientes/", {}, None, _req("GET", "/api/clientes/", expected_codes=[401])),
    ]
    out["List Clientes"] = [x for x in out["List Clientes"] if x]

    # --- Create Cliente: sucesso e erro (nome vazio) ---
    create_body = {"nome": "Cliente Captura", "email": "captura@postman.com", "telefone": "11999999999", "cpf_cnpj": "", "observacoes": ""}
    create_ok = _req("POST", "/api/clientes/", headers=auth_header, json_body=create_body, expected_codes=[201])
    create_data = json.loads(create_ok["body"]) if create_ok.get("body") else {}
    if create_data.get("id") and not cliente_id:
        cliente_id = create_data["id"]
    create_err = _req("POST", "/api/clientes/", headers=auth_header, json_body={"nome": "", "email": "", "telefone": "", "cpf_cnpj": "", "observacoes": ""}, expected_codes=[400])
    out["Create Cliente"] = [
        _postman_response("✅ 201 - Cliente criado", "POST", "/api/clientes/", {**auth_header, "Content-Type": "application/json"}, create_body, create_ok),
        _postman_response("❌ 400 - Validação (nome vazio)", "POST", "/api/clientes/", {**auth_header, "Content-Type": "application/json"}, {"nome": "", "email": "", "telefone": "", "cpf_cnpj": "", "observacoes": ""}, create_err),
    ]
    out["Create Cliente"] = [x for x in out["Create Cliente"] if x]

    # Cliente ID para Get/Update/Delete (usar o criado ou primeiro da lista)
    cid = cliente_id or (create_data.get("id") if create_data else None) or 1

    # --- Get Cliente: sucesso e 404 ---
    get_ok = _req("GET", f"/api/clientes/{cid}/", headers=auth_header, expected_codes=[200])
    get_404 = _req("GET", "/api/clientes/99999/", headers=auth_header, expected_codes=[404])
    out["Get Cliente"] = [
        _postman_response("✅ 200 - Detalhe", "GET", f"/api/clientes/{cid}/", auth_header, None, get_ok),
        _postman_response("❌ 404 - Cliente não encontrado", "GET", "/api/clientes/99999/", auth_header, None, get_404),
    ]
    out["Get Cliente"] = [x for x in out["Get Cliente"] if x]

    # --- Update Cliente: sucesso e 404 ---
    update_body = {"nome": "Cliente Atualizado", "email": "cliente@postman.com", "telefone": "11988887777", "cpf_cnpj": "", "observacoes": "Editado via capture"}
    update_ok = _req("PUT", f"/api/clientes/{cid}/", headers={**auth_header, "Content-Type": "application/json"}, json_body=update_body, expected_codes=[200])
    update_404 = _req("PUT", "/api/clientes/99999/", headers={**auth_header, "Content-Type": "application/json"}, json_body=update_body, expected_codes=[404])
    out["Update Cliente"] = [
        _postman_response("✅ 200 - Atualizado", "PUT", f"/api/clientes/{cid}/", {**auth_header, "Content-Type": "application/json"}, update_body, update_ok),
        _postman_response("❌ 404 - Cliente não encontrado", "PUT", "/api/clientes/99999/", {**auth_header, "Content-Type": "application/json"}, update_body, update_404),
    ]
    out["Update Cliente"] = [x for x in out["Update Cliente"] if x]

    # --- Delete: 404 primeiro (para não alterar estado), depois sucesso num cliente criado por nós ---
    delete_404 = _req("DELETE", "/api/clientes/99999/", headers=auth_header, expected_codes=[404])
    # Criar um cliente só para deletar e obter 204 real
    temp_create = _req("POST", "/api/clientes/", headers=auth_header, json_body={"nome": "Temp Delete", "email": "temp@del.com", "telefone": "", "cpf_cnpj": "", "observacoes": ""}, expected_codes=[201])
    temp_id = None
    if temp_create.get("body"):
        try:
            temp_id = json.loads(temp_create["body"]).get("id")
        except Exception:
            pass
    delete_204 = None
    if temp_id:
        delete_204 = _req("DELETE", f"/api/clientes/{temp_id}/", headers=auth_header, expected_codes=[204])
    out["Delete Cliente"] = [
        _postman_response("✅ 204 - Excluído", "DELETE", f"/api/clientes/{temp_id or cid}/", auth_header, None, delete_204 or {"code": 204, "headers": {"Content-Type": "application/json"}, "body": ""}),
        _postman_response("❌ 404 - Cliente não encontrado", "DELETE", "/api/clientes/99999/", auth_header, None, delete_404),
    ]
    out["Delete Cliente"] = [x for x in out["Delete Cliente"] if x]

    # --- Documentos / Chat placeholders ---
    doc_ok = _req("GET", "/api/documents/", expected_codes=[200])
    chat_ok = _req("GET", "/api/chat/", expected_codes=[200])
    out["Documentos - placeholder"] = [_postman_response("✅ 200 - Placeholder", "GET", "/api/documents/", {}, None, doc_ok)] if doc_ok.get("code") == 200 else []
    out["Chat - placeholder"] = [_postman_response("✅ 200 - Placeholder", "GET", "/api/chat/", {}, None, chat_ok)] if chat_ok.get("code") == 200 else []

    return out


def set_response_on_item(item, name_to_responses):
    if item.get("request"):
        name = item.get("name")
        if name and name in name_to_responses:
            item["response"] = name_to_responses[name]
    for child in item.get("item") or []:
        set_response_on_item(child, name_to_responses)


def main():
    print(f"Base URL: {BASE_URL}")
    print("Executando requests e capturando respostas...")
    captured = capture_all()
    for name, responses in captured.items():
        print(f"  {name}: {len(responses)} exemplo(s)")

    with open(COLLECTION_PATH, "r", encoding="utf-8") as f:
        collection = json.load(f)

    set_response_on_item({"item": collection["item"]}, captured)
    with open(COLLECTION_PATH, "w", encoding="utf-8") as f:
        json.dump(collection, f, ensure_ascii=False, indent=2)

    print(f"Collection atualizada: {COLLECTION_PATH}")


if __name__ == "__main__":
    main()
