import unittest

from flask import json, jsonify

from app import create_app, db
from app.book.models import Book, book_share_schema, books_share_schema


class BookTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        book = Book(title="The Art of Computer Programming", author="Donald E. Knuth", description="The bible of all fundamental algorithms")
        book1 = Book(title="Automate the Boring Stuff with Python", author="Al Sweigart", description="You’ll learn how to use Python to write programs that do in minutes what would take you hours to do by hand")
        book2 = Book(title="Learning Python, 5th Edition", author="Mark Lutz", description="Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. ")
        with self.app.app_context():
            db.create_all()
            db.session.add(book)
            db.session.add(book1)
            db.session.add(book2)
            db.session.commit()

    def tearDown(self):
        """TearDown all initialized variable"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_api_list_books(self):
        """Test list of books"""
        with self.app.app_context():
            res = self.client().get("/api/books", content_type="application/json")
            data_dict = json.loads(res.json)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(data_dict), 3)

    def test_api_add_book(self):
        """Test add book"""
        with self.app.app_context():
            sent = {"author":"Allen B. Downey","title":"Think Python: How to Think Like a Computer Scientist", "description":" This hands-on guide takes you through the language a step at a time"}
            res = self.client().post("api/books/add",data=json.dumps(sent),content_type="application/json")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["author"], sent['author'])

    def test_api_edit_book(self):
        """Test Edit Book"""
        with self.app.app_context():
            sent = {"id": 1,"author":"Bjarne Stroustrup", "title":"The C++ Programming Language", "description":"The new C++11 standard allows programmers to express ideas more clearly, simply, and directly, and to write faster, more efficient code."}
            res = self.client().post("api/books/edit", data=json.dumps(sent),content_type="application/json")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json['author'], sent['author'])

    def test_api_delete_book(self):
        pass

if __name__ == "__main__":
    unittest.main()
