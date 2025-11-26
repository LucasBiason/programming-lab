# Programming Laboratory - Structure Guide

This document explains the organization structure of the Programming Laboratory repository.

## Philosophy

This repository serves as a **temporary learning space** where projects are organized by technology and purpose. Projects remain here until they:

1. **Mature** - Become production-ready or reference implementations
2. **Get Promoted** - Move to specialized knowledge bases
3. **Get Archived** - No longer relevant or superseded

## Directory Structure

### `/python/`
Python-related projects organized by category.

**Subdirectories:**
- `frameworks/` - Web frameworks (Django, Flask, Streamlit)
- `patterns/` - Design patterns and architectural patterns
- `testing/` - Testing methodologies (TDD, test doubles)
- `tools/` - Development tools and environment setup

**Examples:**
- Django REST API projects
- Flask web applications
- Streamlit dashboards
- Design pattern implementations
- TDD practice projects

### `/nodejs/`
Node.js and JavaScript ecosystem projects.

**Subdirectories:**
- `fundamentals/` - Basic Node.js concepts and tutorials
- `typescript/` - TypeScript projects and examples
- `graphql/` - GraphQL implementations
- `react/` - React projects and hooks
- `orm/` - ORM examples (TypeORM, etc.)
- `infrastructure/` - DevOps and infrastructure (Docker, Kafka, Redis)

**Examples:**
- REST API implementations
- TypeScript setups
- GraphQL servers
- React applications
- Docker configurations
- Message queue implementations

### `/ai-ml/`
Artificial Intelligence and Machine Learning experiments.

**Subdirectories:**
- `tools/` - AI tool integrations (chatbots, OCR, LangChain)
- `algorithms/` - Algorithm implementations (genetic algorithms, etc.)
- `formations/` - Course materials and educational content

**Examples:**
- OpenAI integrations
- LangChain experiments
- Dashboard projects
- Algorithm implementations
- Course notebooks

### `/architecture/`
Architecture patterns and advanced concepts.

**Subdirectories:**
- `cqrs-events/` - CQRS and Event Sourcing implementations

**Examples:**
- CQRS pattern implementations
- Event-driven architectures
- Distributed system patterns

### `/docs/`
Documentation and reference materials.

**Subdirectories:**
- `catalog/` - Project catalogs and inventories
- `migration/` - Migration notes and plans

## Project Organization

Each project should follow this structure:

```
project-name/
├── README.md           # Project description, source, how to run
├── requirements.txt    # Python dependencies (if applicable)
├── package.json       # Node.js dependencies (if applicable)
├── src/               # Source code
├── tests/             # Test files
└── docs/              # Project-specific documentation
```

## Naming Conventions

- **Directories**: lowercase-with-hyphens
- **Projects**: Keep original names when possible
- **Files**: Follow language conventions (Python: snake_case, Node.js: camelCase)

## Migration Path

Projects can be promoted to knowledge bases when they:

1. Have complete documentation
2. Are production-ready or reference implementations
3. Cover a topic comprehensively
4. Are no longer experimental

**Promotion destinations:**
- `ia-ml-knowledge-base` - Mature AI/ML projects
- `microservices-knowledge-base` - Architecture patterns
- Future knowledge bases as they are created

## Maintenance

- Review projects quarterly
- Archive or promote mature projects
- Keep experimental projects organized
- Update documentation regularly

---

**Last Updated**: 2025-11-26

