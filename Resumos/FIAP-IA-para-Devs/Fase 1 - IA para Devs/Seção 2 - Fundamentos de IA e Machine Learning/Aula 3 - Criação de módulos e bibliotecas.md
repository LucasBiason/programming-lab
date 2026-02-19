# Aula 3 - Criação de módulos e bibliotecas

**Fase 1 - IA para Devs** | **Seção 2 - Fundamentos de IA e Machine Learning**

---

## Resumo executivo

Esta aula ensina a **criar módulos e bibliotecas em Python**: definição de **módulo** (arquivo `.py` com funções, classes e variáveis) e **biblioteca** (coleção de módulos com funcionalidades específicas), motivações (organização, reutilização, testes, escalabilidade), **passo a passo** para criar um módulo (ex.: `investimentos.py` com funções de retorno, juros compostos, CAGR, conversão de taxas), uso em outro arquivo (`import investimentos`), e **criação de uma biblioteca** com estrutura de pacote (`__init__.py`, `setup.py`, `README.md`, testes com `unittest`) e **publicação no PyPI**. Ao final, você saberá organizar código em módulos e empacotar uma biblioteca para distribuição.

**Objetivos de aprendizagem:**

- Diferenciar módulo e biblioteca (pacote).
- Criar um módulo com funções documentadas (docstrings) e importá-lo.
- Estruturar um pacote (pastas, `__init__.py`, `setup.py`).
- Escrever testes unitários com `unittest` para o módulo.
- Conhecer o processo de publicação no PyPI (pip install).

---

## Conceitos-chave (flashcards)

**P:** O que é um módulo em Python?  
**R:** Arquivo `.py` contendo definições de funções, classes e variáveis; permite organizar e reutilizar código.

**P:** O que é uma biblioteca (pacote) em Python?  
**R:** Coleção de módulos organizados em um diretório, com `__init__.py` e, para distribuição, `setup.py` e metadados.

**P:** Para que serve o `__init__.py`?  
**R:** Marca o diretório como pacote Python; pode estar vazio ou exportar símbolos do pacote (ex.: `from .investimentos import calcular_retorno`).

**P:** O que é o setup.py?  
**R:** Script usado pelo setuptools para definir nome, versão, pacotes, dependências e metadados do projeto para instalação (pip) e publicação no PyPI.

**P:** Por que criar módulos e bibliotecas?  
**R:** Organização do código, reutilização entre projetos, facilidade de testes (isolamento) e escalabilidade em projetos maiores.

---

## Módulo: exemplo investimentos

Funções típicas em um módulo de investimentos (conforme conteúdo didático):

- **calcular_retorno_investimento(valor_inicial, valor_final):** retorno em porcentagem.
- **calcular_juros_compostos(principal, taxa_juros_anual, periodos):** valor final com juros compostos.
- **converter_taxa_anual_para_mensal(taxa_anual):** conversão de taxa anual para mensal.
- **calcular_cagr(valor_inicial, valor_final, anos):** taxa de crescimento anual composta (CAGR).

Uso em outro arquivo: `import investimentos` e depois `investimentos.calcular_retorno_investimento(1000, 1500)`.

---

## Estrutura de uma biblioteca (pacote)

```
meu_investimento/
├── investimentos/
│   ├── __init__.py      # exporta funções do pacote
│   └── investimentos.py # implementação
├── tests/
│   └── test_investimentos.py  # unittest
├── setup.py             # setuptools: name, version, packages, install_requires
├── README.md
└── LICENSE
```

- **setup.py:** `find_packages()`, `install_requires=[]`, `author`, `description`, `classifiers`, `python_requires='>=3.6'`.
- ****init**.py:** `from .investimentos import calcular_retorno_investimento, calcular_juros_compostos, ...`
- **Testes:** `unittest.TestCase`, `assertAlmostEqual` para valores float; rodar com `python -m unittest`.

---

## Publicação no PyPI

1. Conta no PyPI (pypi.org).
2. Gerar distribuição: `python setup.py sdist bdist_wheel` (ou `build`).
3. Publicar: `twine upload dist/*` (com usuário e senha ou token).
4. Instalação por terceiros: `pip install meu_investimento`.

---

## Mapa conceitual

```
Módulos e bibliotecas
├── Módulo
│   ├── Arquivo .py com funções/classes
│   ├── Docstrings (Args, Returns)
│   └── import em outro arquivo
├── Biblioteca (pacote)
│   ├── Diretório com __init__.py
│   ├── setup.py (setuptools)
│   ├── README, LICENSE
│   └── tests/
└── Distribuição
    ├── PyPI (pip install)
    └── twine upload
```

---

## Receita prática

1. **Módulo:** criar arquivo `.py` com funções bem nomeadas e docstrings; importar onde for usar.
2. **Pacote:** criar pasta com `__init__.py` e módulos; em `__init__.py` exportar o que é público.
3. **setup.py:** preencher name, version, packages=find_packages(), install_requires, classifiers.
4. **Testes:** escrever `test_*.py` com unittest; rodar antes de publicar.
5. **PyPI:** criar conta, gerar dist, usar twine para upload.

---

## Perguntas para teste de reforço

1. Qual a diferença entre módulo e biblioteca? **R:** Módulo é um arquivo .py; biblioteca é um conjunto de módulos organizados em pacote (com **init**.py e setup.py para distribuição).
2. Para que serve o arquivo **init**.py? **R:** Marcar o diretório como pacote e opcionalmente exportar símbolos.
3. O que o setup.py define? **R:** Nome do pacote, versão, lista de pacotes, dependências, metadados para instalação e PyPI.
4. Como testar um módulo de forma automatizada? **R:** Usar unittest (ou pytest) em arquivos test\_\*.py.
5. Como alguém instala uma biblioteca que você publicou no PyPI? **R:** `pip install nome_do_pacote`.

---

## Materiais de apoio

- Documentação Python – Módulos: [docs.python.org/tutorial/modules](https://docs.python.org/3/tutorial/modules.html)
- setuptools: [setuptools.pypa.io](https://setuptools.pypa.io)
- PyPI: [pypi.org](https://pypi.org)
- twine (upload): [pypi.org/project/twine](https://pypi.org/project/twine)
