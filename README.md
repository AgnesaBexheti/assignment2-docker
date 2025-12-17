# Online Library System - Microservices Architecture

A microservices-based online library system with three independent services, each with its own database.

## Architecture Overview

### Services:
1. **Catalog Service** (Python/Flask + PostgreSQL)
   - Manages book catalog
   - Port: 5000
   - Database: PostgreSQL

2. **User Service** (Python/Flask + MySQL)
   - Manages user profiles
   - Port: 5001
   - Database: MySQL

3. **Order Service** (PHP + MySQL)
   - Manages book orders
   - Port: 8080
   - Database: MySQL

## Quick Start with Docker Compose

### Prerequisites
- Docker
- Docker Compose

### Running the Application

```bash
# Build and start all services
docker-compose up --build

# Run in detached mode
docker-compose up -d --build

# Stop all services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```

### Service URLs
- Catalog Service: http://localhost:5000
- User Service: http://localhost:5001
- Order Service: http://localhost:8080

## Manual Deployment (Without Docker Compose)

### Step 1: Create Network
```bash
docker network create library-net
```

### Step 2: Create and Run Databases

#### Catalog Database (PostgreSQL)
```bash
# Create volume
docker volume create catalog-data

# Run PostgreSQL
docker run -d \
  --name catalog-db \
  --network library-net \
  -e POSTGRES_DB=catalog_db \
  -e POSTGRES_USER=catalog_user \
  -e POSTGRES_PASSWORD=catalog_pass \
  -v catalog-data:/var/lib/postgresql/data \
  postgres:15-alpine
```

#### User Database (MySQL)
```bash
# Create volume
docker volume create user-data

# Run MySQL
docker run -d \
  --name user-db \
  --network library-net \
  -e MYSQL_DATABASE=user_db \
  -e MYSQL_USER=user_user \
  -e MYSQL_PASSWORD=user_pass \
  -e MYSQL_ROOT_PASSWORD=root_pass \
  -v user-data:/var/lib/mysql \
  mysql:8.0
```

#### Order Database (MySQL)
```bash
# Create volume
docker volume create order-data

# Run MySQL
docker run -d \
  --name order-db \
  --network library-net \
  -e MYSQL_DATABASE=order_db \
  -e MYSQL_USER=order_user \
  -e MYSQL_PASSWORD=order_pass \
  -e MYSQL_ROOT_PASSWORD=root_pass \
  -v order-data:/var/lib/mysql \
  mysql:8.0
```

### Step 3: Build and Run Services

#### Catalog Service
```bash
# Build image
docker build -t catalog-service ./catalog-service

# Run container
docker run -d \
  --name catalog-service \
  --network library-net \
  -p 5000:5000 \
  -e DB_HOST=catalog-db \
  -e DB_NAME=catalog_db \
  -e DB_USER=catalog_user \
  -e DB_PASS=catalog_pass \
  catalog-service
```

#### User Service
```bash
# Build image
docker build -t user-service ./user-service

# Run container
docker run -d \
  --name user-service \
  --network library-net \
  -p 5001:5001 \
  -e DB_HOST=user-db \
  -e DB_NAME=user_db \
  -e DB_USER=user_user \
  -e DB_PASS=user_pass \
  user-service
```

#### Order Service
```bash
# Build image
docker build -t order-service ./order-service

# Run container
docker run -d \
  --name order-service \
  --network library-net \
  -p 8080:80 \
  -e DB_HOST=order-db \
  -e DB_NAME=order_db \
  -e DB_USER=order_user \
  -e DB_PASS=order_pass \
  order-service
```

### Clean Up Manual Deployment
```bash
# Stop and remove all containers
docker stop catalog-service user-service order-service catalog-db user-db order-db
docker rm catalog-service user-service order-service catalog-db user-db order-db

# Remove network
docker network rm library-net

# Remove volumes (optional - deletes all data)
docker volume rm catalog-data user-data order-data
```

## API Endpoints

### Catalog Service (Port 5000)

#### READ Operations
```bash
# Get all books
curl http://localhost:5000/catalog

# Get specific book
curl http://localhost:5000/catalog/1
```

#### CREATE
```bash
curl -X POST http://localhost:5000/catalog \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Book",
    "author": "Author Name",
    "isbn": "9781234567890",
    "published_year": 2024,
    "genre": "Fiction",
    "available_copies": 5
  }'
```

#### UPDATE
```bash
curl -X PUT http://localhost:5000/catalog/1 \
  -H "Content-Type: application/json" \
  -d '{"available_copies": 10}'
```

#### DELETE
```bash
curl -X DELETE http://localhost:5000/catalog/1
```

### User Service (Port 5001)

#### READ Operations
```bash
# Get all users
curl http://localhost:5001/users

# Get specific user
curl http://localhost:5001/users/1
```

#### CREATE
```bash
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@email.com",
    "full_name": "New User",
    "phone": "+1234567890",
    "address": "123 Street"
  }'
```

#### UPDATE
```bash
curl -X PUT http://localhost:5001/users/1 \
  -H "Content-Type: application/json" \
  -d '{"phone": "+9876543210"}'
```

#### DELETE
```bash
curl -X DELETE http://localhost:5001/users/1
```

### Order Service (Port 8080)

#### READ Operations
```bash
# Get all orders
curl http://localhost:8080/orders

# Get specific order
curl http://localhost:8080/orders/1
```

#### CREATE
```bash
curl -X POST http://localhost:8080/orders \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "book_id": 2,
    "quantity": 3,
    "status": "pending",
    "total_price": 45.99
  }'
```

#### UPDATE
```bash
curl -X PUT http://localhost:8080/orders/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "shipped"}'
```

#### DELETE
```bash
curl -X DELETE http://localhost:8080/orders/1
```

## Testing with Postman

1. Import the following endpoints into Postman:
   - GET http://localhost:5000/catalog
   - GET http://localhost:5001/users
   - GET http://localhost:8080/orders

2. Each service returns JSON responses with sample data

3. Test CRUD operations using the endpoints above

## Project Structure

```
.
├── catalog-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── user-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── order-service/
│   ├── index.php
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Database Configuration

Each service uses unique database credentials:

| Service | Database | Host | User | Password | Database Name |
|---------|----------|------|------|----------|---------------|
| Catalog | PostgreSQL | catalog-db | catalog_user | catalog_pass | catalog_db |
| User | MySQL | user-db | user_user | user_pass | user_db |
| Order | MySQL | order-db | order_user | order_pass | order_db |


## Troubleshooting

### Check running containers
```bash
docker ps
```

### View logs
```bash
# Docker Compose
docker-compose logs -f [service-name]

# Individual containers
docker logs -f catalog-service
docker logs -f user-service
docker logs -f order-service
```

### Restart a service
```bash
docker-compose restart catalog-service
```

### Access database directly
```bash
# PostgreSQL
docker exec -it catalog-db psql -U catalog_user -d catalog_db

# MySQL
docker exec -it user-db mysql -u user_user -puser_pass user_db
docker exec -it order-db mysql -u order_user -porder_pass order_db
```
