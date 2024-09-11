import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text

app = Flask(__name__)
CORS(app)

def load_db_config():
    return {
        'host': os.getenv('DB_HOST', ''),
        'user': os.getenv('DB_USER', ''),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', '')
    }

db_config = load_db_config()
DATABASE_URI = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
engine = create_engine(DATABASE_URI)

@app.route('/add_item', methods=['POST'])
def add_item():
    thing = request.form.get('thing')
    price = request.form.get('price')
    
    if request.method != "POST":
        return jsonify({'message': 'Congratulations, your Flask app running normally'}), 200

    try:
        # Convert price to float
        price = float(price)
    except (ValueError, TypeError):
        return jsonify({'error': 'The "price" field must be a number'}), 400

    if not thing:
        return jsonify({'error': 'The "thing" field is required'}), 400

    try:
        with engine.connect() as connection:
            # Use raw SQL or SQLAlchemy text to execute the query
            query = text("INSERT INTO items (thing, price) VALUES (:thing, :price)")
            connection.execute(query, {'thing': thing, 'price': price})
        
        return jsonify({'message': 'Item added successfully!', 'data': {'thing': thing, 'price': price}}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete_item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        with engine.connect() as connection:
            query = text("DELETE FROM items WHERE id = :item_id")
            result = connection.execute(query, {'item_id': item_id})
        
        if result.rowcount == 0:
            return jsonify({'error': 'Item not found'}), 404
        
        return jsonify({'message': 'Item deleted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2020)

