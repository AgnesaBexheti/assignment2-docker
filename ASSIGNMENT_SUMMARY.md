# Assignment #2 - Implementation Summary

## Online Library System - Microservices with Docker

### Student Information
**Assignment:** Implementing Microservices with Docker and Independent Databases
**Completion Date:** December 17, 2025

---

## Project Overview

This project implements a microservices-based online library system with three independent services, each with its own database. The system demonstrates the interoperability of microservices using different technologies and programming languages.

---

## Architecture

### Services Implemented

#### 1. **Catalog Service**
- **Language:** Python
- **Framework:** Flask
- **Database:** PostgreSQL
- **Port:** 5000
- **Endpoints:**
  - `GET /catalog` - List all books
  - `GET /catalog/<id>` - Get specific book
  - `POST /catalog` - Create new book
  - `PUT /catalog/<id>` - Update book
  - `DELETE /catalog/<id>` - Delete book

#### 2. **User Service**
- **Language:** Python
- **Framework:** Flask
- **Database:** MySQL
- **Port:** 5001
- **Endpoints:**
  - `GET /users` - List all users
  - `GET /users/<id>` - Get specific user
  - `POST /users` - Create new user
  - `PUT /users/<id>` - Update user
  - `DELETE /users/<id>` - Delete user

#### 3. **Order Service**
- **Language:** PHP
- **Framework:** Native PHP with Apache
- **Database:** MySQL
- **Port:** 8080
- **Endpoints:**
  - `GET /orders` - List all orders
  - `GET /orders/<id>` - Get specific order
  - `POST /orders` - Create new order
  - `PUT /orders/<id>` - Update order
  - `DELETE /orders/<id>` - Delete order

---

## Database Configuration

Each service has its own independent database with unique credentials:

| Service | Database Type | Container Name | Database Name | Username | Password |
|---------|--------------|----------------|---------------|----------|----------|
| Catalog | PostgreSQL   | catalog-db     | catalog_db    | catalog_user | catalog_pass |
| User    | MySQL        | user-db        | user_db       | user_user    | user_pass    |
| Order   | MySQL        | order-db       | order_db      | order_user   | order_pass   |

**Data Persistence:** Each database uses Docker volumes for persistent storage:
- `catalog-data` - Catalog database
- `user-data` - User database
- `order-data` - Order database

---

## Docker Configuration

### Network
- **Network Name:** `library-net`
- **Driver:** bridge
- **Purpose:** Enables communication between services and databases

### Dockerfiles

Each service has its own Dockerfile:

1. **catalog-service/Dockerfile**
   - Base: `python:3.11-slim`
   - Dependencies: Flask, psycopg2-binary

2. **user-service/Dockerfile**
   - Base: `python:3.11-slim`
   - Dependencies: Flask, mysql-connector-python

3. **order-service/Dockerfile**
   - Base: `php:8.2-apache`
   - Dependencies: PDO, PDO MySQL

### Docker Compose

The `docker-compose.yml` orchestrates all services and databases with:
- Health checks for all databases
- Dependency management (services wait for databases)
- Environment variable configuration
- Port mappings
- Volume mounts

---

## Features Implemented

### ✅ Core Requirements

1. **Independent Databases**
   - Each service has its own database instance
   - Different database systems (PostgreSQL, MySQL)
   - Unique credentials per service
   - Data persistence with volumes

2. **Full CRUD Operations**
   - ✅ CREATE - All services support creating new records
   - ✅ READ - All services support listing and retrieving records
   - ✅ UPDATE - All services support updating existing records
   - ✅ DELETE - All services support deleting records

3. **Docker Configuration**
   - Individual Dockerfiles for each service
   - Docker Compose for orchestration
   - Health checks for databases
   - Automatic database initialization

4. **Environment Variables**
   - All database credentials configured via environment variables
   - DB_HOST, DB_NAME, DB_USER, DB_PASS for each service

5. **Sample Data**
   - Catalog Service: 5 pre-loaded books
   - User Service: 5 pre-loaded users
   - Order Service: 5 pre-loaded orders

---

## Testing Results

### Test Execution

All services have been tested and verified to be working correctly:

#### Catalog Service (✅ Passed)
```bash
GET http://localhost:5000/catalog
- Returns 5 books (The Great Gatsby, To Kill a Mockingbird, 1984, etc.)
- Status: 200 OK
```

#### User Service (✅ Passed)
```bash
GET http://localhost:5001/users
- Returns 5 users with complete profile information
- Status: 200 OK
```

#### Order Service (✅ Passed)
```bash
GET http://localhost:8080/orders
- Returns 5 orders with user/book associations
- Status: 200 OK
```

### Individual Record Retrieval (✅ Passed)
- `GET /catalog/1` - Returns single book
- `GET /users/1` - Returns single user
- `GET /orders/1` - Returns single order

---

## How to Run

### Option 1: Using Docker Compose (Recommended)

```bash
# Start all services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Stop and remove all data
docker-compose down -v
```

### Option 2: Manual Deployment

See [README.md](README.md) for detailed manual deployment commands.

---

## Project Structure

```
assignment2-docker/
├── catalog-service/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Container configuration
├── user-service/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Container configuration
├── order-service/
│   ├── index.php           # PHP application
│   ├── .htaccess           # Apache URL rewriting
│   └── Dockerfile          # Container configuration
├── docker-compose.yml      # Orchestration configuration
├── README.md               # Detailed documentation
├── test-services.sh        # Automated testing script
└── ASSIGNMENT_SUMMARY.md   # This file
```

---

## Key Technologies

- **Containerization:** Docker, Docker Compose
- **Languages:** Python 3.11, PHP 8.2
- **Frameworks:** Flask 3.0, Apache 2.4
- **Databases:** PostgreSQL 15, MySQL 8.0
- **API Style:** RESTful JSON APIs
- **Network:** Docker bridge network

---

## Additional Features

1. **Health Check Endpoints**
   - Each service has a root endpoint (`/`) that returns service status

2. **Error Handling**
   - Proper HTTP status codes (200, 201, 404, 500)
   - JSON error responses

3. **Automatic Database Initialization**
   - Tables created automatically on first run
   - Sample data inserted if tables are empty

4. **Comprehensive Documentation**
   - README with setup instructions
   - API endpoint documentation
   - Manual deployment commands
   - Testing examples

---

## Testing Tools Used

- **curl** - Command-line HTTP testing
- **Postman** - Can be used for API testing (examples provided in README)
- **Docker logs** - For debugging and monitoring

---

## Conclusion

This assignment successfully demonstrates:

1. ✅ Microservices architecture with independent services
2. ✅ Each service with its own database (database-per-service pattern)
3. ✅ Different technologies working together (Python, PHP, PostgreSQL, MySQL)
4. ✅ Docker containerization and orchestration
5. ✅ Full CRUD operations
6. ✅ RESTful API design
7. ✅ Data persistence
8. ✅ Health checks and monitoring
9. ✅ Comprehensive documentation

All requirements have been met and the system is fully functional and ready for evaluation.
