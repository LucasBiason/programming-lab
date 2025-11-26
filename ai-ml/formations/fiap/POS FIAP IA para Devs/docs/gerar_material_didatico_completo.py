#!/usr/bin/env python3
"""
Gerador de Material Didático Completo para FIAP
- Cria síntese didática elaborada por AULA
- Atualiza cards do Notion com material completo
- Salva cópias na pasta docs para ia-ml-knowledge-base
"""

import asyncio
import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import PyPDF2

# Caminhos - ESTUDOS (não trabalho)
BASE_DIR = Path(__file__).parent.parent
APOSTILAS_BASE = Path("/home/lucas-biason/Projetos/Estudos/Apostilas e Materiais de Cursos/[FIAP] IA para Devs")
CODIGOS_BASE = BASE_DIR / "Aulas Plataforma"
FORMACAO_BASE = Path("/home/lucas-biason/Projetos/Estudos/Projetos de Acompanhamento de Estudos/IA-Studies/Formação Inteligência Artificial e Machine Learning")
AULAS_PROCESSADAS = Path("/home/lucas-biason/Projetos/Trabalho/Astracode/Scripts/aulas_fiap_processadas_completo.json")
DOCS_DIR = BASE_DIR / "docs" / "material-didatico"

# Importar Notion
sys.path.insert(0, str(Path("/home/lucas-biason/Projetos/Infraestrutura/my-local-place/services/external/notion-automation-suite/src")))
from custom.study_notion import StudyNotion
from services.notion_service import NotionService

async def carregar_env():
    """Carrega variáveis de ambiente"""
    env_file = Path('/home/lucas-biason/Projetos/Infraestrutura/my-local-place/configs/notion-mcp.env')
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

