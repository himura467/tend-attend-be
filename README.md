# Tend Attend (Backend)

Tend Attend is an intuitive event management tool with predictive analytics capabilities. It stands out by offering features that predict attendee status using machine learning, enabling event organizers to leverage this information for effective management.

## 🏗️ Architecture

This is a microservices-based backend system consisting of the following components:

### Core Components

- **ta-api** - FastAPI-based component defining REST API routes and endpoints
- **ta-core** - Shared core component containing domain models, database infrastructure, and business logic
- **ta-cli** - Command-line interface for database migrations and administrative tasks
- **ta-ml** - Machine learning service using TimesFM for attendee prediction and forecasting
- **ta-qrcode** - Node.js/TypeScript service for QR code generation and management

### Infrastructure

- **docker** - Containerization platform with MySQL database setup and Dockerfiles for server, ML server, and QR code server deployment
- **terraform** - Infrastructure as Code for multi-cloud deployment (AWS + Google Cloud)
- **scripts** - Build, deployment, and developer utility commands

## 🚀 Features

- **Database Sharding** - Scalable database architecture with automated migrations
- **User Authentication** - Secure auth system with JWT tokens
- **Email Verification** - Automated email verification system
- **Event Management** - Create, update, and manage events with attendee tracking
- **Predictive Analytics** - ML-powered attendee status prediction using TimesFM
- **QR Code Generation** - Automated QR code creation for event check-ins

## 🛠️ Technology Stack

### Backend Services

- **Python 3.13.3** (ta-api, ta-core, ta-cli)
- **Python 3.10.18** (ta-ml for ML compatibility)
- **FastAPI** - Modern web framework for APIs
- **SQLAlchemy** - ORM with async support
- **Alembic** - Database migration management
- **Typer** - CLI framework

### Machine Learning

- **PyTorch** - Deep learning framework
- **JAX** - High-performance ML computations
- **TimesFM** - Time series forecasting model
- **Statsmodels** - Statistical analysis

### QR Code Service

- **Node.js** with **TypeScript**
- **node-canvas** - Server-side rendering
- **qr-code-styling** - Custom QR code generation

### Database & Infrastructure

- **MySQL 8.4** - Primary database (local development)
- **AWS CloudFront** - CDN
- **AWS Lambda** - Serverless API functions
- **AWS Aurora** - Production database
- **Google Cloud Run** - ML service deployment

## 📋 Prerequisites

- **Python** - Versions specified in `.python-version` files
- **pyenv** - Python version management
- **Poetry** - Python dependency management
- **Node.js** - Version specified in `.node-version`
- **pnpm** - Node.js package manager
- **Docker & Docker Compose** - For local development
- **1Password CLI** - For environment variable management (`op` command)
- **AWS CLI** - For AWS deployment (optional)
- **Google Cloud CLI** - For Google Cloud deployment (optional)
- **Terraform** - For infrastructure deployment (optional)

## 🚀 Local Setup

### 1. Python Environment Setup

Install required Python versions using pyenv:

```bash
pyenv install `cat ta-api/.python-version` && pyenv install `cat ta-ml/.python-version`
```

### 2. Install Dependencies

Install all Python dependencies:

```bash
./scripts/poetry_all.sh install
```

Install Node.js dependencies for QR code service:

```bash
cd ta-qrcode && pnpm install
```

### 3. Environment Variables Setup

The application uses 1Password for secure environment variable management. Ensure you have:

1. **1Password CLI installed** and authenticated
2. **Proper vault access** configured
3. **Environment variables** set up in your 1Password vault

### 4. Start Services

Start the main API server with environment variables:

```bash
cd ta-api && OP_VAULT_NAME="Tend Attend" OP_APP_ENV="Local" op run --env-file app.env -- poetry run uvicorn main:app --reload --port=8000
```

Start the ML service:

```bash
cd ta-ml && poetry run uvicorn main:app --reload --port=8001
```

Start the QR code service:

```bash
cd ta-qrcode
pnpm run build
pnpm start
```

### 5. Database Setup

Start the MySQL database with Docker Compose:

```bash
docker compose up
```

Run database migrations by calling the API endpoint:

```bash
curl -X POST http://localhost:8000/admin/migration/upgrade
```

## 🧪 Development

### Code Quality Tools

Each Python component includes:

- **MyPy** - Static type checking
- **Flake8** - Code linting
- **Black** - Code formatting
- **isort** - Import sorting
- **pytest** - Testing framework

Run linting and formatting:

```bash
./scripts/poe_all.sh lint    # Run MyPy and Flake8
./scripts/poe_all.sh format  # Run Black and isort
./scripts/poe_all.sh test    # Run tests
```

### CLI Commands

```bash
cd ta-cli
# Print DDL statements for database schema generation
poetry run poe db-migration print-ddl
# Run database migrations and reset database to latest schema
poetry run poe db-migration migrate
# Generate mock attendance log data for development and testing
poetry run poe db-mock attendance-log
```

**Command Descriptions:**

- `db-migration print-ddl` - Generates and prints DDL (Data Definition Language) statements for the database schema
- `db-migration migrate` - Resets the database and applies all migrations to bring it to the latest schema version
- `db-mock attendance-log` - Creates mock user attendance sequence data for development and testing purposes

## 🌐 API Endpoints

The ta-api service provides the following endpoint groups:

- `/accounts` - User account management
- `/admin` - Administrative functions
- `/auth` - Authentication and authorization
- `/events` - Event CRUD operations
- `/verify` - Email verification
- `/healthz` - Health check endpoint

## 🚀 Deployment

The project uses a multi-cloud architecture with both AWS and Google Cloud Platform:

- **AWS**: Hosts the main API (Lambda), QR code generation service (Lambda), database (Aurora), and CDN (CloudFront)
- **Google Cloud**: Hosts the ML service (Cloud Run)

### Build and Deployment Scripts

Use the provided scripts for building and deployment:

```bash
./scripts/build.sh  # Build all components
./scripts/deploy.sh <aws-profile> <gcloud-config-name> <environment>
```

The deployment script handles the complete deployment process including:

- Terraform backend preparation
- Infrastructure provisioning with `terraform init`, `terraform plan`, and `terraform apply`
- Both AWS and Google Cloud resources deployment

**Initial Setup (One-time):**

Prepare Terraform backend before first deployment:

```bash
cd terraform/environments/prod
# Run the commands in README.md to set up S3 backend
```

**Example Deployment:**

```bash
./scripts/deploy.sh default my-gcp-config prod
```

## 📁 Project Structure

```
tend-attend-be/
├── ta-api/      # FastAPI REST API service
├── ta-cli/      # CLI tools and migrations
├── ta-core/     # Shared core library
├── ta-ml/       # Machine learning service
├── ta-qrcode/   # QR code generation service
├── docker/      # Docker configurations
├── terraform/   # Infrastructure as Code
├── scripts/     # Build and deployment scripts
└── compose.yml  # Docker Compose configuration
```

## 🤝 Contributing

1. Follow the established code style (Black, isort)
2. Run linting and tests before submitting PRs
3. Update documentation for new features
4. Use conventional commit messages

## 📝 License

This project is licensed under the terms specified in the LICENSE file.

## 👨‍💻 Author

**himura467** - mitarashidango0927@gmail.com
