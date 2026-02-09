# Postman – Jury AI (Bloco 2)

## Collection e exemplos

- **collection.json** – Collection com todos os endpoints (Auth, Clientes, Documentos, Chat). Cada request tem **exemplos de resposta gravados a partir da execução real da API** (casos de sucesso e de erro).
- **environment.json** – Variáveis para ambiente local (`base_url`, `user_email`, `user_password`, etc.).

## Atualizar exemplos (respostas reais)

Os exemplos de request/response da collection são gerados pelo script que **executa cada request na API** e grava o resultado em `collection.json`:

1. Suba o servidor Django: `cd jury_ai && python3 manage.py runserver 127.0.0.1:8000`
2. Rode o script de captura:
   ```bash
   python3 scripts/capture_postman_examples.py http://localhost:8000
   ```
   Ou com variável de ambiente: `BASE_URL=http://localhost:8000 python3 scripts/capture_postman_examples.py`

Isso regrava os exemplos de **sucesso e erro** (201, 200, 204, 400, 401, 404) em cada item da collection.

## Executar testes (Newman)

```bash
./scripts/run_newman.sh
```

Requer servidor rodando em `base_url` (ex.: http://localhost:8000) e ambiente com `user_email`/`user_password` (ex.: teste@jury.ai / senha1234). Dados de teste: `python3 manage.py seed` (em `jury_ai/`).
