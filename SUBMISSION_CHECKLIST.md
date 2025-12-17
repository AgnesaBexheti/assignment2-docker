# Assignment Submission Checklist

## 📋 Complete Submission Package

### ✅ **Step 1: Ensure All Services Are Running**

```bash
# Start all services
docker-compose up -d --build

# Verify all containers are up
docker-compose ps
```

**Expected:** 6 containers running (3 services + 3 databases, all healthy)

---

## 📸 **Step 2: Capture Required Screenshots**

### Category 1: Docker Configuration (60% - Most Important!)

#### Screenshot 1: Docker Compose Status
```bash
docker-compose ps
```
**Shows:** All 6 containers with status "Up" and databases showing "healthy"

#### Screenshot 2: Docker Volumes
```bash
docker volume ls | grep assignment2
```
**Shows:** 3 persistent volumes (catalog-data, user-data, order-data)

#### Screenshot 3: Docker Network
```bash
docker network ls | grep library
docker network inspect assignment2-docker_library-net
```
**Shows:** library-net network with all containers connected

#### Screenshot 4: docker-compose.yml File
**Shows:** Your complete docker-compose.yml configuration

#### Screenshot 5: Dockerfiles
**Shows:** All three Dockerfile contents (can be 3 separate screenshots)

---

### Category 2: Database Separation (25% - Critical!)

#### Screenshot 6: Catalog Database (PostgreSQL)
```bash
docker exec -it catalog-db psql -U catalog_user -d catalog_db -c "\dt"
docker exec -it catalog-db psql -U catalog_user -d catalog_db -c "SELECT * FROM books LIMIT 3;"
```
**Shows:** PostgreSQL with books table and sample data

#### Screenshot 7: User Database (MySQL)
```bash
docker exec -it user-db mysql -u user_user -puser_pass user_db -e "SHOW TABLES;"
docker exec -it user-db mysql -u user_user -puser_pass user_db -e "SELECT * FROM users LIMIT 3;"
```
**Shows:** MySQL with users table and sample data

#### Screenshot 8: Order Database (MySQL)
```bash
docker exec -it order-db mysql -u order_user -porder_pass order_db -e "SHOW TABLES;"
docker exec -it order-db mysql -u order_user -porder_pass order_db -e "SELECT * FROM orders LIMIT 3;"
```
**Shows:** MySQL with orders table and sample data

#### Screenshot 9: Environment Variables (Different per service)
```bash
docker exec catalog-service env | grep DB_
docker exec user-service env | grep DB_
docker exec order-service env | grep DB_
```
**Shows:** Each service has unique database credentials

---

### Category 3: CRUD Functionality (10%)

You can use either **curl** or **Postman**. Postman is easier for screenshots!

#### Catalog Service CRUD (5 screenshots):

**Screenshot 10: READ All Books**
```bash
curl http://localhost:5000/catalog
```
OR use Postman: `GET http://localhost:5000/catalog`

**Screenshot 11: READ Single Book**
```bash
curl http://localhost:5000/catalog/1
```

**Screenshot 12: CREATE Book**
```bash
curl -X POST http://localhost:5000/catalog \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin","isbn":"9780132350884","published_year":2008,"genre":"Technology","available_copies":10}'
```

**Screenshot 13: UPDATE Book**
```bash
curl -X PUT http://localhost:5000/catalog/6 \
  -H "Content-Type: application/json" \
  -d '{"available_copies":20}'
```

**Screenshot 14: DELETE Book**
```bash
curl -X DELETE http://localhost:5000/catalog/6
```

#### User Service CRUD (5 screenshots):

**Screenshot 15-19:** Same pattern as Catalog for User Service
- READ All: `GET http://localhost:5001/users`
- READ One: `GET http://localhost:5001/users/1`
- CREATE: `POST http://localhost:5001/users`
- UPDATE: `PUT http://localhost:5001/users/6`
- DELETE: `DELETE http://localhost:5001/users/6`

#### Order Service CRUD (5 screenshots):

