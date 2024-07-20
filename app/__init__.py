from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import models here
    from .models import item  # Adjust this import based on your actual model files

    api = Api(app)
   
    # Initialize routes
    from .resources.item import ItemResource, ItemListResource
    from .services.api_routes import initialize_routes

    api.add_resource(ItemResource, '/items/<int:item_id>')
    api.add_resource(ItemListResource, '/items')
    initialize_routes(api)

    return app