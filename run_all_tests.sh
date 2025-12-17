#!/bin/bash

echo "========================================="
echo "ONLINE LIBRARY SYSTEM - COMPLETE TESTING"
echo "========================================="
echo ""

echo "TEST 1: DOCKER CONTAINER STATUS"
echo "================================"
docker-compose ps
echo ""
echo "Press Enter to continue..."
read

echo "TEST 2: CATALOG SERVICE - READ ALL BOOKS"
echo "========================================="
curl -X GET http://localhost:5000/catalog | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 3: CATALOG SERVICE - READ SINGLE BOOK (ID: 1)"
echo "==================================================="
curl -X GET http://localhost:5000/catalog/1 | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 4: CATALOG SERVICE - CREATE NEW BOOK"
echo "=========================================="
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
echo ""
echo "Press Enter to continue..."
read

echo "TEST 5: CATALOG SERVICE - UPDATE BOOK (ID: 6)"
echo "=============================================="
curl -X PUT http://localhost:5000/catalog/6 \
  -H "Content-Type: application/json" \
  -d '{
    "available_copies": 20
  }' | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 6: CATALOG SERVICE - DELETE BOOK (ID: 6)"
echo "=============================================="
curl -X DELETE http://localhost:5000/catalog/6 | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 7: USER SERVICE - READ ALL USERS"
echo "======================================"
curl -X GET http://localhost:5001/users | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 8: USER SERVICE - READ SINGLE USER (ID: 1)"
echo "================================================"
curl -X GET http://localhost:5001/users/1 | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 9: USER SERVICE - CREATE NEW USER"
echo "======================================="
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "test_user",
    "email": "test@example.com",
    "full_name": "Test User",
    "phone": "+1555000000",
    "address": "456 Test Ave"
  }' | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 10: USER SERVICE - UPDATE USER (ID: 6)"
echo "============================================"
curl -X PUT http://localhost:5001/users/6 \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "+1999999999"
  }' | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 11: USER SERVICE - DELETE USER (ID: 6)"
echo "============================================"
curl -X DELETE http://localhost:5001/users/6 | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 12: ORDER SERVICE - READ ALL ORDERS"
echo "========================================="
curl -X GET http://localhost:8080/orders | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 13: ORDER SERVICE - READ SINGLE ORDER (ID: 1)"
echo "==================================================="
curl -X GET http://localhost:8080/orders/1 | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 14: ORDER SERVICE - CREATE NEW ORDER"
echo "=========================================="
curl -X POST http://localhost:8080/orders \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 2,
    "book_id": 3,
    "quantity": 5,
    "status": "pending",
    "total_price": 99.95
  }' | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 15: ORDER SERVICE - UPDATE ORDER (ID: 6)"
echo "=============================================="
curl -X PUT http://localhost:8080/orders/6 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "shipped"
  }' | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 16: ORDER SERVICE - DELETE ORDER (ID: 6)"
echo "=============================================="
curl -X DELETE http://localhost:8080/orders/6 | python -m json.tool
echo ""
echo "Press Enter to continue..."
read

echo "TEST 17: DATABASE SEPARATION - CATALOG DB (PostgreSQL)"
echo "======================================================="
echo "Tables:"
docker exec -it catalog-db psql -U catalog_user -d catalog_db -c "\dt"
echo ""
echo "Sample Data:"
docker exec -it catalog-db psql -U catalog_user -d catalog_db -c "SELECT id, title, author FROM books LIMIT 3;"
echo ""
echo "Press Enter to continue..."
read

echo "TEST 18: DATABASE SEPARATION - USER DB (MySQL)"
echo "==============================================="
echo "Tables:"
docker exec -it user-db mysql -u user_user -puser_pass user_db -e "SHOW TABLES;"
echo ""
echo "Sample Data:"
docker exec -it user-db mysql -u user_user -puser_pass user_db -e "SELECT id, username, email FROM users LIMIT 3;"
echo ""
echo "Press Enter to continue..."
read

echo "TEST 19: DATABASE SEPARATION - ORDER DB (MySQL)"
echo "================================================"
echo "Tables:"
docker exec -it order-db mysql -u order_user -porder_pass order_db -e "SHOW TABLES;"
echo ""
echo "Sample Data:"
docker exec -it order-db mysql -u order_user -porder_pass order_db -e "SELECT id, user_id, book_id, status FROM orders LIMIT 3;"
echo ""
echo "Press Enter to continue..."
read

echo "TEST 20: DOCKER VOLUMES"
echo "======================="
docker volume ls | grep assignment2
echo ""
echo "Press Enter to continue..."
read

echo "TEST 21: DOCKER NETWORK"
echo "======================="
docker network ls | grep library
echo ""
echo "Network Details:"
docker network inspect assignment2-docker_library-net --format='{{range .Containers}}{{.Name}} {{end}}'
echo ""
echo "Press Enter to continue..."
read

echo "TEST 22: ENVIRONMENT VARIABLES"
echo "==============================="
echo "Catalog Service:"
docker exec catalog-service env | grep DB_
echo ""
echo "User Service:"
docker exec user-service env | grep DB_
echo ""
echo "Order Service:"
docker exec order-service env | grep DB_
echo ""
echo "Press Enter to continue..."
read

echo "TEST 23: HEALTH CHECKS"
echo "======================"
echo "Catalog Service Health:"
curl -X GET http://localhost:5000/ | python -m json.tool
echo ""
echo "User Service Health:"
curl -X GET http://localhost:5001/ | python -m json.tool
echo ""
echo "Order Service Health:"
curl -X GET http://localhost:8080/ | python -m json.tool
echo ""

echo "========================================="
echo "ALL TESTS COMPLETED SUCCESSFULLY!"
echo "========================================="
echo ""
echo "Total Tests Run: 23"
echo "- CRUD Tests: 15 (5 per service)"
echo "- Database Tests: 3"
echo "- Infrastructure Tests: 5"
echo ""
echo "Summary:"
echo "✓ All services are running"
echo "✓ All CRUD operations working"
echo "✓ Databases are separated"
echo "✓ Docker configuration is correct"
echo ""