**Screenshot 20-24:** Same pattern for Order Service
- READ All: `GET http://localhost:8080/orders`
- READ One: `GET http://localhost:8080/orders/1`
- CREATE: `POST http://localhost:8080/orders`
- UPDATE: `PUT http://localhost:8080/orders/6`
- DELETE: `DELETE http://localhost:8080/orders/6`

---

### Category 4: Documentation (5%)

#### Screenshot 25: Project Structure
```bash
ls -la
tree -L 2
```
**Shows:** Complete file structure

#### Screenshot 26: README.md
**Shows:** Your documentation file (can take screenshot of the file itself)

---

## 📁 **Step 3: Prepare Files for Submission**

### Required Files:

#### Source Code Files:
- [ ] `catalog-service/app.py`
- [ ] `catalog-service/Dockerfile`
- [ ] `catalog-service/requirements.txt`
- [ ] `user-service/app.py`
- [ ] `user-service/Dockerfile`
- [ ] `user-service/requirements.txt`
- [ ] `order-service/index.php`
- [ ] `order-service/Dockerfile`
- [ ] `order-service/.htaccess`
- [ ] `docker-compose.yml`
- [ ] `.gitignore`

#### Documentation Files:
- [ ] `README.md`
- [ ] `ASSIGNMENT_SUMMARY.md`
- [ ] `ARCHITECTURE.md`
- [ ] `TESTING_GUIDE.md`
- [ ] `PROJECT_FILES.md`
- [ ] `QUICK_REFERENCE.md`
- [ ] `TESTING_EVIDENCE.md`
- [ ] `SUBMISSION_CHECKLIST.md` (this file)

#### Testing Files:
- [ ] `test-services.sh`
- [ ] `run_all_tests.sh`
- [ ] `quick_test.sh`
- [ ] `Postman_Collection.json` (optional but helpful)

---

## 🚀 **Step 4: Quick Testing Methods**

### Method 1: Using Provided Test Scripts

```bash
# Make scripts executable
chmod +x *.sh

# Run quick test (all at once)
bash quick_test.sh

# OR run interactive test (pause between each test)
bash run_all_tests.sh
```

### Method 2: Using Postman (RECOMMENDED for Screenshots!)

1. Open Postman
2. Import → Upload Files → Select `Postman_Collection.json`
3. You'll see 3 folders: Catalog Service, User Service, Order Service
4. Click each request and click "Send"
5. Take screenshots of the responses
6. Much cleaner than curl output!

### Method 3: Manual curl Commands

Use the commands in `TESTING_EVIDENCE.md` one by one.

---

## 📊 **Evaluation Criteria Mapping**

### 60% - Docker and Microservice Configurations
**What to submit:**
- ✅ Screenshot of all containers running (`docker-compose ps`)
- ✅ docker-compose.yml file content
- ✅ All 3 Dockerfiles
- ✅ Screenshot of Docker volumes
- ✅ Screenshot of Docker network
- ✅ Screenshot showing services are accessible

### 25% - Database Separation
**What to submit:**
- ✅ Screenshot of PostgreSQL database (catalog)
- ✅ Screenshot of MySQL database (user)
- ✅ Screenshot of MySQL database (order)
- ✅ Screenshot showing different environment variables per service
- ✅ Screenshot showing different database credentials

### 10% - CRUD Functionality
**What to submit:**
- ✅ 5 screenshots per service (Create, Read All, Read One, Update, Delete)
- ✅ Total: 15 CRUD operation screenshots
- ✅ Show successful responses with status codes

### 5% - Documentation
**What to submit:**
- ✅ README.md file
- ✅ Comments in code
- ✅ Clear API endpoint documentation
- ✅ Setup instructions

---

## 📦 **Step 5: Create Submission Package**

### Option A: ZIP File

```bash
# Create a ZIP file with everything
zip -r OnlineLibrary_Submission.zip . -x "*.git*" -x "*__pycache__*" -x "*.pyc"
```

### Option B: Folder Structure

Create a folder named: `YourName_Assignment2_OnlineLibrary`

