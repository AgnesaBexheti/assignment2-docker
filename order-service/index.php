<?php
header('Content-Type: application/json');

// Database connection configuration from environment variables
$db_host = getenv('DB_HOST') ?: 'order-db';
$db_name = getenv('DB_NAME') ?: 'order_db';
$db_user = getenv('DB_USER') ?: 'order_user';
$db_pass = getenv('DB_PASS') ?: 'order_pass';

// Create database connection
function getDbConnection() {
    global $db_host, $db_name, $db_user, $db_pass;

    try {
        $conn = new PDO("mysql:host=$db_host;dbname=$db_name", $db_user, $db_pass);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch(PDOException $e) {
        http_response_code(500);
        echo json_encode([
            'success' => false,
            'error' => 'Database connection failed: ' . $e->getMessage()
        ]);
        exit();
    }
}

// Initialize database
function initDb() {
    global $db_host, $db_user, $db_pass;

    try {
        // Connect without database to create it if needed
        $conn = new PDO("mysql:host=$db_host", $db_user, $db_pass);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Create database if not exists
        global $db_name;
        $conn->exec("CREATE DATABASE IF NOT EXISTS $db_name");
        $conn->exec("USE $db_name");

        // Create orders table
        $conn->exec("CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            book_id INT NOT NULL,
            quantity INT NOT NULL DEFAULT 1,
            status VARCHAR(50) DEFAULT 'pending',
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total_price DECIMAL(10, 2)
        )");

        // Check if table is empty
        $stmt = $conn->query("SELECT COUNT(*) FROM orders");
        $count = $stmt->fetchColumn();

        // Insert sample data if table is empty
        if ($count == 0) {
            $sampleOrders = [
                [1, 1, 2, 'completed', 29.99],
                [2, 2, 1, 'completed', 15.99],
                [1, 3, 3, 'pending', 44.97],
                [3, 4, 1, 'shipped', 12.99],
                [4, 5, 2, 'completed', 31.98]
            ];

            $stmt = $conn->prepare("INSERT INTO orders (user_id, book_id, quantity, status, total_price) VALUES (?, ?, ?, ?, ?)");

            foreach ($sampleOrders as $order) {
                $stmt->execute($order);
            }
        }

        $conn = null;
    } catch(PDOException $e) {
        error_log("Database initialization error: " . $e->getMessage());
    }
}

// Initialize database on first run
initDb();

// Get request method and path
$method = $_SERVER['REQUEST_METHOD'];
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$path = rtrim($path, '/');

// Route handling
if ($path == '' || $path == '/') {
    // Health check endpoint
    echo json_encode([
        'service' => 'Order Service',
        'status' => 'running',
        'endpoints' => ['/orders', '/orders/{id}']
    ]);
    exit();
}

// Handle /orders endpoint
if (preg_match('#^/orders$#', $path)) {
    if ($method == 'GET') {
        // READ: Get all orders
        try {
            $conn = getDbConnection();
            $stmt = $conn->query("SELECT * FROM orders ORDER BY id");
            $orders = $stmt->fetchAll(PDO::FETCH_ASSOC);

            echo json_encode([
                'success' => true,
                'count' => count($orders),
                'orders' => $orders
            ]);
        } catch(PDOException $e) {
            http_response_code(500);
            echo json_encode([
                'success' => false,
                'error' => $e->getMessage()
            ]);
        }
    } elseif ($method == 'POST') {
        // CREATE: Add a new order
        try {
            $data = json_decode(file_get_contents('php://input'), true);

            // Validate required fields
            if (!isset($data['user_id']) || !isset($data['book_id']) || !isset($data['quantity'])) {
                http_response_code(400);
                echo json_encode([
                    'success' => false,
                    'error' => 'Missing required fields: user_id, book_id, quantity'
                ]);
                exit();
            }

            $conn = getDbConnection();
            $stmt = $conn->prepare("INSERT INTO orders (user_id, book_id, quantity, status, total_price) VALUES (?, ?, ?, ?, ?)");

            $stmt->execute([
                $data['user_id'],
                $data['book_id'],
                $data['quantity'],
                $data['status'] ?? 'pending',
                $data['total_price'] ?? 0.00
            ]);

            $orderId = $conn->lastInsertId();

            // Fetch the created order
            $stmt = $conn->prepare("SELECT * FROM orders WHERE id = ?");
            $stmt->execute([$orderId]);
            $newOrder = $stmt->fetch(PDO::FETCH_ASSOC);

            http_response_code(201);
            echo json_encode([
                'success' => true,
                'message' => 'Order created successfully',
                'order' => $newOrder
            ]);
        } catch(PDOException $e) {
            http_response_code(500);
            echo json_encode([
                'success' => false,
                'error' => $e->getMessage()
            ]);
        }
    } else {
        http_response_code(405);
        echo json_encode([
            'success' => false,
            'error' => 'Method not allowed'
        ]);
    }
} elseif (preg_match('#^/orders/(\d+)$#', $path, $matches)) {
    $orderId = $matches[1];

    if ($method == 'GET') {
        // READ: Get a specific order by ID
        try {
            $conn = getDbConnection();
            $stmt = $conn->prepare("SELECT * FROM orders WHERE id = ?");
            $stmt->execute([$orderId]);
            $order = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($order) {
                echo json_encode([
                    'success' => true,
                    'order' => $order
                ]);
            } else {
                http_response_code(404);
                echo json_encode([
                    'success' => false,
                    'error' => 'Order not found'
                ]);
            }
        } catch(PDOException $e) {
            http_response_code(500);
            echo json_encode([
                'success' => false,
                'error' => $e->getMessage()
            ]);
        }
    } elseif ($method == 'PUT') {
        // UPDATE: Update an existing order
        try {
            $data = json_decode(file_get_contents('php://input'), true);

            $conn = getDbConnection();

            // Build dynamic update query
            $updateFields = [];
            $values = [];

            if (isset($data['user_id'])) {
                $updateFields[] = 'user_id = ?';
                $values[] = $data['user_id'];
            }
            if (isset($data['book_id'])) {
                $updateFields[] = 'book_id = ?';
                $values[] = $data['book_id'];
            }
            if (isset($data['quantity'])) {
                $updateFields[] = 'quantity = ?';
                $values[] = $data['quantity'];
            }
            if (isset($data['status'])) {
                $updateFields[] = 'status = ?';
                $values[] = $data['status'];
            }
            if (isset($data['total_price'])) {
                $updateFields[] = 'total_price = ?';
                $values[] = $data['total_price'];
            }

            if (empty($updateFields)) {
                http_response_code(400);
                echo json_encode([
                    'success' => false,
                    'error' => 'No fields to update'
                ]);
                exit();
            }

            $values[] = $orderId;
            $query = "UPDATE orders SET " . implode(', ', $updateFields) . " WHERE id = ?";

            $stmt = $conn->prepare($query);
            $stmt->execute($values);

            if ($stmt->rowCount() > 0) {
                // Fetch the updated order
                $stmt = $conn->prepare("SELECT * FROM orders WHERE id = ?");
                $stmt->execute([$orderId]);
                $updatedOrder = $stmt->fetch(PDO::FETCH_ASSOC);

                echo json_encode([
                    'success' => true,
                    'message' => 'Order updated successfully',
                    'order' => $updatedOrder
                ]);
            } else {
                http_response_code(404);
                echo json_encode([
                    'success' => false,
                    'error' => 'Order not found'
                ]);
            }
        } catch(PDOException $e) {
            http_response_code(500);
            echo json_encode([
                'success' => false,
                'error' => $e->getMessage()
            ]);
        }
    } elseif ($method == 'DELETE') {
        // DELETE: Remove an order
        try {
            $conn = getDbConnection();

            // Fetch order before deleting
            $stmt = $conn->prepare("SELECT * FROM orders WHERE id = ?");
            $stmt->execute([$orderId]);
            $deletedOrder = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($deletedOrder) {
                $stmt = $conn->prepare("DELETE FROM orders WHERE id = ?");
                $stmt->execute([$orderId]);

                echo json_encode([
                    'success' => true,
                    'message' => 'Order deleted successfully',
                    'order' => $deletedOrder
                ]);
            } else {
                http_response_code(404);
                echo json_encode([
                    'success' => false,
                    'error' => 'Order not found'
                ]);
            }
        } catch(PDOException $e) {
            http_response_code(500);
            echo json_encode([
                'success' => false,
                'error' => $e->getMessage()
            ]);
        }
    } else {
        http_response_code(405);
        echo json_encode([
            'success' => false,
            'error' => 'Method not allowed'
        ]);
    }
} else {
    http_response_code(404);
    echo json_encode([
        'success' => false,
        'error' => 'Endpoint not found'
    ]);
}
?>
