from flask import jsonify, request

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
        author = request.json['author']
        title = request.json['title']
        descr = request.json['description']
        book = Book(title=title, author=author, description=descr)
        try:
            db.session.add(book)
            db.session.commit()
        except Exception as err:
            return jsonify({"error":"Erro durante a persistencia"})
        return book_share_schema.dump(Book.query.filter_by(title=book.title).first())
    return jsonify({"error":"Requisição vazia"})

@book.route('/api/books/edit', methods=['POST'])
def books_edit():
    if request.get_json():
        id = request.json['id']
        author = request.json['author']
        title = request.json['title']
        descr = request.json['description']
        book = Book(id=id, author=author,title=title,description=descr)
        try:
            db.session.add(book)
            db.session.commit()
        except Exception as err:
            return jsonify({"error":"Erro durante a persistencia"})
        return book_share_schema.dump(Book.query.filter_by(id=book.id).first())
    return jsonify({"error","Requisição vazia"})