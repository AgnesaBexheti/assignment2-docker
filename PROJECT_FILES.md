# Project Files Overview

## Complete File Structure

```
assignment2-docker/
│
├── catalog-service/                 # Catalog Service (Python/Flask + PostgreSQL)
│   ├── app.py                      # Main Flask application with CRUD operations
│   ├── Dockerfile                  # Container configuration for Catalog Service
│   └── requirements.txt            # Python dependencies (Flask, psycopg2)
│
├── user-service/                    # User Service (Python/Flask + MySQL)
│   ├── app.py                      # Main Flask application with CRUD operations
│   ├── Dockerfile                  # Container configuration for User Service
│   └── requirements.txt            # Python dependencies (Flask, mysql-connector)
│
├── order-service/                   # Order Service (PHP + MySQL)
│   ├── index.php                   # Main PHP application with CRUD operations
│   ├── .htaccess                   # Apache URL rewriting configuration
│   └── Dockerfile                  # Container configuration for Order Service
│
├── docker-compose.yml              # Docker Compose orchestration file
├── .gitignore                      # Git ignore patterns
│
├── README.md                       # Main project documentation
├── ASSIGNMENT_SUMMARY.md           # Assignment completion summary
├── ARCHITECTURE.md                 # System architecture diagrams
├── TESTING_GUIDE.md                # Comprehensive testing instructions
├── PROJECT_FILES.md                # This file - project structure overview
└── test-services.sh                # Automated testing script
```

---

## File Descriptions

### Service Implementation Files

#### catalog-service/app.py (238 lines)
**Purpose:** Catalog Service implementation
- Flask web application
- PostgreSQL database connection
- Full CRUD operations for books
- Automatic database initialization
- Sample data seeding
- RESTful API endpoints

**Key Features:**
- Environment variable configuration
- Connection pooling
- Error handling
- JSON responses
- Database schema creation

#### user-service/app.py (241 lines)
**Purpose:** User Service implementation
- Flask web application
- MySQL database connection
- Full CRUD operations for users
- Automatic database initialization
- Sample data seeding
- RESTful API endpoints

**Key Features:**
- MySQL connector usage
- Dictionary cursor for JSON conversion
- Dynamic query building
- Timestamp handling

#### order-service/index.php (343 lines)
**Purpose:** Order Service implementation
- Native PHP application
- PDO MySQL connection
- Full CRUD operations for orders
- Automatic database and table creation
- Sample data seeding
- RESTful API routing

**Key Features:**
- URL routing without framework
- PDO prepared statements
- Dynamic query building
- JSON response formatting
- Database initialization on startup

---

### Docker Configuration Files

#### catalog-service/Dockerfile
**Purpose:** Build container for Catalog Service
```dockerfile
- Base: python:3.11-slim
- System deps: gcc, postgresql-client
- Python deps: Flask, psycopg2-binary
- Port: 5000
```

#### user-service/Dockerfile
**Purpose:** Build container for User Service
```dockerfile
- Base: python:3.11-slim
- System deps: gcc, libmysqlclient-dev
- Python deps: Flask, mysql-connector-python
- Port: 5001
```

#### order-service/Dockerfile
**Purpose:** Build container for Order Service
```dockerfile
- Base: php:8.2-apache
- Extensions: PDO, PDO MySQL
- Mods: mod_rewrite, PHP handler
- Port: 80
```

#### docker-compose.yml
**Purpose:** Orchestrate all services and databases
- 6 services (3 apps + 3 databases)
- Network configuration (library-net)
- Volume management
- Environment variables
- Health checks
- Port mappings
- Dependencies

---

### Dependency Files

#### catalog-service/requirements.txt
```
Flask==3.0.0
psycopg2-binary==2.9.9
```

#### user-service/requirements.txt
```
Flask==3.0.0
mysql-connector-python==8.2.0
```

#### order-service/.htaccess
```apache
DirectoryIndex index.php
URL rewriting rules
```

---

### Documentation Files

#### README.md (350+ lines)
**Purpose:** Main project documentation
- Architecture overview
- Quick start guide
- Docker Compose instructions
- Manual deployment commands
- API endpoint documentation
- Testing examples
- Troubleshooting guide

#### ASSIGNMENT_SUMMARY.md (350+ lines)
**Purpose:** Assignment completion summary
- Project overview
- Architecture details
- Implementation summary
- Testing results
- Technology stack
- Features checklist

#### ARCHITECTURE.md (280+ lines)
**Purpose:** System architecture documentation
- ASCII architecture diagrams
- Data models
- Request flow examples
- Technology stack visualization
- Container dependencies
- Port mappings
- Volume persistence

#### TESTING_GUIDE.md (450+ lines)
**Purpose:** Comprehensive testing guide
- Quick start testing
- READ operations (required)
- CREATE operations
- UPDATE operations
- DELETE operations
- Postman collection
- Database verification
- Error testing
- Troubleshooting

#### PROJECT_FILES.md (this file)
**Purpose:** File structure overview
- Complete file listing
- File descriptions
- Code statistics
- Line counts

---

### Utility Files

#### test-services.sh
**Purpose:** Automated testing script
- Tests all three services
- Health checks
- READ operations
- Formatted output

#### .gitignore
**Purpose:** Git ignore patterns
- Python cache files
- Virtual environments
- IDE files
- OS files
- Log files

