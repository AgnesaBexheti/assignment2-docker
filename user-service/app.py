from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

# Database connection configuration from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'user-db'),
    'database': os.getenv('DB_NAME', 'user_db'),
    'user': os.getenv('DB_USER', 'user_user'),
    'password': os.getenv('DB_PASS', 'user_pass')
}

def get_db_connection():
    """Create a database connection"""
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

def init_db():
    """Initialize the database with users table"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            full_name VARCHAR(255) NOT NULL,
            phone VARCHAR(20),
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Insert some sample data if table is empty
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    if count == 0:
        sample_users = [
            ('john_doe', 'john.doe@email.com', 'John Doe', '+1234567890', '123 Main St, City, State'),
            ('jane_smith', 'jane.smith@email.com', 'Jane Smith', '+1987654321', '456 Oak Ave, Town, State'),
            ('bob_wilson', 'bob.wilson@email.com', 'Bob Wilson', '+1555123456', '789 Pine Rd, Village, State'),
            ('alice_brown', 'alice.brown@email.com', 'Alice Brown', '+1555987654', '321 Elm St, City, State'),
            ('charlie_davis', 'charlie.davis@email.com', 'Charlie Davis', '+1555456789', '654 Maple Dr, Town, State')
        ]

        cursor.executemany('''
            INSERT INTO users (username, email, full_name, phone, address)
            VALUES (%s, %s, %s, %s, %s)
        ''', sample_users)

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'service': 'User Service',
        'status': 'running',
        'endpoints': ['/users', '/users/<id>']
    })

@app.route('/users', methods=['GET'])
def get_users():
    """READ: Get all users"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users ORDER BY id')
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'count': len(users),
            'users': users
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """READ: Get a specific user by ID"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return jsonify({
                'success': True,
                'user': user
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/users', methods=['POST'])
def create_user():
    """CREATE: Add a new user"""
    try:
        data = request.get_json()

        required_fields = ['username', 'email', 'full_name']
        if not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'error': 'Missing required fields: username, email, full_name'
            }), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('''
            INSERT INTO users (username, email, full_name, phone, address)
            VALUES (%s, %s, %s, %s, %s)
        ''', (
            data['username'],
            data['email'],
            data['full_name'],
            data.get('phone'),
            data.get('address')
        ))

        user_id = cursor.lastrowid
        conn.commit()

        # Fetch the created user
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        new_user = cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'message': 'User created successfully',
            'user': new_user
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """UPDATE: Update an existing user"""
    try:
        data = request.get_json()

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Build dynamic update query
        update_fields = []
        values = []

        if 'username' in data:
            update_fields.append('username = %s')
            values.append(data['username'])
        if 'email' in data:
            update_fields.append('email = %s')
            values.append(data['email'])
        if 'full_name' in data:
            update_fields.append('full_name = %s')
            values.append(data['full_name'])
        if 'phone' in data:
            update_fields.append('phone = %s')
            values.append(data['phone'])
        if 'address' in data:
            update_fields.append('address = %s')
            values.append(data['address'])

        if not update_fields:
            return jsonify({
                'success': False,
                'error': 'No fields to update'
            }), 400

        values.append(user_id)
        query = f"UPDATE users SET {', '.join(update_fields)} WHERE id = %s"

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            # Fetch the updated user
            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            updated_user = cursor.fetchone()
            cursor.close()
            conn.close()

            return jsonify({
                'success': True,
                'message': 'User updated successfully',
                'user': updated_user
            }), 200
        else:
            cursor.close()
            conn.close()
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """DELETE: Remove a user"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Fetch user before deleting
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        deleted_user = cursor.fetchone()

        if deleted_user:
            cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({
                'success': True,
                'message': 'User deleted successfully',
                'user': deleted_user
            }), 200
        else:
            cursor.close()
            conn.close()
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)
