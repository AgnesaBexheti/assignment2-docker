# Quick Reference Card - Online Library System

## 🚀 Quick Commands

### Start/Stop Services
```bash
# Start all services
docker-compose up -d --build

# Stop all services
docker-compose down

# Stop and remove all data
docker-compose down -v

# Restart a service
docker-compose restart catalog-service
```

### Check Status
```bash
# View all containers
docker-compose ps

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f catalog-service
```

---

## 📡 Service URLs

| Service | URL | Port |
|---------|-----|------|
| Catalog Service | http://localhost:5000 | 5000 |
| User Service | http://localhost:5001 | 5001 |
| Order Service | http://localhost:8080 | 8080 |

---

## 🔍 Quick Tests (curl)

### Catalog Service
```bash
curl http://localhost:5000/catalog           # List all books
curl http://localhost:5000/catalog/1         # Get book #1
```

### User Service
```bash
curl http://localhost:5001/users             # List all users
curl http://localhost:5001/users/1           # Get user #1
```

### Order Service
```bash
curl http://localhost:8080/orders            # List all orders
curl http://localhost:8080/orders/1          # Get order #1
```

---

## 🗄️ Database Access

### PostgreSQL (Catalog)
```bash
docker exec -it catalog-db psql -U catalog_user -d catalog_db
```

### MySQL (User)
```bash
docker exec -it user-db mysql -u user_user -puser_pass user_db
```

### MySQL (Order)
```bash
docker exec -it order-db mysql -u order_user -porder_pass order_db
```

---

## 📊 API Endpoints Summary

### Catalog Service (Books)
- `GET /catalog` - List all books
- `GET /catalog/<id>` - Get specific book
- `POST /catalog` - Create new book
- `PUT /catalog/<id>` - Update book
- `DELETE /catalog/<id>` - Delete book

### User Service (Users)
- `GET /users` - List all users
- `GET /users/<id>` - Get specific user
- `POST /users` - Create new user
- `PUT /users/<id>` - Update user
- `DELETE /users/<id>` - Delete user

### Order Service (Orders)
- `GET /orders` - List all orders
- `GET /orders/<id>` - Get specific order
- `POST /orders` - Create new order
- `PUT /orders/<id>` - Update order
- `DELETE /orders/<id>` - Delete order

---

## 🔧 Troubleshooting

### Service not responding?
```bash
docker-compose restart <service-name>
docker-compose logs -f <service-name>
```

### Database connection issues?
```bash
docker-compose ps                 # Check if DB is healthy
docker-compose restart <db-name>  # Restart database
```

### Reset everything
```bash
docker-compose down -v
docker-compose up -d --build
```

---

## 📁 Project Structure

```
assignment2-docker/
├── catalog-service/     # Python/Flask + PostgreSQL
├── user-service/        # Python/Flask + MySQL
├── order-service/       # PHP + MySQL
├── docker-compose.yml   # Orchestration
└── *.md                # Documentation
```

---

## 🗃️ Database Credentials

### Catalog Database (PostgreSQL)
- Host: `catalog-db`
- Database: `catalog_db`
- User: `catalog_user`
- Password: `catalog_pass`

### User Database (MySQL)
- Host: `user-db`
- Database: `user_db`
- User: `user_user`
- Password: `user_pass`

### Order Database (MySQL)
- Host: `order-db`
- Database: `order_db`
- User: `order_user`
- Password: `order_pass`

---

## 📝 Sample Data Counts

- **Books:** 5 records
- **Users:** 5 records
- **Orders:** 5 records

---

## 🧪 Create Examples

### Create Book
```bash
curl -X POST http://localhost:5000/catalog \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Book",
    "author": "Author Name",
    "isbn": "1234567890123",
    "published_year": 2024,
    "genre": "Fiction",
    "available_copies": 5
  }'
```

### Create User
```bash
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "new@email.com",
    "full_name": "New User",
    "phone": "+1234567890",
    "address": "123 Street"
  }'
```

### Create Order
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

---

## 🔄 Update Examples

### Update Book
```bash
curl -X PUT http://localhost:5000/catalog/1 \
  -H "Content-Type: application/json" \
  -d '{"available_copies": 10}'
```

### Update User
```bash
curl -X PUT http://localhost:5001/users/1 \
  -H "Content-Type: application/json" \
  -d '{"phone": "+9999999999"}'
```

### Update Order
```bash
curl -X PUT http://localhost:8080/orders/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "shipped"}'
```

---

## ❌ Delete Examples

```bash
curl -X DELETE http://localhost:5000/catalog/6
curl -X DELETE http://localhost:5001/users/6
curl -X DELETE http://localhost:8080/orders/6
```

---

## 📚 Documentation Files

- **README.md** - Main documentation
- **ASSIGNMENT_SUMMARY.md** - Project summary
- **ARCHITECTURE.md** - System architecture
- **TESTING_GUIDE.md** - Testing instructions
- **PROJECT_FILES.md** - File structure
- **QUICK_REFERENCE.md** - This file

---

## 🏃 One-Line Quick Test

```bash
curl -s http://localhost:5000/catalog | python -m json.tool && \
curl -s http://localhost:5001/users | python -m json.tool && \
curl -s http://localhost:8080/orders | python -m json.tool
```

---

## 🎯 Common Tasks

### View all books
```bash
curl http://localhost:5000/catalog | python -m json.tool
```

### View all users
```bash
curl http://localhost:5001/users | python -m json.tool
```

### View all orders
```bash
curl http://localhost:8080/orders | python -m json.tool
```

### Check if everything is running
```bash
docker-compose ps
```

### View real-time logs
```bash
docker-compose logs -f
```

---

## ⚡ Performance Tips

- Use `-s` flag with curl for silent mode
- Pipe to `python -m json.tool` for formatted JSON
- Use `docker-compose logs -f <service>` for specific service logs
- Use `docker-compose ps` to quickly check status

---

## 🆘 Emergency Commands

### Everything broken? Reset it all:
```bash
docker-compose down -v
docker-compose up -d --build
sleep 10
curl http://localhost:5000/catalog
```

### Single service broken? Restart it:
```bash
docker-compose restart catalog-service
docker-compose logs -f catalog-service
```

---

## ✅ Quick Verification Checklist

```bash
# 1. Are all containers running?
docker-compose ps

# 2. Are databases healthy?
docker-compose ps | grep healthy

# 3. Can I access all services?
curl http://localhost:5000/
curl http://localhost:5001/
curl http://localhost:8080/

# 4. Can I get data from all services?
curl http://localhost:5000/catalog
curl http://localhost:5001/users
curl http://localhost:8080/orders
```

If all of the above work, your system is operational! ✨