---

## Code Statistics

### Total Files by Type

| Type       | Count | Files                                    |
|------------|-------|------------------------------------------|
| Python     | 2     | catalog-service/app.py, user-service/app.py |
| PHP        | 1     | order-service/index.php                  |
| Dockerfile | 3     | One per service                          |
| Config     | 3     | docker-compose.yml, .htaccess, .gitignore |
| Docs       | 5     | README, SUMMARY, ARCHITECTURE, TESTING, FILES |
| Scripts    | 1     | test-services.sh                         |
| Deps       | 2     | requirements.txt (×2)                    |

**Total:** 17 files

### Lines of Code

| File                      | Lines | Language   |
|---------------------------|-------|------------|
| catalog-service/app.py    | 238   | Python     |
| user-service/app.py       | 241   | Python     |
| order-service/index.php   | 343   | PHP        |
| docker-compose.yml        | 95    | YAML       |
| catalog-service/Dockerfile| 29    | Dockerfile |
| user-service/Dockerfile   | 31    | Dockerfile |
| order-service/Dockerfile  | 38    | Dockerfile |

**Total Application Code:** ~1,015 lines

---

## Documentation Statistics

| File                  | Lines | Purpose           |
|-----------------------|-------|-------------------|
| README.md            | 350+  | Main docs         |
| ASSIGNMENT_SUMMARY.md | 350+  | Summary report    |
| ARCHITECTURE.md      | 280+  | Architecture      |
| TESTING_GUIDE.md     | 450+  | Testing guide     |
| PROJECT_FILES.md     | 200+  | This file         |

**Total Documentation:** ~1,630 lines

---

## Key Technologies Used

### Programming Languages
- **Python 3.11** - Catalog and User services
- **PHP 8.2** - Order service

### Frameworks
- **Flask 3.0** - Python web framework
- **Apache 2.4** - PHP web server

### Databases
- **PostgreSQL 15** - Catalog database
- **MySQL 8.0** - User and Order databases

### Database Drivers
- **psycopg2** - PostgreSQL adapter for Python
- **mysql-connector-python** - MySQL adapter for Python
- **PDO** - PHP Data Objects for MySQL

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Container orchestration

---

## Project Metrics

### Services
- **Total Services:** 3 microservices
- **Total Databases:** 3 independent databases
- **Total Containers:** 6 Docker containers
- **Total Volumes:** 3 persistent volumes
- **Total Ports:** 3 exposed ports (5000, 5001, 8080)

### API Endpoints
- **Catalog Service:** 5 endpoints (1 health + 4 CRUD)
- **User Service:** 5 endpoints (1 health + 4 CRUD)
- **Order Service:** 5 endpoints (1 health + 4 CRUD)
- **Total Endpoints:** 15 endpoints

### Database Tables
- **Books table:** 7 fields
- **Users table:** 7 fields
- **Orders table:** 7 fields

### Sample Data
- **Books:** 5 pre-loaded records
- **Users:** 5 pre-loaded records
- **Orders:** 5 pre-loaded records
- **Total Records:** 15 sample records

---

## Build Information

### Docker Images Built
1. `assignment2-docker-catalog-service`
2. `assignment2-docker-user-service`
3. `assignment2-docker-order-service`

### Docker Images Used
1. `postgres:15-alpine`
2. `mysql:8.0` (×2)
3. `python:3.11-slim` (×2)
4. `php:8.2-apache`

---

## Assignment Requirements Checklist

### ✅ Core Requirements
- [x] 3 microservices implemented
- [x] Each service has its own database
- [x] Different technologies used (Python, PHP)
- [x] Different databases used (PostgreSQL, MySQL)
- [x] Dockerfile for each service
- [x] Docker Compose configuration
- [x] Independent database instances
- [x] Unique database credentials
- [x] Docker volumes for persistence
- [x] Custom network (library-net)

### ✅ Functionality
- [x] READ operations implemented (all services)
- [x] CREATE operations implemented (all services)
- [x] UPDATE operations implemented (all services)
- [x] DELETE operations implemented (all services)
- [x] Environment variable configuration
- [x] Sample data seeding

### ✅ Documentation
- [x] README with instructions
- [x] API endpoint documentation
- [x] Testing guide
- [x] Architecture documentation
- [x] Manual deployment commands
- [x] Docker Compose commands

### ✅ Testing
- [x] All services tested and working
- [x] READ operations verified
- [x] Database connectivity confirmed
- [x] Health checks functioning
- [x] Sample data accessible

---

## Usage Instructions

### Quick Start
```bash
# Clone and navigate to project
cd assignment2-docker

# Start all services
docker-compose up -d --build

# Verify everything is running
docker-compose ps

# Test the services
curl http://localhost:5000/catalog
curl http://localhost:5001/users
curl http://localhost:8080/orders

# Stop services
docker-compose down
```

### For Detailed Instructions
- See [README.md](README.md) for comprehensive setup guide
- See [TESTING_GUIDE.md](TESTING_GUIDE.md) for testing instructions
- See [ARCHITECTURE.md](ARCHITECTURE.md) for system design details

---

## License & Academic Integrity

This project is an academic assignment for educational purposes.

**Date Completed:** December 17, 2025
**Assignment:** Implementing Microservices with Docker and Independent Databases
