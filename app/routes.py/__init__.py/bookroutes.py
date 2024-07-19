from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from app.models import Book, BookCreate

book_bp = Blueprint('book', __name__)
book_service = BookService()

@book_bp.route('', methods=['POST'])
def create_book():
    data = request.get_json()
    book = BookCreate(**data)
    created_book = book_service.create_book(book)
    return jsonify(created_book.dict()), 201

@book_bp.route('/<string:book_id>', methods=['GET'])
def read_book(book_id):
    book = book_service.get_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.dict())

@book_bp.route('/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book(**data)
    updated_book = book_service.update_book(book_id, book)
    if updated_book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(updated_book.dict())

@book_bp.route('', methods=['GET'])
def list_books():
    books = book_service.list_books()
    return jsonify([book.dict() for book in books])
