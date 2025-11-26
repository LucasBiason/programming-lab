# Programming Laboratory

A comprehensive laboratory for tracking courses, tutorials, experiments, videos, classes, and learning projects across various technology areas.

## Purpose

This repository serves as a **learning laboratory** where experimental projects, tutorials, and study materials are organized. When concepts mature, they either become standalone projects or are moved to specialized knowledge bases:

- **IA/ML projects** → `ia-ml-knowledge-base`
- **Architecture patterns** → `microservices-knowledge-base`
- **Other specialized topics** → respective knowledge bases

## Structure

```
programming-lab/
├── python/              # Python projects and tutorials
│   ├── frameworks/      # Django, Flask, Streamlit
│   │   ├── django/      # Django REST, JWT auth, CI/CD
│   │   ├── flask/       # Flask web apps, REST APIs
│   │   └── streamlit/   # Streamlit dashboards
│   ├── patterns/        # Design patterns
│   │   └── design-patterns/  # Design Patterns Python I & II
│   ├── testing/         # TDD, test doubles
│   │   ├── tdd/         # Test-Driven Development
│   │   └── test-doubles/ # Test doubles and mocks
│   ├── tools/           # Development tools
│   │   └── environments/ # Virtual environments (pipenv, Docker, ASDF)
│   └── api-integrations/ # API integrations
│       └── APIBancoCentral/
├── nodejs/              # Node.js projects and tutorials
│   ├── fundamentals/    # Basic Node.js, REST APIs
│   ├── typescript/      # TypeScript projects and setup
│   ├── graphql/         # GraphQL implementations
│   ├── react/           # React projects and hooks
│   ├── nextjs/          # Next.js projects
│   ├── orm/             # ORM examples (TypeORM)
│   └── infrastructure/  # Docker, Kafka, Redis, uploads
├── ai-ml/               # AI/ML experiments
│   ├── tools/           # AI tools and integrations
│   │   ├── chatbots/    # OpenAI chatbots
│   │   ├── dashboards/  # AI-powered dashboards
│   │   ├── ocr/         # Optical Character Recognition
│   │   ├── langchain/   # LangChain experiments
│   │   ├── audio/       # Audio generation
│   │   └── ml-basics/   # Basic ML projects
│   ├── algorithms/      # Algorithm implementations
│   │   └── genetic-algorithms/
│   ├── formations/      # Course materials
│   │   ├── fiap/        # POS FIAP IA para Devs
│   │   └── alura/       # Alura formations
│   └── projects/        # Mature projects
│       └── Projetos Construidos/  # Imobiliaria, NoMoreSpams, Telegram
├── architecture/        # Architecture patterns
│   └── cqrs-events/     # CQRS and event sourcing (complete implementation)
└── docs/                # Documentation
    ├── catalog/         # Project catalog
    └── migration/       # Migration notes
```

## Statistics

- **Total Projects**: ~36+ projects migrated
- **Python Projects**: 18+ projects
- **Node.js Projects**: 15+ projects
- **AI/ML Projects**: 11+ projects
- **Architecture Projects**: 1 complex project (CQRS)

## Quick Navigation

- [Python Projects](./python/README.md)
- [Node.js Projects](./nodejs/README.md)
- [AI/ML Projects](./ai-ml/README.md)
- [Architecture Patterns](./architecture/README.md)
- [Complete Catalog](./docs/catalog/CATALOGO_PROJETOS.md)

## Categories

### Learning Projects
Projects created while following courses, tutorials, or learning new concepts.

### Experiments
Proof of concepts, tests, and experimental code.

### Tutorials
Step-by-step implementations from tutorials and courses.

### Study Materials
Notes, notebooks, and learning resources.

## Migration from Legacy Repositories

This repository consolidates content from:
- `IA-Studies` - AI/ML projects and experiments
- `Python-Studies` - Python courses and projects
- `Nodejs-Studies` - Node.js tutorials and examples
- `CQRS-Events-in-Node.js` - Architecture pattern implementation

See `docs/catalog/` for complete project catalog.

## Organization Principles

1. **By Technology**: Projects organized by programming language/framework
2. **By Purpose**: Learning, experimentation, or reference
3. **Temporary Nature**: Projects remain here until they mature
4. **Migration Path**: Clear path to knowledge bases when ready

## Contributing

This is a personal learning laboratory. Projects are organized for:
- Easy reference during learning
- Tracking progress
- Building knowledge systematically
- Preparing content for knowledge bases

## License

MIT License - See LICENSE file for details

## Author

Lucas Biason - [GitHub](https://github.com/LucasBiason)

---

**Note**: This repository is under active organization. Structure may change as projects are migrated and organized.

