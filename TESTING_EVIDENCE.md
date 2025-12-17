# Testing Evidence - Online Library System

## Submission Proof Documentation

This document contains all commands and expected outputs for testing the Online Library System. Use these commands to generate screenshots for your submission.

---

## Prerequisites

### 1. Verify All Services Are Running

```bash
docker-compose ps
```

**Expected Output:**
```
NAME              IMAGE                                COMMAND                  STATUS
catalog-db        postgres:15-alpine                   ...                      Up (healthy)
catalog-service   assignment2-docker-catalog-service   ...                      Up
user-db           mysql:8.0                            ...                      Up (healthy)
user-service      assignment2-docker-user-service      ...                      Up
order-db          mysql:8.0                            ...                      Up (healthy)
order-service     assignment2-docker-order-service     ...                      Up
```

📸 **Screenshot #1: Docker Compose Status** - Shows all 6 containers running

---

## Catalog Service Testing (Python/Flask + PostgreSQL)

### Test 1: READ - Get All Books

```bash
curl -X GET http://localhost:5000/catalog | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "count": 5,
    "books": [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "isbn": "9780743273565",
            "published_year": 1925,
            "genre": "Fiction",
            "available_copies": 5
        },
        ...
    ]
}
```

📸 **Screenshot #2: Catalog READ All** - Shows all books

---

### Test 2: READ - Get Single Book

```bash
curl -X GET http://localhost:5000/catalog/1 | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "book": {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "isbn": "9780743273565",
        "published_year": 1925,
        "genre": "Fiction",
        "available_copies": 5
    }
}
```

📸 **Screenshot #3: Catalog READ Single** - Shows single book details

---

### Test 3: CREATE - Add New Book

```bash
curl -X POST http://localhost:5000/catalog \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "isbn": "9780132350884",
    "published_year": 2008,
    "genre": "Technology",
    "available_copies": 10
  }' | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "Book created successfully",
    "book": {
        "id": 6,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "published_year": 2008,
        "genre": "Technology",
        "available_copies": 10
    }
}
```

📸 **Screenshot #4: Catalog CREATE** - Shows new book created

---

### Test 4: UPDATE - Update Book

```bash
curl -X PUT http://localhost:5000/catalog/6 \
  -H "Content-Type: application/json" \
  -d '{
    "available_copies": 20
  }' | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "Book updated successfully",
    "book": {
        "id": 6,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "published_year": 2008,
        "genre": "Technology",
        "available_copies": 20
    }
}
```

📸 **Screenshot #5: Catalog UPDATE** - Shows book updated

---

### Test 5: DELETE - Remove Book

```bash
curl -X DELETE http://localhost:5000/catalog/6 | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "Book deleted successfully",
    "book": {
        "id": 6,
        "title": "Clean Code",
        ...
    }
}
```

📸 **Screenshot #6: Catalog DELETE** - Shows book deleted

---

## User Service Testing (Python/Flask + MySQL)

### Test 6: READ - Get All Users

```bash
curl -X GET http://localhost:5001/users | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "count": 5,
    "users": [
        {
            "id": 1,
            "username": "john_doe",
            "email": "john.doe@email.com",
            "full_name": "John Doe",
            "phone": "+1234567890",
            "address": "123 Main St, City, State",
            "created_at": "..."
        },
        ...
    ]
}
```

📸 **Screenshot #7: User READ All** - Shows all users

---

### Test 7: READ - Get Single User

```bash
curl -X GET http://localhost:5001/users/1 | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john.doe@email.com",
        "full_name": "John Doe",
        "phone": "+1234567890",
        "address": "123 Main St, City, State",
        "created_at": "..."
    }
}
```

📸 **Screenshot #8: User READ Single** - Shows single user

---

### Test 8: CREATE - Add New User

```bash
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "test_user",
    "email": "test@example.com",
    "full_name": "Test User",
    "phone": "+1555000000",
    "address": "456 Test Ave"
  }' | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "User created successfully",
    "user": {
        "id": 6,
        "username": "test_user",
        "email": "test@example.com",
        "full_name": "Test User",
        "phone": "+1555000000",
        "address": "456 Test Ave",
        "created_at": "..."
    }
}
```

📸 **Screenshot #9: User CREATE** - Shows new user created

---

### Test 9: UPDATE - Update User

```bash
curl -X PUT http://localhost:5001/users/6 \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "+1999999999"
  }' | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "User updated successfully",
    "user": {
        "id": 6,
        "username": "test_user",
        "email": "test@example.com",
        "full_name": "Test User",
        "phone": "+1999999999",
        "address": "456 Test Ave",
        "created_at": "..."
    }
}
```

📸 **Screenshot #10: User UPDATE** - Shows user updated

---

### Test 10: DELETE - Remove User

```bash
curl -X DELETE http://localhost:5001/users/6 | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "User deleted successfully",
    "user": {
        "id": 6,
        "username": "test_user",
        ...
    }
}
```

📸 **Screenshot #11: User DELETE** - Shows user deleted

---

## Order Service Testing (PHP + MySQL)

