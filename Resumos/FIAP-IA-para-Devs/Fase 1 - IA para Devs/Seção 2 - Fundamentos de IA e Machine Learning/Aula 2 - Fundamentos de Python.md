# Aula 2 - Fundamentos de Python

**Fase 1 - IA para Devs** | **Seção 2 - Fundamentos de IA e Machine Learning**

---

## Resumo executivo

Esta aula cobre os **fundamentos do Python** necessários para desenvolvimento e ML: estruturas de dados (listas, tuplas, conjuntos, dicionários), **controle de fluxo** (if/elif/else, for, while), **funções** (def, argumentos padrão, lambda), **manipulação de arquivos** (leitura e escrita com `with`), **módulos e pacotes** (import, criação de módulos), **tratamento de exceções** (try/except, raise), **compreensão de listas**, **decoradores** e **context managers**. Ao final, você terá base sólida para escrever e organizar código Python.

**Objetivos de aprendizagem:**
- Usar listas, tuplas, conjuntos e dicionários de forma adequada.
- Aplicar condicionais e laços (for, while).
- Definir e chamar funções, incluindo lambda e argumentos padrão.
- Ler e escrever arquivos com segurança (with).
- Importar e criar módulos.
- Tratar exceções e lançar erros quando necessário.
- Escrever list comprehensions, decoradores e context managers básicos.

---

## Conceitos-chave (flashcards)

**P:** Qual a diferença entre lista e tupla?  
**R:** Lista é ordenada e mutável `[]`; tupla é ordenada e imutável `()`. Use tupla quando os dados não devem mudar.

**P:** O que caracteriza um conjunto (set)?  
**R:** Elementos únicos, sem repetição; não garante ordem; definido com `{}` (ou `set()`).

**P:** Como acessar um valor em um dicionário?  
**R:** Por chave: `dicionario['chave']` ou `dicionario.get('chave')`. Dicionários são pares chave-valor.

**P:** O que faz o `with open(...)`?  
**R:** Abre o arquivo e garante fechamento ao sair do bloco, mesmo em caso de erro (context manager).

**P:** Para que serve uma função lambda?  
**R:** Definir funções pequenas e anônimas em uma expressão: `lambda x: x * 2`. Útil como argumento (ex.: sort, map).

**P:** O que é um decorador?  
**R:** Função que recebe outra função e modifica ou estende seu comportamento, usando `@nome_do_decorador` acima da definição.

**P:** O que é um context manager?  
**R:** Objeto que define `__enter__` e `__exit__`, usado com `with` para alocar e liberar recursos (arquivos, locks) de forma segura.

**P:** O que é list comprehension?  
**R:** Forma concisa de criar lista: `[x**2 for x in range(10)]` gera lista dos quadrados de 0 a 9.

---

## Estruturas de dados

- **Listas** `[]`: ordenadas, mutáveis; `append`, `extend`, indexação, fatiamento.
- **Tuplas** `()`: ordenadas, imutáveis; úteis para retorno múltiplo e chaves de dicionário.
- **Conjuntos** `{}`: elementos únicos; operações de conjunto (união, interseção); sem ordem garantida.
- **Dicionários** `{chave: valor}`: acesso por chave; `keys()`, `values()`, `items()`.

---

## Controle de fluxo e funções

- **Condicionais:** `if`, `elif`, `else` com indentação.
- **Laços:** `for item in iterável`, `for i in range(n)`; `while condição` com cuidado para não loop infinito.
- **Funções:** `def nome(args):`; `return`; argumentos padrão `def f(x=1)`; `*args`, `**kwargs` quando necessário.
- **Lambda:** `lambda x: expressão` para funções anônimas de uma linha.

---

## Arquivos, módulos e exceções

- **Arquivos:** `open('arquivo.txt', 'r'/'w'/'a')`; preferir `with open(...) as f:` para leitura/escrita.
- **Módulos:** `import math`, `from meu_modulo import funcao`; criar arquivo `.py` com funções/classes para reutilizar.
- **Exceções:** `try:` / `except TipoErro:` / `finally:`; `raise ValueError("mensagem")` para sinalizar erro.

---

## Recursos avançados (resumo)

- **List comprehension:** `[expr for x in iterable if condição]`.
- **Decorador:** função que envolve outra; `def decorador(f): return wrapper`.
- **Context manager:** classe com `__enter__` e `__exit__` para uso com `with`.

---

## Mapa conceitual

```
Fundamentos de Python
├── Estruturas de dados
│   ├── Listas, tuplas
│   ├── Conjuntos
│   └── Dicionários
├── Controle de fluxo
│   ├── if / elif / else
│   └── for, while
├── Funções
│   ├── def, return, argumentos
│   └── lambda
├── Arquivos e módulos
│   ├── open, with
│   └── import, criar módulo
├── Exceções
│   ├── try / except
│   └── raise
└── Recursos
    ├── List comprehension
    ├── Decoradores
    └── Context managers
```

---

## Receita prática

1. **Dados:** escolher lista (mutável), tupla (imutável), set (únicos) ou dict (chave-valor) conforme o problema.
2. **Lógica:** usar condicionais e laços; extrair trechos repetidos para funções.
3. **Arquivos:** sempre usar `with open(...)` para não esquecer de fechar.
4. **Organização:** colocar funções reutilizáveis em módulos (arquivos `.py`) e importar onde precisar.
5. **Erros:** tratar exceções esperadas com `try/except`; usar `raise` para contratos e validações.

---

## Perguntas para teste de reforço

1. Como criar uma lista com os quadrados de 0 a 9 em uma linha? **R:** `[x**2 for x in range(10)]`.
2. O que imprime `print({1,2,2,3})`? **R:** `{1, 2, 3}` (conjunto sem repetição).
3. Para que serve `with` em arquivos? **R:** Garantir que o arquivo seja fechado ao sair do bloco.
4. Como definir um argumento padrão em uma função? **R:** `def f(nome="mundo"):` no parâmetro.
5. O que é um decorador em Python? **R:** Função que recebe outra função e altera ou estende seu comportamento.

---

## Materiais de apoio

- Documentação oficial Python: [docs.python.org](https://docs.python.org)  
- Tutorial Python (oficial): seção sobre estruturas de dados e controle de fluxo.
