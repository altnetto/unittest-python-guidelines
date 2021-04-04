from unittest import TestCase
from app.app import create_app, db


class BaseTest(TestCase):
    '''
    The setUpClass enables to set things inside it just one time, 
    while the setUp method enables the setting to be at each test call
    '''
    @classmethod
    def setUpClass(cls):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


    def setUp(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.create_all()

        self.app = app.test_client
        self.app_context = app.app_context


    def tearDown(self):
        with self.app_context():
            db.session.remove()
            db.drop_all()