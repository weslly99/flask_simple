from flask import json

from app import db, ma


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(84), nullable=False)
    description = db.Column(db.String(128), nullable=True)

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

    @classmethod
    def from_json(cls, book_json: str) -> 'Book':
        book = json.loads(book_json)
        return cls(title=book['title'],
                   author=book['author'],
                   description=book['description'])

    def __repr__(self):
        return f"<Book : {self.title}"


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'description')


book_share_schema = BookSchema()
books_share_schema = BookSchema(many=True)
