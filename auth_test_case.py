import os
import unittest

from flask import jsonify, json

from app import create_app, db
from app.auth.models import User, user_share_schema


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        user = User(username='wesllycoliveiras',
                    email='weslly@css.com',
                    password='12345678')
        with self.app.app_context():
            db.create_all()
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        """TearDown all initialized variable"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_api_register(self):
        '''Test register'''
        with self.app.app_context():
            sent = {
                "username": "maria",
                "password": "12345678",
                "email": "maria@test.com"
            }
            res = self.client().post('/api/auth/register',
                                     data=json.dumps(sent),
                                     content_type='application/json')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json['email'], sent['email'])

    def test_api_login_password_fail(self):
        '''Test with wrong password'''
        with self.app.app_context():
            user = User.query.filter_by(id=1).first()
            sent = {'email': user.email, 'password': 'dsafdas'}
            res = self.client().post('/api/auth/login',
                                     data=json.dumps(sent),
                                     content_type='application/json')
            self.assertEqual(res.status_code, 403)
            self.assertEqual(res.json['error'], 'Credenciais invalidas')

    def test_api_login_email_fail(self):
        '''Test with wrong email'''
        with self.app.app_context():
            user = User.query.filter_by(id=1).first()
            sent = {'email': 'testes@fdsal.com', 'password':user.password}
            res = self.client().post('/api/auth/login',
                                    data=json.dumps(sent),
                                    content_type='application/json')
            self.assertEqual(res.status_code, 404)
            
    def test_api_login(self):
        '''Test sucessful login'''
        with self.app.app_context():
            user = User.query.filter_by(id=1).first()
            sent = {'email': user.email, 'password': "12345678"}
            res = self.client().post('/api/auth/login',
                                    data=json.dumps(sent),
                                    content_type='application/json')
            self.assertEqual(res.status_code, 200)
            self.assertTrue(res.json['token'])

    def test_api_list_user(self):
        '''Test get all users'''
        with self.app.app_context():
            res = self.client().get()

if __name__ == "__main__":
    unittest.main()