```
YourName_Assignment2_OnlineLibrary/
├── source_code/
│   ├── catalog-service/
│   ├── user-service/
│   ├── order-service/
│   └── docker-compose.yml
├── documentation/
│   ├── README.md
│   ├── ASSIGNMENT_SUMMARY.md
│   └── ... (all .md files)
├── screenshots/
│   ├── 01_docker_status.png
│   ├── 02_volumes.png
│   ├── 03_network.png
│   ├── ... (all screenshots)
│   └── README.txt (explaining each screenshot)
└── testing/
    ├── Postman_Collection.json
    ├── test-services.sh
    └── TESTING_EVIDENCE.md
```

---

## ✅ **Final Checklist Before Submission**

### Pre-Submission Verification:

- [ ] All 6 containers are running
- [ ] All databases show "healthy" status
- [ ] All 15 CRUD operations tested and working
- [ ] At least 25 screenshots captured
- [ ] All source code files included
- [ ] Documentation is complete and clear
- [ ] docker-compose.yml is included
- [ ] All Dockerfiles are included
- [ ] Test scripts are included
- [ ] Postman collection is included (optional)

### Screenshot Quality Check:

- [ ] Screenshots are clear and readable
- [ ] Terminal text is visible
- [ ] JSON responses are properly formatted
- [ ] Each screenshot is labeled/numbered
- [ ] Screenshots show successful operations (200, 201 status codes)

### Code Quality Check:

- [ ] Code has comments explaining key sections
- [ ] Environment variables are properly used
- [ ] Error handling is implemented
- [ ] Sample data is pre-loaded

### Documentation Check:

- [ ] README explains how to run the project
- [ ] API endpoints are documented
- [ ] Database schemas are described
- [ ] Architecture is explained
- [ ] Testing instructions are provided

---

## 🎯 **Quick Screenshot Session Guide**

**Time needed:** ~20 minutes

1. **Minutes 0-5: Docker Configuration**
   - Run `docker-compose ps` → Screenshot
   - Run `docker volume ls` → Screenshot
   - Run `docker network inspect` → Screenshot
   - Take screenshots of docker-compose.yml and Dockerfiles

2. **Minutes 5-10: Database Separation**
   - Connect to catalog-db → Screenshot
   - Connect to user-db → Screenshot
   - Connect to order-db → Screenshot
   - Show environment variables → Screenshot

3. **Minutes 10-20: CRUD Operations**
   - Open Postman
   - Import collection
   - Run all 15 CRUD operations
   - Screenshot each successful response

Done! ✅

---

## 💡 **Pro Tips**

1. **Use Postman** - Much cleaner screenshots than curl
2. **Number your screenshots** - Makes organization easier
3. **Create a README in screenshots folder** - Explain what each shows
4. **Test everything twice** - Make sure it all works before screenshotting
5. **Keep terminal window large** - Makes text readable in screenshots
6. **Use light theme** - Easier to read in printed documents
7. **Include URL in Postman screenshots** - Shows which endpoint is being tested

---

## 📧 **What to Submit**

### Minimum Required:
1. **Source Code** - All files listed above
2. **Screenshots** - At least 25 screenshots showing:
   - Docker configuration (6 screenshots)
   - Database separation (4 screenshots)
   - CRUD operations (15 screenshots)
3. **Documentation** - At least README.md

### Recommended:
- All of the above PLUS:
  - ASSIGNMENT_SUMMARY.md
  - ARCHITECTURE.md
  - TESTING_GUIDE.md
  - Postman collection
  - Test scripts

---

## 🆘 **Troubleshooting**

### Services won't start?
```bash
docker-compose down -v
docker-compose up -d --build
```

### Need to regenerate sample data?
```bash
docker-compose down -v  # This deletes all data
docker-compose up -d --build  # Fresh start with sample data
```

### Screenshots are blurry?
- Increase terminal font size
- Use full screen terminal
- Save as PNG, not JPG

---

## ✨ **You're Ready to Submit!**

Good luck with your submission! 🚀

If you followed this checklist, you should have:
- ✅ Complete working microservices system
- ✅ All required screenshots
- ✅ Comprehensive documentation
- ✅ Evidence of CRUD functionality
- ✅ Proof of database separation
- ✅ Professional presentation

**Estimated Grade Potential:** 95-100% if all items completed! 🎉