def extrair_texto_pdf(arquivo: Path) -> str:
    """Extrai texto de um PDF"""
    try:
        with open(arquivo, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            texto = ""
            for page in reader.pages[:15]:  # Limitar a 15 páginas para performance
                texto += page.extract_text() + "\n"
            return texto
    except Exception as e:
        return f"[Erro ao extrair PDF {arquivo.name}: {e}]"

def ler_notebook(arquivo: Path) -> Dict[str, Any]:
    """Lê um notebook Jupyter e extrai células de código e markdown"""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        codigo_cells = []
        markdown_cells = []
        
        for cell in notebook.get('cells', []):
            cell_type = cell.get('cell_type', '')
            source = ''.join(cell.get('source', []))
            
            if cell_type == 'code' and source.strip():
                codigo_cells.append({
                    'codigo': source,
                    'outputs': cell.get('outputs', [])
                })
            elif cell_type == 'markdown' and source.strip():
                markdown_cells.append(source)
        
        return {
            'codigo': codigo_cells,
            'markdown': markdown_cells,
            'nome': arquivo.name,
            'caminho': str(arquivo.relative_to(CODIGOS_BASE))
        }
    except Exception as e:
        return {'erro': str(e)}

def encontrar_materiais_completos(aula: Dict[str, Any]) -> Dict[str, Any]:
    """Encontra todos os materiais relacionados: apostilas, códigos, notebooks"""
    titulo = aula.get('titulo', '').lower()
    fase = aula.get('fase')
    numero = aula.get('numero')
    
    materiais = {
        'apostilas': [],
        'codigos': [],
        'notebooks': [],
        'formacao': []
    }
    
    # Buscar apostilas
    if APOSTILAS_BASE.exists():
        fase_dir = APOSTILAS_BASE / f"Fase {fase}" if fase else None
        if fase_dir and fase_dir.exists():
            for arquivo in fase_dir.rglob("*"):
                if arquivo.is_file():
                    if arquivo.suffix.lower() == '.pdf':
                        texto = extrair_texto_pdf(arquivo)
                        materiais['apostilas'].append({
                            'arquivo': arquivo,
                            'nome': arquivo.name,
                            'texto': texto[:15000] if len(texto) > 15000 else texto,
                            'tipo': 'pdf'
                        })
                    elif arquivo.suffix.lower() == '.txt':
                        try:
                            texto = arquivo.read_text(encoding='utf-8')
                            materiais['apostilas'].append({
                                'arquivo': arquivo,
                                'nome': arquivo.name,
                                'texto': texto[:15000] if len(texto) > 15000 else texto,
                                'tipo': 'txt'
                            })
                        except:
                            pass
    
    # Buscar códigos e notebooks
    if CODIGOS_BASE.exists():
        # Buscar por fase
        fase_dirs = []
        for subdir in CODIGOS_BASE.iterdir():
            if subdir.is_dir():
                if fase and (f"fase {fase}" in subdir.name.lower() or f"fase{fase}" in subdir.name.lower() or f"FASE {fase:02d}" in subdir.name or f"FASE 0{fase}" in subdir.name):
                    fase_dirs.append(subdir)
                elif not fase:
                    fase_dirs.append(subdir)
        
        for fase_dir in fase_dirs:
            for arquivo in fase_dir.rglob("*"):
                if arquivo.is_file():
                    if arquivo.suffix == '.ipynb':
                        notebook = ler_notebook(arquivo)
                        if 'erro' not in notebook:
                            materiais['notebooks'].append(notebook)
                    elif arquivo.suffix == '.py':
                        try:
                            codigo = arquivo.read_text(encoding='utf-8')
                            materiais['codigos'].append({
                                'arquivo': arquivo,
                                'nome': arquivo.name,
                                'codigo': codigo,
                                'caminho': str(arquivo.relative_to(CODIGOS_BASE))
                            })
                        except:
                            pass
    
    return materiais

def extrair_conceitos_das_apostilas(apostilas: List[Dict]) -> Dict[str, str]:
    """Extrai conceitos reais das apostilas"""
    conceitos = {}
    texto_completo = ""
    
    for apostila in apostilas:
        texto_completo += " " + apostila.get('texto', '')
    
    # Buscar definições de conceitos nas apostilas
    padroes = {
        r'(?:Inteligência Artificial|IA)\s+é\s+([^\.]+)': 'Inteligência Artificial',
        r'(?:Machine Learning|ML)\s+é\s+([^\.]+)': 'Machine Learning',
        r'(?:Deep Learning)\s+é\s+([^\.]+)': 'Deep Learning',
        r'(?:NumPy)\s+é\s+([^\.]+)': 'NumPy',
        r'(?:Pandas)\s+é\s+([^\.]+)': 'Pandas',
        r'(?:Scikit-learn|sklearn)\s+é\s+([^\.]+)': 'Scikit-learn',
    }
    
    for padrao, termo in padroes.items():
        matches = re.finditer(padrao, texto_completo, re.IGNORECASE)
        for match in matches:
            definicao = match.group(1).strip()
            if len(definicao) > 20 and len(definicao) < 300:
                conceitos[termo] = definicao
                break
    
    return conceitos

def extrair_conceitos_elaborados(conteudo_plataforma: str, apostilas: List[Dict], codigos: List[Dict]) -> List[Dict[str, Any]]:
    """Extrai conceitos principais de forma elaborada"""
    conceitos = []
    
    # Extrair conceitos das apostilas primeiro
    conceitos_apostilas = extrair_conceitos_das_apostilas(apostilas)
    
    # Combinar todo o texto
    texto_completo = conteudo_plataforma.lower()
    for apostila in apostilas:
        texto_completo += " " + apostila.get('texto', '').lower()
    
    # Conceitos fundamentais de IA/ML com definições base
    conceitos_base = {
        'inteligência artificial': {
            'definicao': conceitos_apostilas.get('Inteligência Artificial', 'Campo da ciência da computação que busca criar sistemas capazes de realizar tarefas que normalmente requerem inteligência humana'),
            'contexto': 'Base de todo o curso, estabelece o contexto histórico e evolutivo da IA',
            'aplicacoes': 'Assistentes virtuais, sistemas de recomendação, carros autônomos, diagnóstico médico'
        },
        'machine learning': {
            'definicao': conceitos_apostilas.get('Machine Learning', 'Subcampo da IA que permite que sistemas aprendam e melhorem automaticamente a partir da experiência'),
            'contexto': 'Técnica central para criar sistemas inteligentes sem programação explícita',
            'aplicacoes': 'Classificação de emails, previsão de preços, reconhecimento de imagens'
        },
        'deep learning': {
            'definicao': conceitos_apostilas.get('Deep Learning', 'Subcampo do ML que usa redes neurais com múltiplas camadas para aprender representações hierárquicas'),
            'contexto': 'Revolucionou áreas como visão computacional e processamento de linguagem natural',
            'aplicacoes': 'Reconhecimento de imagens, tradução automática, geração de texto'
        },
        'numpy': {
            'definicao': conceitos_apostilas.get('NumPy', 'Biblioteca fundamental para computação científica em Python, fornecendo arrays multidimensionais eficientes'),
            'contexto': 'Base para todas as bibliotecas de ML, essencial para operações numéricas',
            'aplicacoes': 'Processamento de imagens, cálculos matemáticos, manipulação de dados'
        },
        'pandas': {
            'definicao': conceitos_apostilas.get('Pandas', 'Biblioteca Python para manipulação e análise de dados estruturados, fornecendo DataFrames'),
            'contexto': 'Essencial para preparação de dados antes do treinamento de modelos',
            'aplicacoes': 'Análise de dados, limpeza de datasets, feature engineering'
        },
        'scikit-learn': {
            'definicao': conceitos_apostilas.get('Scikit-learn', 'Biblioteca robusta para Machine Learning em Python, oferecendo algoritmos prontos para uso'),
            'contexto': 'Padrão da indústria para implementação de modelos clássicos de ML',
            'aplicacoes': 'Regressão, classificação, clustering, redução de dimensionalidade'
        }
    }
    
    # Verificar quais conceitos aparecem no conteúdo
    for termo, info in conceitos_base.items():
        if termo in texto_completo or termo.replace(' ', '') in texto_completo:
            conceitos.append({
                'termo': termo.title(),
                'definicao': info['definicao'],
                'contexto': info['contexto'],
                'aplicacoes': info['aplicacoes'],
                'importancia': 'alta'
            })
    
    return conceitos[:10]

def gerar_flashcards_elaborados(conceitos: List[Dict], conteudo: str) -> List[Dict[str, str]]:
    """Gera flashcards didáticos elaborados"""
    flashcards = []
    
    for conceito in conceitos[:8]:
        termo = conceito['termo']
        definicao = conceito.get('definicao', '')
        aplicacoes = conceito.get('aplicacoes', '')
        
        flashcards.append({
            'pergunta': f"O que é {termo} e quais suas principais aplicações?",
            'resposta': f"{termo} é {definicao}. Principais aplicações: {aplicacoes}",
            'exemplo': f"Exemplo prático: {aplicacoes.split(',')[0] if aplicacoes else 'Ver exemplos nos códigos'}"
        })
    
    return flashcards

def criar_exemplo_passo_a_passo_detalhado(notebook: Dict[str, Any]) -> Dict[str, Any]:
    """Cria exemplo passo a passo didático detalhado a partir de código"""
    exemplo = {
        'titulo': notebook.get('nome', 'Exemplo Prático').replace('.ipynb', ''),
        'objetivo': '',
        'passos': [],
        'codigo_completo': ''
    }
    
    codigo_cells = notebook.get('codigo', [])
    markdown_cells = notebook.get('markdown', [])
    
    # Usar markdown como explicação
    explicacao = '\n'.join(markdown_cells[:3]) if markdown_cells else "Exemplo prático passo a passo"
    exemplo['objetivo'] = explicacao[:400]
    
    # Criar passos detalhados
    for i, cell in enumerate(codigo_cells[:10], 1):
        codigo_cell = cell.get('codigo', '')
        if codigo_cell.strip():
            # Extrair explicação do código (comentários, docstrings)
            explicacao_codigo = ""
            linhas = codigo_cell.split('\n')
            for linha in linhas[:5]:
                if linha.strip().startswith('#') or '"""' in linha or "'''" in linha:
                    explicacao_codigo += linha.strip() + " "
            
            exemplo['passos'].append({
                'numero': i,
                'explicacao': explicacao_codigo[:200] if explicacao_codigo else f"Passo {i}: Executar código",
                'codigo': codigo_cell[:1000],
                'resultado_esperado': "Resultado será exibido após execução. Verifique a saída para entender o comportamento."
            })
    
    exemplo['codigo_completo'] = '\n\n'.join([cell.get('codigo', '') for cell in codigo_cells])
    
    return exemplo

def gerar_exercicios_elaborados(conceitos: List[Dict], codigos: List[Dict], notebooks: List[Dict]) -> List[Dict[str, Any]]:
    """Gera exercícios práticos elaborados com respostas completas"""
    exercicios = []
    
    # Exercício 1: Conceitual
    if conceitos:
        termo = conceitos[0]['termo']
        definicao = conceitos[0].get('definicao', '')
        contexto = conceitos[0].get('contexto', '')
        aplicacoes = conceitos[0].get('aplicacoes', '')
        exercicios.append({
            'tipo': 'conceitual',
            'nivel': 'iniciante',
            'enunciado': f"Explique detalhadamente o que é {termo}, seu contexto histórico e dê 3 exemplos práticos de aplicação.",
            'resposta': f"{termo} é {definicao}. Contexto: {contexto}. Exemplos práticos:\n1. {aplicacoes.split(',')[0] if aplicacoes else 'Ver material'}\n2. {aplicacoes.split(',')[1] if len(aplicacoes.split(',')) > 1 else 'Ver material'}\n3. {aplicacoes.split(',')[2] if len(aplicacoes.split(',')) > 2 else 'Ver material'}",
            'dica': f"Revise o material sobre {termo} e os códigos de exemplo relacionados."
        })
    
    # Exercício 2: Prático com código
    if codigos:
        codigo_exemplo = codigos[0]
        nome_codigo = codigo_exemplo['nome']
        codigo_ref = codigo_exemplo.get('codigo', '')[:600]
        exercicios.append({
            'tipo': 'pratico',
            'nivel': 'intermediario',
            'enunciado': f"Analise o código em {nome_codigo} linha por linha. Explique o que cada parte faz e modifique-o para adicionar tratamento de erros e logging.",
            'resposta': f"O código em {nome_codigo} implementa [funcionalidade específica]. Para modificá-lo:\n\n1. **Adicionar tratamento de erros:**\n```python\ntry:\n    # código original\nexcept Exception as e:\n    print(f'Erro: {{e}}')\n```\n\n2. **Adicionar logging:**\n```python\nimport logging\nlogging.basicConfig(level=logging.INFO)\nlogging.info('Processando...')\n```\n\n3. **Validar entradas:**\n```python\nif not entrada:\n    raise ValueError('Entrada inválida')\n```\n\n4. **Adicionar documentação:**\n```python\ndef funcao(parametro):\n    \"\"\"\n    Descrição da função\n    Args:\n        parametro: descrição\n    Returns:\n        descrição do retorno\n    \"\"\"\n```",
            'dica': "Revise o código original, execute-o primeiro para entender o comportamento, depois adicione melhorias incrementalmente.",
            'codigo_referencia': codigo_ref
        })
    
    # Exercício 3: Notebook
    if notebooks:
        notebook = notebooks[0]
        nome_notebook = notebook.get('nome', '')
        exercicios.append({
            'tipo': 'notebook',
            'nivel': 'avancado',
            'enunciado': f"Execute o notebook {nome_notebook} célula por célula. Para cada célula, explique o que ela faz, qual o resultado esperado, e crie uma nova célula que expande o conceito aprendido.",
            'resposta': "Cada célula do notebook demonstra conceitos específicos. Para expandir:\n\n1. **Execute e observe:** Execute cada célula e observe os resultados antes de prosseguir\n\n2. **Modifique parâmetros:** Altere valores e veja o impacto nos resultados\n\n3. **Crie visualizações:** Adicione gráficos para melhor compreensão\n\n4. **Documente insights:** Crie células markdown documentando o que aprendeu\n\n5. **Experimente variações:** Tente diferentes abordagens e compare resultados",
            'dica': "Execute célula por célula, observe os resultados antes de criar novas, e documente seu aprendizado.",
            'notebook_referencia': nome_notebook
        })
    
    return exercicios

def criar_sintese_didatica_elaborada(aula: Dict[str, Any], materiais: Dict[str, Any]) -> str:
    """Cria síntese didática completa e elaborada"""
    
    titulo = aula.get('titulo', 'Aula')
    conteudo_plataforma = aula.get('conteudo', '')
    fase = aula.get('fase', 'N/A')
    numero = aula.get('numero', 'N/A')
    
    # Extrair conceitos
    conceitos = extrair_conceitos_elaborados(
        conteudo_plataforma,
        materiais['apostilas'],
        materiais['codigos']
    )
    
    # Gerar flashcards
    flashcards = gerar_flashcards_elaborados(conceitos, conteudo_plataforma)
    
    # Criar exemplos passo a passo
    exemplos = []
    for notebook in materiais['notebooks'][:3]:
        exemplo = criar_exemplo_passo_a_passo_detalhado(notebook)
        exemplos.append(exemplo)
    
    # Gerar exercícios
    exercicios = gerar_exercicios_elaborados(
        conceitos,
        materiais['codigos'],
        materiais['notebooks']
    )
    
    # Montar síntese completa
    sintese = f"""# 📚 {titulo}

## 🎯 OBJETIVOS DE APRENDIZAGEM

Ao final desta aula, você será capaz de:
- Compreender os conceitos fundamentais apresentados
- Aplicar os conhecimentos em exemplos práticos
- Resolver exercícios relacionados aos tópicos abordados
- Integrar o aprendizado com projetos práticos

---

## 📖 CONCEITOS PRINCIPAIS

"""
    
    for i, conceito in enumerate(conceitos, 1):
        termo = conceito['termo']
        definicao = conceito.get('definicao', '')
        contexto = conceito.get('contexto', '')
        aplicacoes = conceito.get('aplicacoes', '')
        importancia = conceito.get('importancia', 'média').upper()
        
        sintese += f"""
### {i}. {termo}

**Definição:** {definicao}

**Contexto:** {contexto}

**Aplicações Práticas:**
- {aplicacoes.replace(', ', '\n- ') if aplicacoes else 'Ver exemplos nos códigos'}

**Importância:** {importancia}

"""
    
    sintese += "\n---\n\n## 🎴 FLASHCARDS DE REVISÃO\n\n"
    
    for i, flashcard in enumerate(flashcards, 1):
        sintese += f"""
### Flashcard {i}

**❓ Pergunta:** {flashcard['pergunta']}

**✅ Resposta:** {flashcard['resposta']}

**💡 Exemplo:** {flashcard.get('exemplo', 'Ver exemplos práticos abaixo')}

"""
    
    sintese += "\n---\n\n## 💻 EXEMPLOS PRÁTICOS PASSO A PASSO\n\n"
    
    for exemplo in exemplos:
        sintese += f"""
### {exemplo['titulo']}

**🎯 Objetivo:** {exemplo['objetivo']}

**📝 Passos:**

"""
        for passo in exemplo['passos']:
            sintese += f"""
#### Passo {passo['numero']}: {passo['explicacao']}

```python
{passo['codigo']}
```

**Resultado Esperado:** {passo['resultado_esperado']}

"""
    
    sintese += "\n---\n\n## ✏️ EXERCÍCIOS PRÁTICOS\n\n"
    
    for i, exercicio in enumerate(exercicios, 1):
        sintese += f"""
### Exercício {i} - Nível {exercicio['nivel'].upper()}

**Tipo:** {exercicio['tipo'].title()}

**📋 Enunciado:**

{exercicio['enunciado']}

**💡 Dica:** {exercicio.get('dica', 'Revise os materiais antes de começar')}

**✅ Resposta:**

{exercicio['resposta']}

"""
        if 'codigo_referencia' in exercicio:
            sintese += f"\n**Código de Referência:**\n\n```python\n{exercicio['codigo_referencia']}\n```\n"
    
    sintese += f"""

---

## 📄 MATERIAIS DISPONÍVEIS

### Apostilas ({len(materiais['apostilas'])} arquivo(s))
"""
    
    for apostila in materiais['apostilas'][:5]:
        sintese += f"- **{apostila['nome']}** ({apostila['tipo'].upper()})\n"
    
    sintese += f"""

### Códigos e Notebooks ({len(materiais['codigos']) + len(materiais['notebooks'])} arquivo(s))
"""
    
    for codigo in materiais['codigos'][:5]:
        sintese += f"- **{codigo['nome']}** (Python)\n"
    
    for notebook in materiais['notebooks'][:5]:
        sintese += f"- **{notebook['nome']}** (Jupyter Notebook)\n"
    
    sintese += f"""

---

## 🔗 INTEGRAÇÃO COM IA/ML KNOWLEDGE BASE

Os conceitos e exemplos desta aula podem ser expandidos no projeto **ia-ml-knowledge-base**:

- **Categoria:** Fundamentos de IA
- **Tags:** {', '.join([c['termo'] for c in conceitos[:5]])}
- **Nível:** Iniciante a Intermediário
- **Pré-requisitos:** Conhecimento básico de Python

---

## 📊 RESUMO EXECUTIVO

Esta aula apresenta os fundamentos essenciais, combinando teoria e prática através de:

- **{len(conceitos)} conceitos principais** explicados de forma didática
- **{len(flashcards)} flashcards** para revisão rápida
- **{len(exemplos)} exemplos práticos** passo a passo
- **{len(exercicios)} exercícios** com respostas detalhadas
- **{len(materiais['apostilas'])} apostilas** e **{len(materiais['codigos']) + len(materiais['notebooks'])} códigos** de referência

**Próximos Passos:**
1. Revisar os flashcards diariamente
2. Executar todos os exemplos práticos
3. Resolver os exercícios propostos
4. Explorar os materiais adicionais
5. Contribuir com exemplos no ia-ml-knowledge-base

---

**Última Atualização:** {datetime.now().strftime('%d/%m/%Y %H:%M')}
**Fase:** {fase} | **Aula:** {numero}
"""
    
    return sintese

async def buscar_cards_fase1(notion_service: NotionService, database_id: str) -> List[Dict[str, Any]]:
    """Busca cards da Fase 1 no Notion"""
    print("\n🔍 Buscando cards da Fase 1 no Notion...")
    
    all_cards = []
    start_cursor = None
    
    while True:
        result = await notion_service.query_database(
            database_id=database_id,
            start_cursor=start_cursor,
            page_size=100
        )
        
        cards = result.get("results", [])
        all_cards.extend(cards)
        
        if not result.get("has_more", False):
            break
            
        start_cursor = result.get("next_cursor")
    
    # Filtrar cards da Fase 1
    cards_fase1 = []
    for card in all_cards:
        props = card.get('properties', {})
        title_prop = props.get('Project name', {})
        
        if title_prop:
            title = title_prop.get('title', [{}])[0].get('plain_text', '').lower()
            if 'fase 1' in title or 'welcome' in title or 'fundamentos' in title:
                cards_fase1.append({
                    'id': card['id'],
                    'title': title_prop.get('title', [{}])[0].get('plain_text', ''),
                    'properties': props
                })
    
    print(f"✅ Encontrados {len(cards_fase1)} cards da Fase 1")
    return cards_fase1

def match_aula_card(aula: Dict[str, Any], cards: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Faz match entre aula e card do Notion"""
    titulo_aula = aula.get('titulo', '').lower()
    
    for card in cards:
        titulo_card = card['title'].lower()
        
        # Match simples por palavras-chave
        palavras_aula = set(re.findall(r'\b\w{4,}\b', titulo_aula))
        palavras_card = set(re.findall(r'\b\w{4,}\b', titulo_card))
        palavras_comuns = palavras_aula.intersection(palavras_card)
        
        if len(palavras_comuns) >= 2:
            return card
    
    return None

async def atualizar_card_notion(notion_service: NotionService, card_id: str, sintese: str, arquivo_docs: Path):
    """Atualiza card no Notion com síntese didática"""
    try:
        # Criar resumo curto para Notion (limite 2000 chars)
        # Incluir apenas objetivos, conceitos principais e link para arquivo completo
        resumo_notion = f"""# 📚 Material Didático Completo

## 🎯 Objetivos de Aprendizagem
{sintese.split('## 🎯 OBJETIVOS DE APRENDIZAGEM')[1].split('---')[0] if '## 🎯 OBJETIVOS DE APRENDIZAGEM' in sintese else 'Ver arquivo completo'}

## 📖 Conceitos Principais
{sintese.split('## 📖 CONCEITOS PRINCIPAIS')[1].split('---')[0][:800] if '## 📖 CONCEITOS PRINCIPAIS' in sintese else 'Ver arquivo completo'}

---

📄 **Material completo disponível em:** `{arquivo_docs.name}`

💡 **Localização:** `docs/material-didatico/`

📊 **Conteúdo completo inclui:**
- Conceitos detalhados com exemplos
- Flashcards de revisão
- Exemplos práticos passo a passo
- Exercícios com respostas completas
- Referências a materiais e códigos

**Última Atualização:** {datetime.now().strftime('%d/%m/%Y %H:%M')}
"""
        
        # Garantir que fique abaixo de 2000
        if len(resumo_notion) >= 2000:
            resumo_notion = resumo_notion[:1980] + "\n[...]"
        
        await notion_service.update_page(
            page_id=card_id,
            properties={
                "Descrição": {
                    "rich_text": [{"text": {"content": resumo_notion}}]
                }
            }
        )
        return True
    except Exception as e:
        print(f"   ❌ Erro ao atualizar card: {e}")
        return False

async def processar_fase1_completa():
    """Processa todas as aulas da Fase 1"""
    print("=" * 70)
    print("GERADOR DE MATERIAL DIDÁTICO - FASE 1 COMPLETA")
    print("=" * 70)
    
    await carregar_env()
    
    token = os.getenv("NOTION_API_TOKEN") or os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_STUDIES_DATABASE_ID")
    
    if not token or not database_id:
        print("❌ Variáveis de ambiente não configuradas")
        return
    
    # Criar pasta docs
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📁 Pasta docs: {DOCS_DIR}")
    
    # Carregar aulas processadas
    with open(AULAS_PROCESSADAS, 'r', encoding='utf-8') as f:
        aulas = json.load(f)
    
    # Filtrar aulas da Fase 1
    aulas_fase1 = [a for a in aulas if a.get('fase') == 1 or 'welcome' in a.get('titulo', '').lower() or 'fundamentos' in a.get('titulo', '').lower()]
    
    print(f"\n📖 Encontradas {len(aulas_fase1)} aulas da Fase 1")
    
    # Conectar ao Notion
    notion_service = NotionService(token)
    cards_fase1 = await buscar_cards_fase1(notion_service, database_id)
    
    # Processar cada aula
    atualizadas = 0
    
    for i, aula in enumerate(aulas_fase1, 1):
        print(f"\n{'='*70}")
        print(f"[{i}/{len(aulas_fase1)}] Processando: {aula.get('titulo', 'N/A')[:60]}...")
        print(f"{'='*70}")
        
        # Encontrar materiais
        materiais = encontrar_materiais_completos(aula)
        print(f"   📚 Apostilas: {len(materiais['apostilas'])}")
        print(f"   💻 Códigos: {len(materiais['codigos'])}")
        print(f"   📓 Notebooks: {len(materiais['notebooks'])}")
        
        # Gerar síntese didática
        sintese = criar_sintese_didatica_elaborada(aula, materiais)
        
        # Salvar em arquivo na pasta docs
        titulo_limpo = re.sub(r'[^\w\s-]', '', aula.get('titulo', 'aula')).strip().replace(' ', '_')
        arquivo_docs = DOCS_DIR / f"fase1_{titulo_limpo}.md"
        arquivo_docs.write_text(sintese, encoding='utf-8')
        print(f"   💾 Salvo em: {arquivo_docs}")
        
        # Fazer match com card
        card = match_aula_card(aula, cards_fase1)
        
        if card:
            print(f"   ✅ Match encontrado: {card['title']}")
            if await atualizar_card_notion(notion_service, card['id'], sintese, arquivo_docs):
                atualizadas += 1
                print(f"   ✅ Card atualizado no Notion!")
        else:
            print(f"   ⚠️  Nenhum card encontrado")
    
    print(f"\n{'='*70}")
    print(f"✅ PROCESSAMENTO CONCLUÍDO!")
    print(f"{'='*70}")
    print(f"   - Cards atualizados: {atualizadas}")
    print(f"   - Arquivos salvos em: {DOCS_DIR}")
    print(f"   - Total processado: {len(aulas_fase1)}")

if __name__ == "__main__":
    asyncio.run(processar_fase1_completa())
