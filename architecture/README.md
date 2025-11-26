# Architecture Patterns

This directory contains advanced architecture pattern implementations.

## Structure

```
architecture/
└── cqrs-events/      # CQRS and Event Sourcing
```

## Projects

### CQRS Events

**CQRS Events Lab**: Shopping cart simulation using CQRS architecture pattern.

- **Source**: Based on [CQRS: What? Why? How?](https://sderosiaux.medium.com/cqrs-what-why-how-945543482313)
- **Technologies**:
  - Node.js (Write System, Read System)
  - Python/Django (Alternative Read System)
  - PostgreSQL (multiple databases)
  - Docker Compose
  - gRPC Adapter
  - Event Sourcing

- **Structure**:
  - `src/` - Main version
  - `src2.0/` - Version 2.0
  - `src3.0/` - Version 3.0
  - `grpc-adapter/` - gRPC adapter
  - `mocks/` - Test mocks

- **Features**:
  - Write service for cart commands
  - Read services (Node.js and Python)
  - Event-driven architecture
  - Multiple database support
  - Performance benchmarks

## Notes

This is a complex, production-ready architecture pattern implementation. When fully documented, it may be moved to `microservices-knowledge-base`.

