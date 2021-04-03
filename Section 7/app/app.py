from flask import Flask
from flask.json import jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, JWTError


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

    from app.security.security import authenticate, identity
    jwt = JWT(app, authenticate, identity) # this enables to call the /auth endpoint

    @app.errorhandler(JWTError)
    def auth_error_handler(err):
        return jsonify({'message': 'Could not authorize. Have you included a valid Authorization header?'}), 400


    @app.before_first_request
    def create_tables():
        db.create_all()

    return app