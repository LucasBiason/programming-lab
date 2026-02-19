# GANs

**Seção:** Aprofundando na IA e LLM  
**Aula:** GANs (Generative Adversarial Networks)  
**Data da aula:** 12/02/2026 (18:47–19:32)  
**Material:** Fundamentos de IA Generativa (PDF p.68)  
**Fonte:** Transcrição da videoaula

---

## Resumo executivo

- **GANs** surgem para **geração de imagens** (e outros domínios visuais/sonoros). Diferente do LLM (pensado para linguagem natural), a coesão aqui é **de imagem**, não textual — não há “próxima palavra da esquerda para a direita”; por isso outra estratégia é necessária.
- **Contexto (~2014):** geração de imagens era rudimentar, baixa qualidade, aparência artificial; GANs permitiram imagens mais realistas e de alta qualidade, abrindo caminho para IA em arte, moda, jogos e design.
- **Funcionamento:** dois componentes em jogo. **Gerador:** tenta gerar amostras “falsas” (ex.: imagens de notas de R$ 10). **Discriminador:** tenta classificar se a amostra é real ou falsa. O gerador recebe feedback do discriminador e vai se afinando até produzir saídas cada vez mais realistas; os dois melhoram em conjunto.
- **Analogia:** gerador = falsificador; discriminador = policial. Gerador gera falsa, real, falsa…; discriminador diz “falso”, “real”, “falso”. Com o tempo o gerador aprende o que é real e o que é falso e produz notas (ou rostos, roupas, etc.) mais realistas.
- **VAE (Variational Autoencoder):** complementar aos GANs. **Encoder** comprime os dados; **decoder** reconstrói/gera. Permite **controlar** o que se gera (ex.: “homem sorrindo, cabelo curto, bigode”) manipulando variáveis latentes. Mais estável matematicamente e controlado que GANs; melhor para geração muito específica. Também evoluiu geração de voz/som.

---

## Conceitos-chave (flashcards)

- **P: Por que GAN e não LLM para imagem?**  
  R: LLM foi pensado para linguagem (sequência de palavras, coesão textual); imagem tem outra coesão (espacial, não “esquerda–direita”); GAN foi desenhado para geração visual.

- **P: Quem são os dois “personagens” do GAN?**  
  R: Gerador (produz amostras “falsas”) e discriminador (diz se é real ou falso); um melhora o outro.

- **P: Como o gerador melhora?**  
  R: Recebendo feedback do discriminador; ao longo do tempo entende o que parece real e ajusta a geração.

- **P: O que é VAE?**  
  R: Variational Autoencoder: encoder comprime, decoder reconstrói/gera; permite controlar a saída via variáveis latentes (ex.: atributos do rosto).

- **P: GAN vs VAE?**  
  R: GAN: mais flexível para realismo; treino instável. VAE: mais estável e controlado; melhor para especificidade (detalhes da geração).

- **P: Aplicações dos GANs?**  
  R: Arte, moda, jogos, design, geração de rostos e imagens realistas; VAE também em voz/som.

---

## Mapa conceitual

```
GANs
├── Contexto: geração de imagem (~2014), antes rudimentar
├── Dois componentes
│   ├── Gerador: produz amostras “falsas”
│   └── Discriminador: classifica real vs falso
├── Dinâmica: gerador melhora com feedback do discriminador
├── Aplicações: arte, moda, jogos, design, rostos
└── VAE (complementar)
    ├── Encoder + Decoder
    ├── Controle via variáveis latentes
    ├── Mais estável e controlado
    └── Voz/som também
```

---

## Receita prática

1. **Usar GAN** quando o foco é geração de imagem (ou domínio similar) realista e não há necessidade de controle fino por atributos.
2. **Usar VAE** quando precisar **controlar** a saída (ex.: “homem sorrindo, cabelo curto, bigode”) ou quando quiser mais estabilidade no treino.
3. **Treino GAN:** alternar atualizações do gerador e do discriminador; monitorar equilíbrio para evitar um “ganhar” demais.
4. **Aplicações:** arte generativa, data augmentation, super-resolução, geração de rostos; VAE para geração condicionada e voz.

---

## Perguntas de reforço

1. O gerador e o discriminador treinam juntos? Sim; um produz, o outro classifica; o feedback melhora o gerador.
2. GAN resolve “próxima palavra” como LLM? Não; GAN é para geração de imagem (e similares), não para sequência de texto.
3. O que são “variáveis latentes” no VAE? Representação comprimida que o encoder aprende; ao manipular essas variáveis no decoder, controla-se o que é gerado.
4. Por que VAE é “mais estável” que GAN? Modelo probabilístico com encoder/decoder; treino menos adversarial, mais controlado.
5. Onde VAE ajudou além de imagem? Evolução da geração de voz/som, deixando mais realista.
