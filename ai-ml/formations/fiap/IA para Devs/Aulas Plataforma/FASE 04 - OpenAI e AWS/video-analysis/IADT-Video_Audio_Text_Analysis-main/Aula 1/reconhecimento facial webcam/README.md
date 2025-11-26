# Reconhecimento Facial - Aula 1

**Ambiente configurado com venv!** ✅

---

## 🚀 Setup Rápido

### 1. Ativar Ambiente Virtual

```bash
cd "$(pwd)"
source .venv/bin/activate
```

### 2. IMPORTANTE: Habilitar Webcam (Linux)

**Você precisa executar MANUALMENTE (requer sudo):**

```bash
# Opção A: Executar script
./COMANDOS_EXECUTAR.sh

# Opção B: Copiar comandos
sudo chmod 666 /dev/video0 /dev/video2 /dev/video4
```

**⚠️ Isso é TEMPORÁRIO!** Volta ao normal ao reiniciar.

**Solução permanente (depois):**
```bash
sudo usermod -a -G video $USER
# Fazer logout e login
```

---

## 🧪 Testar Webcam

### Diagnóstico Completo

```bash
source .venv/bin/activate
python3 encontrar_webcam_linux.py
```

**Vai mostrar:**
- Quais câmeras funcionam
- Qual índice usar
- Código pronto para copiar

---

## 📝 Scripts da Aula

### 1. face_detection.py
**Detecção facial** usando Haar Cascade.

```bash
source .venv/bin/activate
python3 face_detection.py
```

### 2. facial_recognition.py
**Reconhecimento facial** com identificação de pessoas.

**Antes de executar:**
1. Criar pasta `images/`
2. Adicionar fotos: `nome1.jpg`, `nome2.jpg`, etc

```bash
source .venv/bin/activate
python3 facial_recognition.py
```

### 3. teste.py
Verificar instalação das bibliotecas.

```bash
source .venv/bin/activate
python3 teste.py
```

---

## 📦 Bibliotecas Instaladas

- opencv-python==4.12.0.88
- numpy==2.2.6

**Face-recognition:** NÃO instalado (requer cmake)

**Para instalar face-recognition (opcional):**
```bash
# Instalar cmake primeiro
sudo apt-get install cmake

# Depois instalar face-recognition
pip install face-recognition
```

---

## ❌ Problema Atual: Webcam

**Diagnóstico executado:**
- ✅ 32 dispositivos /dev/video* encontrados
- ❌ Nenhum captura frames
- 🎯 **Causa:** Falta grupo `video`

**Solução:**
1. Executar `./COMANDOS_EXECUTAR.sh` (temporário)
2. Ou adicionar ao grupo video (permanente)

---

## 📋 Checklist

**Setup:**
- [x] Venv criado
- [x] OpenCV instalado
- [x] numpy instalado
- [ ] Webcam habilitada (precisa permissão sudo)
- [ ] face-recognition instalado (opcional, requer cmake)

**Permissões:**
- [ ] Executar COMANDOS_EXECUTAR.sh
- [ ] OU adicionar ao grupo video (permanente)
- [ ] Testar com encontrar_webcam_linux.py

---

## 🎯 Próximos Passos

1. **Execute manualmente:**
   ```bash
   sudo chmod 666 /dev/video0 /dev/video2
   ```

2. **Teste:**
   ```bash
   source .venv/bin/activate
   python3 encontrar_webcam_linux.py
   ```

3. **Se funcionar:**
   - Executar scripts da aula!
   - Depois: adicionar ao grupo video (permanente)

---

**Ambiente pronto! Só falta a permissão da webcam (manual).** ✅




