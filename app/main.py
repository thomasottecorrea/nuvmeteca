from flask import Flask, jsonify, request
from app.routes.book_routes import book_bp

app = Flask(__name__)
app.register_blueprint(book_bp, url_prefix='/books')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Internal Library Management System!"})

if __name__ == '__main__':
    app.run(debug=True)
