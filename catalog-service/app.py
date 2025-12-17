from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

# Database connection configuration from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'catalog-db'),
    'database': os.getenv('DB_NAME', 'catalog_db'),
    'user': os.getenv('DB_USER', 'catalog_user'),
    'password': os.getenv('DB_PASS', 'catalog_pass')
}

def get_db_connection():
    """Create a database connection"""
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def init_db():
    """Initialize the database with books table"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create books table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            isbn VARCHAR(13) UNIQUE NOT NULL,
            published_year INTEGER,
            genre VARCHAR(100),
            available_copies INTEGER DEFAULT 0
        )
    ''')

    # Insert some sample data if table is empty
    cursor.execute('SELECT COUNT(*) FROM books')
    if cursor.fetchone()[0] == 0:
        sample_books = [
            ('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 'Fiction', 5),
            ('To Kill a Mockingbird', 'Harper Lee', '9780061120084', 1960, 'Fiction', 3),
            ('1984', 'George Orwell', '9780451524935', 1949, 'Dystopian', 4),
            ('Pride and Prejudice', 'Jane Austen', '9780141439518', 1813, 'Romance', 2),
            ('The Hobbit', 'J.R.R. Tolkien', '9780547928227', 1937, 'Fantasy', 6)
        ]

        cursor.executemany('''
            INSERT INTO books (title, author, isbn, published_year, genre, available_copies)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', sample_books)

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'service': 'Catalog Service',
        'status': 'running',
        'endpoints': ['/catalog', '/catalog/<id>']
    })

@app.route('/catalog', methods=['GET'])
def get_books():
    """READ: Get all books"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('SELECT * FROM books ORDER BY id')
        books = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'count': len(books),
            'books': books
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/catalog/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """READ: Get a specific book by ID"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('SELECT * FROM books WHERE id = %s', (book_id,))
        book = cursor.fetchone()
        cursor.close()
        conn.close()

        if book:
            return jsonify({
                'success': True,
                'book': book
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Book not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/catalog', methods=['POST'])
def create_book():
    """CREATE: Add a new book"""
    try:
        data = request.get_json()

        required_fields = ['title', 'author', 'isbn']
        if not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'error': 'Missing required fields: title, author, isbn'
            }), 400

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute('''
            INSERT INTO books (title, author, isbn, published_year, genre, available_copies)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING *
        ''', (
            data['title'],
            data['author'],
            data['isbn'],
            data.get('published_year'),
            data.get('genre'),
            data.get('available_copies', 0)
        ))

        new_book = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'message': 'Book created successfully',
            'book': new_book
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/catalog/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """UPDATE: Update an existing book"""
    try:
        data = request.get_json()

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Build dynamic update query
        update_fields = []
        values = []

        if 'title' in data:
            update_fields.append('title = %s')
            values.append(data['title'])
        if 'author' in data:
            update_fields.append('author = %s')
            values.append(data['author'])
        if 'isbn' in data:
            update_fields.append('isbn = %s')
            values.append(data['isbn'])
        if 'published_year' in data:
            update_fields.append('published_year = %s')
            values.append(data['published_year'])
        if 'genre' in data:
            update_fields.append('genre = %s')
            values.append(data['genre'])
        if 'available_copies' in data:
            update_fields.append('available_copies = %s')
            values.append(data['available_copies'])

        if not update_fields:
            return jsonify({
                'success': False,
                'error': 'No fields to update'
            }), 400

        values.append(book_id)
        query = f"UPDATE books SET {', '.join(update_fields)} WHERE id = %s RETURNING *"

        cursor.execute(query, values)
        updated_book = cursor.fetchone()

        if updated_book:
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({
                'success': True,
                'message': 'Book updated successfully',
                'book': updated_book
            }), 200
        else:
            cursor.close()
            conn.close()
            return jsonify({
                'success': False,
                'error': 'Book not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/catalog/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """DELETE: Remove a book"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute('DELETE FROM books WHERE id = %s RETURNING *', (book_id,))
        deleted_book = cursor.fetchone()

        if deleted_book:
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({
                'success': True,
                'message': 'Book deleted successfully',
                'book': deleted_book
            }), 200
        else:
            cursor.close()
            conn.close()
            return jsonify({
                'success': False,
                'error': 'Book not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
