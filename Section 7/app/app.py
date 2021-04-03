from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    
    api = Api(app)
    
    from app.resources.item import Item, ItemList
    from app.resources.store import Store, StoreList
    from app.resources.user import UserRegister

    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(StoreList, '/stores')
    api.add_resource(UserRegister, '/register')

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app