### Test 11: READ - Get All Orders

```bash
curl -X GET http://localhost:8080/orders | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "count": 5,
    "orders": [
        {
            "id": 1,
            "user_id": 1,
            "book_id": 1,
            "quantity": 2,
            "status": "completed",
            "order_date": "2025-12-17 11:28:39",
            "total_price": "29.99"
        },
        ...
    ]
}
```

📸 **Screenshot #12: Order READ All** - Shows all orders

---

### Test 12: READ - Get Single Order

```bash
curl -X GET http://localhost:8080/orders/1 | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "order": {
        "id": 1,
        "user_id": 1,
        "book_id": 1,
        "quantity": 2,
        "status": "completed",
        "order_date": "2025-12-17 11:28:39",
        "total_price": "29.99"
    }
}
```

📸 **Screenshot #13: Order READ Single** - Shows single order

---

### Test 13: CREATE - Add New Order

```bash
curl -X POST http://localhost:8080/orders \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 2,
    "book_id": 3,
    "quantity": 5,
    "status": "pending",
    "total_price": 99.95
  }' | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "Order created successfully",
    "order": {
        "id": 6,
        "user_id": 2,
        "book_id": 3,
        "quantity": 5,
        "status": "pending",
        "order_date": "...",
        "total_price": "99.95"
    }
}
```

📸 **Screenshot #14: Order CREATE** - Shows new order created

---

### Test 14: UPDATE - Update Order

```bash
curl -X PUT http://localhost:8080/orders/6 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "shipped"
  }' | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "Order updated successfully",
    "order": {
        "id": 6,
        "user_id": 2,
        "book_id": 3,
        "quantity": 5,
        "status": "shipped",
        "order_date": "...",
        "total_price": "99.95"
    }
}
```

📸 **Screenshot #15: Order UPDATE** - Shows order updated

---

### Test 15: DELETE - Remove Order

```bash
curl -X DELETE http://localhost:8080/orders/6 | python -m json.tool
```

**Expected Output:**
```json
{
    "success": true,
    "message": "Order deleted successfully",
    "order": {
        "id": 6,
        "user_id": 2,
        "book_id": 3,
        ...
    }
}
```

📸 **Screenshot #16: Order DELETE** - Shows order deleted

---

## Database Separation Evidence

### Test 16: Verify Catalog Database (PostgreSQL)

```bash
docker exec -it catalog-db psql -U catalog_user -d catalog_db -c "\dt"
docker exec -it catalog-db psql -U catalog_user -d catalog_db -c "SELECT * FROM books LIMIT 3;"
```

📸 **Screenshot #17: Catalog Database** - Shows PostgreSQL with books table

---

### Test 17: Verify User Database (MySQL)

```bash
docker exec -it user-db mysql -u user_user -puser_pass user_db -e "SHOW TABLES;"
docker exec -it user-db mysql -u user_user -puser_pass user_db -e "SELECT * FROM users LIMIT 3;"
```

📸 **Screenshot #18: User Database** - Shows MySQL with users table

---

### Test 18: Verify Order Database (MySQL)

```bash
docker exec -it order-db mysql -u order_user -porder_pass order_db -e "SHOW TABLES;"
docker exec -it order-db mysql -u order_user -porder_pass order_db -e "SELECT * FROM orders LIMIT 3;"
```

📸 **Screenshot #19: Order Database** - Shows MySQL with orders table

---

## Docker Configuration Evidence

### Test 19: Show Docker Volumes

```bash
docker volume ls | grep assignment2
```

**Expected Output:**
```
assignment2-docker_catalog-data
assignment2-docker_user-data
assignment2-docker_order-data
```

📸 **Screenshot #20: Docker Volumes** - Shows 3 persistent volumes

---

### Test 20: Show Docker Network

```bash
docker network ls | grep library
docker network inspect assignment2-docker_library-net --format='{{range .Containers}}{{.Name}} {{end}}'
```

**Expected Output:**
```
library-net
catalog-db catalog-service user-db user-service order-db order-service
```

📸 **Screenshot #21: Docker Network** - Shows library-net with all containers

---

### Test 21: Show Environment Variables

```bash
docker exec catalog-service env | grep DB_
docker exec user-service env | grep DB_
docker exec order-service env | grep DB_
```

**Expected Output:**
```
# Catalog Service
DB_HOST=catalog-db
DB_NAME=catalog_db
DB_USER=catalog_user
DB_PASS=catalog_pass

# User Service
DB_HOST=user-db
DB_NAME=user_db
DB_USER=user_user
DB_PASS=user_pass

# Order Service
DB_HOST=order-db
DB_NAME=order_db
DB_USER=order_user
DB_PASS=order_pass
```

📸 **Screenshot #22: Environment Variables** - Shows different DB configs per service

---

## Health Check Evidence

### Test 22: All Service Health Checks

```bash
curl -X GET http://localhost:5000/ | python -m json.tool
curl -X GET http://localhost:5001/ | python -m json.tool
curl -X GET http://localhost:8080/ | python -m json.tool
```

