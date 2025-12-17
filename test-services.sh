#!/bin/bash

echo "========================================="
echo "Online Library System - Service Tests"
echo "========================================="
echo ""

echo "1. Testing Catalog Service (Port 5000)..."
echo "-------------------------------------------"
echo "Health Check:"
curl -s http://localhost:5000/ | python -m json.tool
echo ""
echo "All Books:"
curl -s http://localhost:5000/catalog | python -m json.tool
echo ""
echo "Single Book (ID: 1):"
curl -s http://localhost:5000/catalog/1 | python -m json.tool
echo ""

echo "2. Testing User Service (Port 5001)..."
echo "-------------------------------------------"
echo "Health Check:"
curl -s http://localhost:5001/ | python -m json.tool
echo ""
echo "All Users:"
curl -s http://localhost:5001/users | python -m json.tool
echo ""
echo "Single User (ID: 1):"
curl -s http://localhost:5001/users/1 | python -m json.tool
echo ""

echo "3. Testing Order Service (Port 8080)..."
echo "-------------------------------------------"
echo "Health Check:"
curl -s http://localhost:8080/ | python -m json.tool
echo ""
echo "All Orders:"
curl -s http://localhost:8080/orders | python -m json.tool
echo ""
echo "Single Order (ID: 1):"
curl -s http://localhost:8080/orders/1 | python -m json.tool
echo ""

echo "========================================="
echo "All tests completed!"
echo "========================================="
