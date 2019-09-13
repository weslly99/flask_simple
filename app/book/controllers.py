from flask import jsonify, request, json

from app import db

from . import book
from .models import Book, book_share_schema, books_share_schema


@book.route('/api/books')
def books():
    items = books_share_schema.dumps(Book.query.all())
    return jsonify(items)


@book.route('/api/books/add', methods=['POST'])
def books_add():
    if request.get_json():
        book = Book.from_json(json.dumps(request.get_json()))
        try:
            db.session.add(book)
            db.session.commit()
        except Exception as err:
            return jsonify({"error":"Erro durante a persistencia"})
        return book_share_schema.dump(Book.query.filter_by(title=book.title).first())
    return jsonify({"error":"Requisição vazia"})

@book.route('/api/books/edit/<int:book_id>', methods=['PUT'])
def books_edit(book_id):
    if request.get_json():
        book = Book.query.get_or_404(book_id)
        book.author = request.json['author']
        book.title = request.json['title']
        book.descr = request.json['description']
        try:
            db.session.add(book)
            db.session.commit()
        except Exception as err:
            return jsonify({"error":"Erro durante a persistencia"})
        return book_share_schema.dump(Book.query.filter_by(id=book.id).first())
    return jsonify({"error","Requisição vazia"})

@book.route('/api/books/delete/<int:book_id>', methods=['DELETE'])
def books_delete(book_id):
    book = Book.query.get_or_404(book_id)
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as err:
        return jsonify({"error":"Erro enquanto deletava o registro"})
    return book_share_schema.dump(book)

@book.route('/api/books/<int:book_id>')
def books_get(book_id):
    book = Book.query.get_or_404(book_id)
    return book_share_schema.dump(book)
    