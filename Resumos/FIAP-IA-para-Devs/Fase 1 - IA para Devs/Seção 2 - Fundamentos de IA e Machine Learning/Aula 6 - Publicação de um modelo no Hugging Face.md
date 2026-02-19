# Aula 6 - Publicação de um modelo no Hugging Face

**Fase 1 - IA para Devs** | **Seção 2 - Fundamentos de IA e Machine Learning**

---

## Resumo executivo

Esta aula explora o **Hugging Face** como plataforma de IA e NLP: contexto de **implantação de modelos em produção** (fases de desenvolvimento, teste, validação, deploy), o **ciclo típico de ML** (coleta de dados, pré-processamento, treino, ajuste de hiperparâmetros, validação em teste, versionamento e implantação), e as **ferramentas do Hugging Face** (modelos pré-treinados, biblioteca Transformers, Hub para compartilhar modelos). Inclui o **passo a passo para publicar um modelo**: criar conta, login via `huggingface-cli login`, gerar **Access Token** em Settings → Access Tokens, e usar script/API para subir o modelo no **Hugging Face Hub**. Ao final, você saberá por que versionar e compartilhar modelos e como publicar um modelo na plataforma.

**Objetivos de aprendizagem:**
- Entender as fases de implantação de software e de modelos de ML em produção.
- Descrever o fluxo desde coleta de dados até modelo pronto para deploy.
- Conhecer o ecossistema Hugging Face (Transformers, modelos pré-treinados, Hub).
- Criar conta, token e publicar um modelo no Hugging Face Hub.

---

## Conceitos-chave (flashcards)

**P:** O que é o Hugging Face Hub?  
**R:** Repositório para armazenar, compartilhar e descobrir modelos de Machine Learning (e datasets, espaços); integrado à biblioteca Transformers e à comunidade.

**P:** Para que serve a biblioteca Transformers?  
**R:** Acessar e usar modelos pré-treinados de NLP (e outros domínios); fine-tuning para tarefas específicas; tradução, sumarização, classificação de texto, etc.

**P:** Por que versionar modelos?  
**R:** Permitir implantar novas versões quando o modelo é retreinado ou melhorado; rastreabilidade e rollback; similar ao versionamento de software tradicional.

**P:** O que é necessário para publicar um modelo no Hugging Face?  
**R:** Conta na plataforma, login via CLI (`huggingface-cli login`) ou token; depois, usar a API ou biblioteca (ex.: `huggingface_hub`) para fazer upload do modelo (e opcionalmente de tokenizer, README, etc.).

**P:** O que são modelos pré-treinados no contexto Hugging Face?  
**R:** Modelos treinados em grandes quantidades de dados (ex.: BERT, GPT); podem ser usados ou ajustados (fine-tuned) para tarefas específicas com menos dados e esforço.

---

## Implantação de modelos em produção

- **Fases gerais:** viabilidade, desenvolvimento, teste, validação/homologação, implantação. “Produção” = software/modelo disponível para o usuário final resolver o problema de negócio.
- **Ciclo de ML:** definição do problema → coleta de dados (arquivos, Data Warehouse, Data Lake) → análise exploratória, limpeza e transformação (pré-processamento) → escolha do algoritmo e treino → ajuste de hiperparâmetros (iterativo) → validação com dados de teste → versão pronta para deploy.
- **Papéis:** Cientista de Dados (construção e rastreamento do modelo); Engenheiro de ML / MLOps (colocar o modelo em produção, infraestrutura, versionamento).
- **Versionamento:** essencial para implantar novas versões rapidamente e manter rastreabilidade.

---

## Hugging Face: recursos

- **Modelos pré-treinados:** acesso a modelos de NLP (e outros) já treinados; resultados de qualidade com pouco esforço adicional.
- **Biblioteca Transformers:** código aberto; integração de modelos em aplicações; pipelines e fine-tuning.
- **Comunidade ativa:** compartilhamento de modelos, datasets e boas práticas.
- **Hugging Face Hub:** repositório central para publicar e descobrir modelos (e datasets, Spaces).

Origem: startup focada em chatbots; evoluiu para plataforma líder em NLP e modelos de linguagem.

---

## Publicar modelo no Hub – passo a passo

1. **Conta:** acessar o site do Hugging Face e criar conta (cadastro).
2. **Login no terminal:** `huggingface-cli login` e informar credenciais ou token.
3. **Token:** em Settings (ícone do perfil) → Access Tokens → criar novo token (permissões conforme necessidade: read, write).
4. **Publicar:** usar biblioteca `huggingface_hub` (ou API) para criar o repositório do modelo e fazer upload dos arquivos (modelo, tokenizer, config, README). O vídeo da aula mostra exemplo de script que treina e sobe um modelo.

Exemplo de modelo publicado: disponível no link indicado no material (figura “Modelo Hugging Face”).

---

## Mapa conceitual

```
Publicação no Hugging Face
├── Contexto
│   ├── Implantação em produção
│   ├── Ciclo ML (dados → treino → validação)
│   └── Versionamento de modelos
├── Hugging Face
│   ├── Transformers (biblioteca)
│   ├── Modelos pré-treinados
│   ├── Hub (repositório)
│   └── Comunidade
└── Publicar modelo
    ├── Conta, login (huggingface-cli)
    ├── Access Token (Settings)
    └── Upload (script / huggingface_hub)
```

---

## Receita prática

1. **Antes de publicar:** garantir que o modelo foi treinado e avaliado; decidir o que subir (pesos, config, tokenizer, README com uso).
2. **Conta e token:** criar conta no Hugging Face; gerar token em Settings → Access Tokens; usar `huggingface-cli login` com o token.
3. **Upload:** usar `huggingface_hub` (ex.: `HfApi().upload_file`, ou métodos de push do repositório) para criar o repo e enviar os arquivos.
4. **Documentação:** escrever README no repositório do modelo (como carregar, exemplo de uso, métricas principais) para outros usarem.

---

## Perguntas para teste de reforço

1. Cite duas fases do ciclo de implantação de um modelo de ML. **R:** Ex.: coleta e pré-processamento de dados; treino e ajuste de hiperparâmetros; validação com dados de teste; versionamento e deploy.
2. O que é a biblioteca Transformers do Hugging Face? **R:** Biblioteca que oferece modelos pré-treinados e ferramentas para NLP (e outros); permite usar e fazer fine-tuning de modelos de forma simples.
3. Para que serve o Access Token no Hugging Face? **R:** Autenticar o usuário na API e na CLI para fazer upload de modelos, criar repositórios e acessar recursos privados.
4. Como fazer login no Hugging Face pelo terminal? **R:** Comando `huggingface-cli login` e informar o token (ou credenciais) quando solicitado.
5. Por que o versionamento de modelos é importante? **R:** Permitir deploy de novas versões quando o modelo é atualizado; rastreabilidade e possibilidade de rollback; alinhado às práticas de engenharia de software.

---

## Materiais de apoio

- Hugging Face: [huggingface.co](https://huggingface.co)  
- Documentação Hugging Face Hub: [huggingface.co/docs/hub](https://huggingface.co/docs/hub)  
- Biblioteca Transformers: [huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)  
- huggingface_hub (Python): [pypi.org/project/huggingface-hub](https://pypi.org/project/huggingface-hub)
