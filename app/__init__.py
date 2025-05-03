from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Marielouise03@localhost:5433/mymoviedb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'

    # Initialisation de la base de données
    db.init_app(app)

    # Enregistrement des routes
    from .routes import register_routes
    register_routes(app)

    return app