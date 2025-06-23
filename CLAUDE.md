# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Python Services (ta-api, ta-cli, ta-core, ta-ml)

**Bulk operations across all Python services:**
```bash
./scripts/poetry_all.sh install          # Install dependencies for all services
./scripts/poe_all.sh lint                # Run MyPy and Flake8 on all services
./scripts/poe_all.sh format              # Run Black and isort on all services
./scripts/poe_all.sh test                # Run pytest on all services (skips if no tests)
```

**Individual service operations:**
```bash
cd ta-api && poetry run poe lint         # MyPy + Flake8 type checking and linting
cd ta-api && poetry run poe format       # Black + isort code formatting
cd ta-api && poetry run poe test         # Run pytest
```

**Running services:**
```bash
# API Server (requires 1Password setup)
cd ta-api && OP_VAULT_NAME="Tend Attend" OP_APP_ENV="Local" op run --env-file app.env -- poetry run uvicorn main:app --reload --port=8000

# ML Service
cd ta-ml && poetry run uvicorn main:app --reload --port=8001
```

### QR Code Service (Node.js)

```bash
cd ta-qrcode
pnpm install          # Install dependencies
pnpm run build        # Compile TypeScript
pnpm start            # Start service
pnpm test             # Run tests with Vitest
pnpm run ci:lint      # Run ESLint and Prettier
```

### Database Operations

```bash
# Start MySQL database
docker compose up

# Run migrations via API
curl -X POST http://localhost:8000/admin/migration/upgrade

# CLI database operations
cd ta-cli
poetry run poe db-migration print-ddl    # Print DDL statements
poetry run poe db-migration migrate      # Reset and migrate to latest schema
poetry run poe db-mock attendance-log    # Generate mock attendance data
```

### Build and Deployment

```bash
./scripts/build_server.sh        # Build server Docker image and create deployment packages
./scripts/deploy.sh <environment> # Deploy to specified environment (requires 1Password)
```

## Architecture Overview

### Microservices Structure

**ta-api**: FastAPI REST API service with authentication, event management, and admin endpoints
**ta-core**: Shared domain logic, database models, and infrastructure using Domain-Driven Design
**ta-cli**: Administrative CLI for database migrations and mock data generation
**ta-ml**: Machine learning service using TimesFM for attendance prediction
**ta-qrcode**: Node.js service for QR code generation using node-canvas

### Domain-Driven Design Architecture

The codebase follows Clean Architecture principles with Domain-Driven Design:

**Domain Layer** (`ta-core/src/ta_core/domain/`):
- **Entities**: Rich domain objects with business logic (UserAccount, Event, EventAttendance)
- **Repository Interfaces**: Abstract repository contracts using generic types
- **Unit of Work**: Transaction boundary management interface
- **Usecases**: Business logic orchestration interfaces

**Infrastructure Layer** (`ta-core/src/ta_core/infrastructure/`):
- **SQLAlchemy Models**: Database models with bidirectional entity conversion
- **Repository Implementations**: Concrete async repository implementations
- **Unit of Work**: SQLAlchemy session management
- **Database Sharding**: Commons, sequences, and shard database separation

**Key Patterns**:
- **Immutable Entity Updates**: Entities return new instances via factory methods
- **Async-First**: All repository and database operations are async
- **DTO Pattern**: Data Transfer Objects for API boundaries
- **Error Handling**: Structured error codes with `@rollbackable` decorator
- **UUID Primary Keys**: Binary UUID storage with conversion utilities

### Database Architecture

**Sharded Database Design**:
- **Commons**: User accounts, verification, shared data
- **Sequences**: ID generation sequences
- **Shards**: Event and attendance data partitioned by user

**Migration System**:
- Alembic-based migrations in `ta-core/src/alembic/`
- CLI tools for schema management and development data

### 1Password Integration

The project uses 1Password CLI for secure credential management:
- Service account authentication for deployment
- Environment variables stored in "Tend Attend" vault
- Automated credential injection during deployment

## Code Quality Standards

**Python Standards** (configured in pyproject.toml):
- **MyPy**: Strict type checking with `ignore_missing_imports = True`
- **Flake8**: Line length 88, extends Black compatibility
- **Black**: Code formatting with 88 character lines
- **isort**: Import sorting with Black profile

**Node.js Standards** (ta-qrcode):
- **ESLint**: Modern configuration
- **Prettier**: Code formatting with import organization
- **TypeScript**: Strict type checking
- **Vitest**: Testing framework

## Development Environment

**Python Version Management**:
- ta-api/ta-cli/ta-core: Python 3.13.3
- ta-ml: Python 3.10.18 (ML library compatibility)
- Use pyenv with `.python-version` files

**Dependencies**:
- Poetry for Python dependency management
- pnpm for Node.js package management
- Docker Compose for local MySQL database

## Common Workflows

**Adding New Features**:
1. Create domain entity/usecase in ta-core if needed
2. Add repository methods with async patterns
3. Implement API endpoints in ta-api
4. Add CLI commands in ta-cli if administrative access needed
5. Run `./scripts/poe_all.sh lint format test` before committing

**Database Changes**:
1. Modify SQLAlchemy models in ta-core
2. Generate migration: `cd ta-core && poetry run alembic revision --autogenerate -m "description"`
3. Review and test migration
4. Update via API: `curl -X POST http://localhost:8000/admin/migration/upgrade`

**Testing New Code**:
- Python: `pytest` individual files or `./scripts/poe_all.sh test` for all
- Node.js: `cd ta-qrcode && pnpm test`
- Always run linting before committing