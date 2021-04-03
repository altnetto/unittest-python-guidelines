from unittest import TestCase
from app.app import create_app, db


class BaseTest(TestCase):
    def setUp(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.create_all()

        self.app = app.test_client()
        self.app_context = app.app_context


    def tearDown(self):
        with self.app_context():
            db.session.remove()
            db.drop_all()