# Tokens

**Seção:** Aprofundando na IA e LLM  
**Aula:** Tokens  
**Data da aula:** 12/02/2026 (17:54–18:10)  
**Material:** Fundamentos de IA Generativa (PDF p.63–65)  
**Fonte:** Transcrição da videoaula (Attention and Transformers)

---

## Resumo executivo

- **Token** é a unidade de processamento em modelos de linguagem: representação **vetorizada/numérica** de um fragmento de texto (palavra, subpalavra ou pontuação). Tudo que é falado ou escrito vira cálculo e vetor para o modelo.
- No contexto de **Transformers**, cada token de entrada é comparado com **todos os outros** da sequência para calcular **pesos de atenção**; o modelo foca em diferentes partes do texto com peso diferente conforme o contexto.
- **Auto-atenção (self-attention):** o mecanismo calcula a importância relativa de cada token na sequência para compor a representação de um token; palavras distantes podem ter peso alto se a relação for forte (ex.: “O livro que o João **leu**” — “leu” conecta-se a “livro” e “João”).
- **Positional encoding:** como os Transformers não processam em sequência (como RNN), é preciso atribuir uma **posição** a cada token (um “número na fila”) para preservar a ordem; a codificação é adicionada aos embeddings.
- **Arquitetura Transformer:** (1) camada de auto-atenção; (2) camadas feedforward (MLP) por token (não linearidade, processamento em paralelo); (3) positional encoding. Elimina a necessidade de RNNs e permite processamento paralelo e captura de dependências longas.

---

## Conceitos-chave (flashcards)

- **P: O que é um token em modelos de linguagem?**  
  R: Representação vetorizada ou numérica de um fragmento de texto (palavra, subpalavra, pontuação); é a unidade que o modelo processa.

- **P: Por que “não é bem uma palavra”?**  
  R: Token pode ser subpalavra ou símbolo; o importante é que tudo vira vetor/cálculo para o modelo.

- **P: O que a auto-atenção faz com os tokens?**  
  R: Compara cada token com todos os outros da sequência e calcula a importância relativa (pesos) de cada um para formar a representação daquele token.

- **P: Para que serve o positional encoding?**  
  R: Como o Transformer processa tokens em paralelo (não em sequência), é preciso informar a posição de cada token na frase para manter a ordem.

- **P: Exemplo “O cachorro que o menino viu estava latindo”?**  
  R: Para “latindo”, o modelo dá mais peso a “cachorro” (quem late), não a “menino”, mesmo que “menino” esteja mais próximo na frase — conexão por força semântica.

---

## Mapa conceitual

```
Tokens
├── Definição: unidade vetorizada (palavra/subpalavra/pontuação)
├── No Transformer
│   ├── Auto-atenção: cada token comparado a todos, pesos de importância
│   ├── Feedforward (MLP) por token, processamento paralelo
│   └── Positional encoding: posição na sequência
├── Benefícios
│   ├── Processamento paralelo (sem RNN)
│   └── Dependências longas sem degradação do gradiente
└── Base para BERT, GPT, T5, LLaMA, etc.
```

---

## Receita prática

1. **Entender token** como a unidade de entrada/saída em LLMs: texto é tokenizado antes de virar embeddings.
2. **Auto-atenção:** para cada posição, calcular scores com todas as posições e usar como pesos para combinar representações.
3. **Positional encoding:** somar vetor de posição aos embeddings para preservar ordem.
4. **Reuso:** modelos pré-treinados já fazem tokenização + embeddings + atenção; usar para sua tarefa.

---

## Perguntas de reforço

1. Token é sempre uma palavra? Não; pode ser subpalavra ou símbolo; o essencial é a representação numérica.
2. Por que positional encoding no Transformer? Porque não há processamento sequencial; a ordem precisa ser injetada de outra forma.
3. Quem “conecta” livro, João e leu na frase “O livro que o João leu era interessante”? O mecanismo de atenção atribui peso alto a esses tokens para compor a representação.
4. O Transformer substitui RNN como? Processando todos os tokens em paralelo e usando atenção para dependências à distância.
5. O que é “peso” na atenção? A importância relativa de um token em relação aos outros para formar a representação de um dado token.
