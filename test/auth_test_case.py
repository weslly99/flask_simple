import os
import unittest

from flask import jsonify

from flask import current_app
from current_app.app import create_app,db
from app.auth.models import User


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        user = User(username='wesllycoliveiras',email='weslly@css.com',password='12345678')
        with self.app.app_context():
            db.create_all()
            db.session.add(user)
            db.seesion.commit()


    def tearDown(self):
        """TearDown all initialized variable"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_api_register(self):
        user = User(username='weslly99',email='weslly99@css.com',password='12345678')
        sent = jsonify(user)
        res = self.client().post('/auth/register',data=sent)
        self.assertEqual(res.status_code,200)

if __name__ == "__main__":
    unittest.main()
