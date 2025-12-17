# Testing Guide - Online Library System

## Quick Start Testing

### 1. Start All Services
```bash
docker-compose up -d --build
```

### 2. Verify All Services Are Running
```bash
docker-compose ps
```

Expected output: All 6 containers should be "Up" and databases should be "healthy"

---

## READ Operations Testing (Required for Initial Submission)

### Catalog Service Tests

#### Test 1: Get All Books
```bash
curl http://localhost:5000/catalog
```

**Expected Response:**
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

#### Test 2: Get Single Book
```bash
curl http://localhost:5000/catalog/1
```

**Expected Response:**
```json
{
  "success": true,
  "book": {
    "id": 1,
    "title": "The Great Gatsby",
    ...
  }
}
```

#### Test 3: Health Check
```bash
curl http://localhost:5000/
```

**Expected Response:**
```json
{
  "service": "Catalog Service",
  "status": "running",
  "endpoints": ["/catalog", "/catalog/<id>"]
}
```

---

### User Service Tests

#### Test 4: Get All Users
```bash
curl http://localhost:5001/users
```

**Expected Response:**
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

#### Test 5: Get Single User
```bash
curl http://localhost:5001/users/2
```

**Expected Response:**
```json
{
  "success": true,
  "user": {
    "id": 2,
    "username": "jane_smith",
    ...
  }
}
```

#### Test 6: Health Check
```bash
curl http://localhost:5001/
```

---

### Order Service Tests

#### Test 7: Get All Orders
```bash
curl http://localhost:8080/orders
```

**Expected Response:**
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
      "order_date": "2025-12-17 10:20:39",
      "total_price": "29.99"
    },
    ...
  ]
}
```

#### Test 8: Get Single Order
```bash
curl http://localhost:8080/orders/3
```

**Expected Response:**
```json
{
  "success": true,
  "order": {
    "id": 3,
    "user_id": 1,
    "book_id": 3,
    "quantity": 3,
    "status": "pending",
    "total_price": "44.97"
  }
}
```

#### Test 9: Health Check
```bash
curl http://localhost:8080/
```

---

## CREATE Operations Testing

### Create New Book
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
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Book created successfully",
  "book": {
    "id": 6,
    "title": "Clean Code",
    ...
  }
}
```

### Create New User
```bash
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "test_user",
    "email": "test@email.com",
    "full_name": "Test User",
    "phone": "+1234567890",
    "address": "123 Test St"
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "User created successfully",
  "user": {
    "id": 6,
    "username": "test_user",
    ...
  }
}
```

### Create New Order
```bash
curl -X POST http://localhost:8080/orders \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "book_id": 2,
    "quantity": 2,
    "status": "pending",
    "total_price": 25.50
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Order created successfully",
  "order": {
    "id": 6,
    "user_id": 1,
    ...
  }
}
```

---

## UPDATE Operations Testing

### Update Book
```bash
curl -X PUT http://localhost:5000/catalog/1 \
  -H "Content-Type: application/json" \
  -d '{
    "available_copies": 10
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Book updated successfully",
  "book": {
    "id": 1,
    "available_copies": 10,
    ...
  }
}
```

### Update User
```bash
curl -X PUT http://localhost:5001/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "+9999999999"
  }'
```

### Update Order
```bash
curl -X PUT http://localhost:8080/orders/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "shipped"
  }'
```

---

## DELETE Operations Testing

### Delete Book
```bash
curl -X DELETE http://localhost:5000/catalog/6
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Book deleted successfully",
  "book": {
    "id": 6,
    ...
  }
}
```

### Delete User
```bash
curl -X DELETE http://localhost:5001/users/6
```

### Delete Order
```bash
curl -X DELETE http://localhost:8080/orders/6
```

---

## Testing with Postman

### Import to Postman

Create a new Collection in Postman with the following requests:

#### Catalog Service Collection

1. **GET All Books**
   - Method: GET
   - URL: `http://localhost:5000/catalog`

2. **GET Single Book**
   - Method: GET
   - URL: `http://localhost:5000/catalog/1`

3. **POST Create Book**
   - Method: POST
   - URL: `http://localhost:5000/catalog`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON):
     ```json
     {
       "title": "Test Book",
       "author": "Test Author",
       "isbn": "1234567890123",
       "published_year": 2024,
       "genre": "Test",
       "available_copies": 5
     }
     ```

