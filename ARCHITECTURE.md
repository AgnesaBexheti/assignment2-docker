# System Architecture Diagram

## Online Library System - Microservices Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          Docker Network: library-net                     │
│                                                                          │
│  ┌────────────────────┐  ┌────────────────────┐  ┌───────────────────┐ │
│  │  Catalog Service   │  │   User Service     │  │  Order Service    │ │
│  │  (Python/Flask)    │  │  (Python/Flask)    │  │     (PHP)         │ │
│  │   Port: 5000       │  │   Port: 5001       │  │   Port: 8080      │ │
│  │                    │  │                    │  │                   │ │
│  │  ┌──────────────┐  │  │  ┌──────────────┐  │  │  ┌─────────────┐ │ │
│  │  │   Endpoints  │  │  │  │   Endpoints  │  │  │  │  Endpoints  │ │ │
│  │  ├──────────────┤  │  │  ├──────────────┤  │  │  ├─────────────┤ │ │
│  │  │ GET /catalog │  │  │  │ GET /users   │  │  │  │ GET /orders │ │ │
│  │  │ GET /cata../1│  │  │  │ GET /users/1 │  │  │  │ GET /ord../1│ │ │
│  │  │ POST /catalog│  │  │  │ POST /users  │  │  │  │ POST /orders│ │ │
│  │  │ PUT /cata../1│  │  │  │ PUT /users/1 │  │  │  │ PUT /ord../1│ │ │
│  │  │ DELETE ../1  │  │  │  │ DELETE ../1  │  │  │  │ DELETE ../1 │ │ │
│  │  └──────────────┘  │  │  └──────────────┘  │  │  └─────────────┘ │ │
│  │          │          │  │          │          │  │         │        │ │
│  └──────────┼──────────┘  └──────────┼──────────┘  └─────────┼────────┘ │
│             │                        │                       │          │
│             ▼                        ▼                       ▼          │
│  ┌─────────────────┐      ┌─────────────────┐    ┌─────────────────┐  │
│  │   catalog-db    │      │    user-db      │    │    order-db     │  │
│  │   PostgreSQL    │      │     MySQL       │    │     MySQL       │  │
│  │   Port: 5432    │      │   Port: 3306    │    │   Port: 3306    │  │
│  │                 │      │                 │    │                 │  │
│  │ DB: catalog_db  │      │ DB: user_db     │    │ DB: order_db    │  │
│  │ User: catalog..│      │ User: user_user │    │ User: order_..  │  │
│  │                 │      │                 │    │                 │  │
│  │ ┌─────────────┐ │      │ ┌─────────────┐ │    │ ┌─────────────┐ │  │
│  │ │   Tables    │ │      │ │   Tables    │ │    │ │   Tables    │ │  │
│  │ ├─────────────┤ │      │ ├─────────────┤ │    │ ├─────────────┤ │  │
│  │ │   books     │ │      │ │   users     │ │    │ │   orders    │ │  │
│  │ └─────────────┘ │      │ └─────────────┘ │    │ └─────────────┘ │  │
│  │                 │      │                 │    │                 │  │
│  │ Volume:         │      │ Volume:         │    │ Volume:         │  │
│  │ catalog-data    │      │ user-data       │    │ order-data      │  │
│  └─────────────────┘      └─────────────────┘    └─────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   External Access    │
                         ├──────────────────────┤
                         │ localhost:5000       │
                         │ localhost:5001       │
                         │ localhost:8080       │
                         └──────────────────────┘
