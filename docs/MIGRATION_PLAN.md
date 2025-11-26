# Migration Plan - Legacy Repositories to Programming Lab

This document outlines the plan to migrate projects from 4 legacy repositories into the unified Programming Laboratory.

## Repositories to Migrate

1. **IA-Studies** → `ai-ml/` and related folders
2. **Python-Studies** → `python/` and subfolders
3. **Nodejs-Studies** → `nodejs/` and subfolders
4. **CQRS-Events-in-Node.js** → `architecture/cqrs-events/`

## Migration Strategy

### Phase 1: Catalog and Organize
- [x] Create complete catalog of all projects
- [x] Define new repository structure
- [x] Create migration plan
- [ ] Review each project for relevance

### Phase 2: Structure Setup
- [x] Create folder structure
- [x] Create README and documentation
- [x] Setup .gitignore
- [ ] Initialize git repository

### Phase 3: Migration Execution
- [ ] Migrate Python projects
- [ ] Migrate Node.js projects
- [ ] Migrate AI/ML projects
- [ ] Migrate architecture projects
- [ ] Update all READMEs and documentation

### Phase 4: Cleanup
- [ ] Archive legacy repositories
- [ ] Update references in other projects
- [ ] Final documentation review

## Mapping Details

### IA-Studies → programming-lab/ai-ml/

| Source | Destination | Notes |
|--------|-------------|-------|
| `Estudos de Ferramentas/` | `ai-ml/tools/` | Organize by tool type |
| `Formação IA e ML/` | `ai-ml/formations/` | Course materials |
| `POS FIAP IA para Devs/` | `ai-ml/formations/fiap/` | FIAP specific |
| `Projetos Construidos/` | `ai-ml/projects/` | Mature projects |

### Python-Studies → programming-lab/python/

| Source | Destination | Notes |
|--------|-------------|-------|
| `Python/DesignerPatterns/` | `python/patterns/design-patterns/` | Design patterns |
| `Django/` | `python/frameworks/django/` | All Django projects |
| `Flask/` | `python/frameworks/flask/` | All Flask projects |
| `Streamlit/` | `python/frameworks/streamlit/` | All Streamlit projects |
| `Tests/` | `python/testing/` | Testing projects |

### Nodejs-Studies → programming-lab/nodejs/

| Source | Destination | Notes |
|--------|-------------|-------|
| `nodejs-*` (fundamentals) | `nodejs/fundamentals/` | Basic Node.js |
| `typescript-*` | `nodejs/typescript/` | TypeScript projects |
| `graphql-*` | `nodejs/graphql/` | GraphQL projects |
| `react-*` | `nodejs/react/` | React projects |
| `nodejs-crud-typeorm/` | `nodejs/orm/` | ORM examples |
| `nodejs-docker/` | `nodejs/infrastructure/docker/` | Docker setup |
| `node-kafka-poc/` | `nodejs/infrastructure/kafka/` | Kafka POC |
| `cache-redis/` | `nodejs/infrastructure/redis/` | Redis cache |

### CQRS-Events-in-Node.js → programming-lab/architecture/cqrs-events/

| Source | Destination | Notes |
|--------|-------------|-------|
| Entire project | `architecture/cqrs-events/` | Complete CQRS implementation |

## File Naming Conventions

- Keep original project names when possible
- Add README.md to each migrated project
- Include source information (course, tutorial, etc.)
- Maintain original structure within each project

## Documentation Requirements

Each migrated project should have:
- README.md with description
- Source information (course link, tutorial, etc.)
- Technologies used
- How to run/use
- Learning objectives

## Timeline

- **Week 1**: Complete catalog and structure
- **Week 2**: Migrate Python projects
- **Week 3**: Migrate Node.js projects
- **Week 4**: Migrate AI/ML and architecture projects
- **Week 5**: Final cleanup and documentation

## Notes

- Preserve git history where possible
- Update all internal links
- Maintain original licenses
- Document migration date for each project

---

**Status**: Planning phase
**Last Updated**: 2025-11-26