4. **PUT Update Book**
   - Method: PUT
   - URL: `http://localhost:5000/catalog/1`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON):
     ```json
     {
       "available_copies": 20
     }
     ```

5. **DELETE Book**
   - Method: DELETE
   - URL: `http://localhost:5000/catalog/6`

#### User Service Collection

Similar structure for User Service on port 5001

#### Order Service Collection

Similar structure for Order Service on port 8080

---

## Automated Testing Script

Run the provided test script:

```bash
bash test-services.sh
```

This script will automatically test all three services and display the results.

---

## Error Testing

### Test Invalid Endpoint
```bash
curl http://localhost:5000/invalid
```

**Expected:** 404 Not Found

### Test Missing Required Fields
```bash
curl -X POST http://localhost:5000/catalog \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Incomplete Book"
  }'
```

**Expected:** 400 Bad Request with error message

### Test Non-Existent Record
```bash
curl http://localhost:5000/catalog/9999
```

**Expected:** 404 Not Found

---

## Database Verification

### Connect to PostgreSQL (Catalog DB)
```bash
docker exec -it catalog-db psql -U catalog_user -d catalog_db
```

Then run:
```sql
SELECT * FROM books;
\q  -- to exit
```

### Connect to MySQL (User DB)
```bash
docker exec -it user-db mysql -u user_user -puser_pass user_db
```

Then run:
```sql
SELECT * FROM users;
exit;
```

### Connect to MySQL (Order DB)
```bash
docker exec -it order-db mysql -u order_user -porder_pass order_db
```

Then run:
```sql
SELECT * FROM orders;
exit;
```

---

## Monitoring and Logs

### View All Logs
```bash
docker-compose logs -f
```

### View Specific Service Logs
```bash
docker-compose logs -f catalog-service
docker-compose logs -f user-service
docker-compose logs -f order-service
```

### View Database Logs
```bash
docker-compose logs -f catalog-db
docker-compose logs -f user-db
docker-compose logs -f order-db
```

---

## Performance Testing

### Test Response Time
```bash
time curl -s http://localhost:5000/catalog > /dev/null
```

### Test Multiple Requests
```bash
for i in {1..10}; do
  curl -s http://localhost:5000/catalog/1 > /dev/null
  echo "Request $i completed"
done
```

---

## Troubleshooting

### Service Not Responding
```bash
# Check if container is running
docker ps

# Restart specific service
docker-compose restart catalog-service

# Rebuild service
docker-compose up -d --build catalog-service
```

### Database Connection Issues
```bash
# Check database health
docker-compose ps

# View database logs
docker-compose logs catalog-db

# Restart database
docker-compose restart catalog-db
```

### Reset Everything
```bash
# Stop all services and remove volumes
docker-compose down -v

# Rebuild and start
docker-compose up -d --build
```

---

## Test Checklist for Assignment Submission

- [ ] All 6 containers are running (3 services + 3 databases)
- [ ] All databases show "healthy" status
- [ ] Catalog Service READ operations work (GET /catalog, GET /catalog/1)
- [ ] User Service READ operations work (GET /users, GET /users/1)
- [ ] Order Service READ operations work (GET /orders, GET /orders/1)
- [ ] All services return proper JSON responses
- [ ] Health check endpoints work for all services
- [ ] CREATE operations work for all services (optional for initial submission)
- [ ] UPDATE operations work for all services (optional for initial submission)
- [ ] DELETE operations work for all services (optional for initial submission)
- [ ] Data persists after container restart
- [ ] Each service uses its own independent database
- [ ] Environment variables are properly configured

---

## Sample Test Output

### Successful Test
```
$ curl http://localhost:5000/catalog/1
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

### Failed Test (Not Found)
```
$ curl http://localhost:5000/catalog/999
{
  "success": false,
  "error": "Book not found"
}
```

---

## Contact & Support

If you encounter any issues during testing:

1. Check the logs: `docker-compose logs -f`
2. Verify all services are running: `docker-compose ps`
3. Review the README.md for setup instructions
4. Check ARCHITECTURE.md for system design details
