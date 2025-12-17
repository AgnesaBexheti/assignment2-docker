#!/bin/bash

# Quick test script - No pauses, good for screenshots

echo "========================================="
echo " ONLINE LIBRARY - COMPLETE CRUD TESTING"
echo "========================================="
echo ""

echo "=== DOCKER STATUS ==="
docker-compose ps
echo ""

echo "=== CATALOG: READ ALL ==="
curl -s http://localhost:5000/catalog | python -m json.tool
echo ""

echo "=== CATALOG: READ ONE (ID:1) ==="
curl -s http://localhost:5000/catalog/1 | python -m json.tool
echo ""

echo "=== CATALOG: CREATE ==="
curl -s -X POST http://localhost:5000/catalog \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin","isbn":"9780132350884","published_year":2008,"genre":"Technology","available_copies":10}' \
  | python -m json.tool
echo ""

echo "=== CATALOG: UPDATE (ID:6) ==="
curl -s -X PUT http://localhost:5000/catalog/6 \
  -H "Content-Type: application/json" \
  -d '{"available_copies":20}' \
  | python -m json.tool
echo ""

echo "=== CATALOG: DELETE (ID:6) ==="
curl -s -X DELETE http://localhost:5000/catalog/6 | python -m json.tool
echo ""

echo "=== USER: READ ALL ==="
curl -s http://localhost:5001/users | python -m json.tool
echo ""

echo "=== USER: READ ONE (ID:1) ==="
curl -s http://localhost:5001/users/1 | python -m json.tool
echo ""

echo "=== USER: CREATE ==="
curl -s -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{"username":"test_user","email":"test@example.com","full_name":"Test User","phone":"+1555000000","address":"456 Test Ave"}' \
  | python -m json.tool
echo ""

echo "=== USER: UPDATE (ID:6) ==="
curl -s -X PUT http://localhost:5001/users/6 \
  -H "Content-Type: application/json" \
  -d '{"phone":"+1999999999"}' \
  | python -m json.tool
echo ""

echo "=== USER: DELETE (ID:6) ==="
curl -s -X DELETE http://localhost:5001/users/6 | python -m json.tool
echo ""

echo "=== ORDER: READ ALL ==="
curl -s http://localhost:8080/orders | python -m json.tool
echo ""

echo "=== ORDER: READ ONE (ID:1) ==="
curl -s http://localhost:8080/orders/1 | python -m json.tool
echo ""

echo "=== ORDER: CREATE ==="
curl -s -X POST http://localhost:8080/orders \
  -H "Content-Type: application/json" \
  -d '{"user_id":2,"book_id":3,"quantity":5,"status":"pending","total_price":99.95}' \
  | python -m json.tool
echo ""

echo "=== ORDER: UPDATE (ID:6) ==="
curl -s -X PUT http://localhost:8080/orders/6 \
  -H "Content-Type: application/json" \
  -d '{"status":"shipped"}' \
  | python -m json.tool
echo ""

echo "=== ORDER: DELETE (ID:6) ==="
curl -s -X DELETE http://localhost:8080/orders/6 | python -m json.tool
echo ""

echo "========================================="
echo " ALL 15 CRUD TESTS COMPLETED!"
echo "========================================="