```

## Data Models

### Catalog Service - Books Table
```
┌──────────────────┬───────────────┬─────────────┐
│ Field            │ Type          │ Constraints │
├──────────────────┼───────────────┼─────────────┤
│ id               │ SERIAL        │ PRIMARY KEY │
│ title            │ VARCHAR(255)  │ NOT NULL    │
│ author           │ VARCHAR(255)  │ NOT NULL    │
│ isbn             │ VARCHAR(13)   │ UNIQUE      │
│ published_year   │ INTEGER       │             │
│ genre            │ VARCHAR(100)  │             │
│ available_copies │ INTEGER       │ DEFAULT 0   │
└──────────────────┴───────────────┴─────────────┘
```

### User Service - Users Table
```
┌──────────────┬───────────────┬─────────────────────────┐
│ Field        │ Type          │ Constraints             │
├──────────────┼───────────────┼─────────────────────────┤
│ id           │ INT           │ AUTO_INCREMENT, PK      │
│ username     │ VARCHAR(100)  │ UNIQUE, NOT NULL        │
│ email        │ VARCHAR(255)  │ UNIQUE, NOT NULL        │
│ full_name    │ VARCHAR(255)  │ NOT NULL                │
│ phone        │ VARCHAR(20)   │                         │
│ address      │ TEXT          │                         │
│ created_at   │ TIMESTAMP     │ DEFAULT CURRENT_TIME    │
└──────────────┴───────────────┴─────────────────────────┘
```

### Order Service - Orders Table
```
┌──────────────┬──────────────┬─────────────────────────┐
│ Field        │ Type         │ Constraints             │
├──────────────┼──────────────┼─────────────────────────┤
│ id           │ INT          │ AUTO_INCREMENT, PK      │
│ user_id      │ INT          │ NOT NULL                │
│ book_id      │ INT          │ NOT NULL                │
│ quantity     │ INT          │ NOT NULL, DEFAULT 1     │
│ status       │ VARCHAR(50)  │ DEFAULT 'pending'       │
│ order_date   │ TIMESTAMP    │ DEFAULT CURRENT_TIME    │
│ total_price  │ DECIMAL(10,2)│                         │
└──────────────┴──────────────┴─────────────────────────┘
```

## Request Flow Example

### Example: Retrieving All Books

```
Client Request
     │
     ▼
GET http://localhost:5000/catalog
     │
     ▼
Catalog Service (Flask)
     │
     ▼
Query: SELECT * FROM books
     │
     ▼
PostgreSQL Database (catalog-db)
     │
     ▼
Return Results
     │
     ▼
JSON Response to Client
```

## Technology Stack

```
┌─────────────────────────────────────────┐
│         Application Layer               │
├─────────────────────────────────────────┤
│ Catalog Service  │ Python 3.11 + Flask  │
│ User Service     │ Python 3.11 + Flask  │
│ Order Service    │ PHP 8.2 + Apache     │
└─────────────────────────────────────────┘
                    │
┌─────────────────────────────────────────┐
│         Data Access Layer               │
├─────────────────────────────────────────┤
│ Catalog DB       │ psycopg2             │
│ User DB          │ mysql-connector      │
│ Order DB         │ PDO                  │
└─────────────────────────────────────────┘
                    │
┌─────────────────────────────────────────┐
│         Database Layer                  │
├─────────────────────────────────────────┤
│ PostgreSQL 15    │ MySQL 8.0 (×2)      │
└─────────────────────────────────────────┘
                    │
┌─────────────────────────────────────────┐
│      Infrastructure Layer               │
├─────────────────────────────────────────┤
│ Docker Containers + Docker Compose      │
│ Bridge Network: library-net             │
│ Persistent Volumes (×3)                 │
└─────────────────────────────────────────┘
```

## Container Dependencies

```
catalog-service ──depends_on──> catalog-db (PostgreSQL)
user-service ────depends_on──> user-db (MySQL)
order-service ───depends_on──> order-db (MySQL)
```

## Port Mapping

```
Host System                 Docker Container
────────────────            ───────────────
localhost:5000    ──────>   catalog-service:5000
localhost:5001    ──────>   user-service:5001
localhost:8080    ──────>   order-service:80

Internal Network Only:
catalog-db:5432   (PostgreSQL)
user-db:3306      (MySQL)
order-db:3306     (MySQL)
```

## Volume Persistence

```
Docker Volume        Mounted To                   Purpose
──────────────────   ─────────────────────────   ──────────────────
catalog-data    ──>  /var/lib/postgresql/data    Book catalog data
user-data       ──>  /var/lib/mysql              User profiles data
order-data      ──>  /var/lib/mysql              Order records data
```

## Microservices Principles Demonstrated

1. **Service Independence**
   - Each service can be deployed independently
   - Separate codebases and technologies

2. **Database-per-Service**
   - Each service owns its database
   - No shared database between services

3. **Technology Heterogeneity**
   - Python (Catalog, User)
   - PHP (Order)
   - PostgreSQL + MySQL

4. **API-First Design**
   - RESTful JSON APIs
   - Standardized endpoints

5. **Containerization**
   - Each service in its own container
   - Reproducible environments