**Expected Output:**
```json
{"service": "Catalog Service", "status": "running", "endpoints": [...]}
{"service": "User Service", "status": "running", "endpoints": [...]}
{"service": "Order Service", "status": "running", "endpoints": [...]}
```

📸 **Screenshot #23: Service Health Checks** - Shows all services running

---

## Complete Test Run Script

Create a file `run_all_tests.sh`:

```bash
#!/bin/bash

echo "========================================="
echo "COMPLETE CRUD TESTING - ALL SERVICES"
echo "========================================="
echo ""

echo "1. DOCKER STATUS"
echo "-----------------"
docker-compose ps
echo ""

echo "2. CATALOG SERVICE - CRUD TESTS"
echo "--------------------------------"
echo "READ All Books:"
curl -X GET http://localhost:5000/catalog | python -m json.tool
echo ""

echo "READ Single Book:"
curl -X GET http://localhost:5000/catalog/1 | python -m json.tool
echo ""

echo "CREATE Book:"
curl -X POST http://localhost:5000/catalog \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin","isbn":"9780132350884","published_year":2008,"genre":"Technology","available_copies":10}' \
  | python -m json.tool
echo ""

echo "UPDATE Book:"
curl -X PUT http://localhost:5000/catalog/6 \
  -H "Content-Type: application/json" \
  -d '{"available_copies":20}' \
  | python -m json.tool
echo ""

echo "DELETE Book:"
curl -X DELETE http://localhost:5000/catalog/6 | python -m json.tool
echo ""

echo "3. USER SERVICE - CRUD TESTS"
echo "-----------------------------"
echo "READ All Users:"
curl -X GET http://localhost:5001/users | python -m json.tool
echo ""

echo "READ Single User:"
curl -X GET http://localhost:5001/users/1 | python -m json.tool
echo ""

echo "CREATE User:"
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{"username":"test_user","email":"test@example.com","full_name":"Test User","phone":"+1555000000","address":"456 Test Ave"}' \
  | python -m json.tool
echo ""

echo "UPDATE User:"
curl -X PUT http://localhost:5001/users/6 \
  -H "Content-Type: application/json" \
  -d '{"phone":"+1999999999"}' \
  | python -m json.tool
echo ""

echo "DELETE User:"
curl -X DELETE http://localhost:5001/users/6 | python -m json.tool
echo ""

echo "4. ORDER SERVICE - CRUD TESTS"
echo "------------------------------"
echo "READ All Orders:"
curl -X GET http://localhost:8080/orders | python -m json.tool
echo ""

echo "READ Single Order:"
curl -X GET http://localhost:8080/orders/1 | python -m json.tool
echo ""

echo "CREATE Order:"
curl -X POST http://localhost:8080/orders \
  -H "Content-Type: application/json" \
  -d '{"user_id":2,"book_id":3,"quantity":5,"status":"pending","total_price":99.95}' \
  | python -m json.tool
echo ""

echo "UPDATE Order:"
curl -X PUT http://localhost:8080/orders/6 \
  -H "Content-Type: application/json" \
  -d '{"status":"shipped"}' \
  | python -m json.tool
echo ""

echo "DELETE Order:"
curl -X DELETE http://localhost:8080/orders/6 | python -m json.tool
echo ""

echo "========================================="
echo "ALL TESTS COMPLETED!"
echo "========================================="
```

Make it executable and run:
```bash
chmod +x run_all_tests.sh
./run_all_tests.sh
```

---

## Minimum Required Screenshots for Submission

### Essential Screenshots (23 total):

1. **Docker Status** - Shows all 6 containers running
2-6. **Catalog CRUD** - Read All, Read One, Create, Update, Delete
7-11. **User CRUD** - Read All, Read One, Create, Update, Delete
12-16. **Order CRUD** - Read All, Read One, Create, Update, Delete
17-19. **Database Separation** - PostgreSQL (Catalog), MySQL (User), MySQL (Order)
20-22. **Docker Config** - Volumes, Network, Environment Variables
23. **Health Checks** - All three services responding

---

## Alternative: Use Postman

Import these into Postman Collections:

1. Create Collection: "Catalog Service"
2. Create Collection: "User Service"
3. Create Collection: "Order Service"

For each collection, add the requests shown above.

**Export your Postman collection** and include it in your submission.

---

## Submission Checklist

- [ ] Screenshot of `docker-compose ps` showing all containers
- [ ] Screenshots of all CRUD operations for Catalog Service (5 screenshots)
- [ ] Screenshots of all CRUD operations for User Service (5 screenshots)
- [ ] Screenshots of all CRUD operations for Order Service (5 screenshots)
- [ ] Screenshots of database tables in each database (3 screenshots)
- [ ] Screenshot of Docker volumes
- [ ] Screenshot of Docker network
- [ ] Screenshot of environment variables
- [ ] Screenshot of health checks
- [ ] All source code files
- [ ] All documentation files

---

## Quick Evidence Generation

Run this one command to generate output for all tests:

```bash
bash run_all_tests.sh > test_results.txt 2>&1
```

Then take screenshots of the output!
