import os
import shutil
import sys
from typing import Dict

FILE_CONTENTS = {
    "app/__init__.py": """
from flask import Flask
from config import config
from .extensions import db, csrf, cors

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    cors.init_app(app)

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

# Usage:
# In script.py or wherever you're creating your app:
# app = create_app('development')
""",
    
    "app/main/__init__.py": """
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views

# Usage:
# This file creates the 'main' blueprint.
# Import views to register routes with this blueprint.
""",

    "app/api/__init__.py": """
from flask import Blueprint

api = Blueprint('api', __name__)

from . import routes

# Usage:
# This file creates the 'api' blueprint.
# Import routes to register API routes with this blueprint.
""",
    
    "config.py": """
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.dirname(__file__), 'dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.dirname(__file__), 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Usage:
# In create_app function:
# app.config.from_object(config[config_name])
# config[config_name].init_app(app)
""",
    
    "requirements.txt": """
flask
flask-sqlalchemy
flask-moment
flask-wtf
pytz
flask-migrate
flask-login
mysqlclient
flask-mail
flask-bootstrap
blueprint
requests
flask-cors

# Usage:
# Install these packages using:
# pip install -r requirements.txt
""",
    
    "script.py": """
from app import create_app

app = create_app('development')

if __name__ == "__main__":
    app.run(debug=True)

# Usage:
# Run this script to start the Flask development server:
# python script.py
""",
    
    "app/extensions.py": """
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

db = SQLAlchemy()
csrf = CSRFProtect()
cors = CORS()

# Usage:
# These extensions are initialized in the create_app function.
# You can import them in your models or views as needed.
""",
    
    "app/main/views.py": """
from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

# Usage:
# These are example routes. Add your own routes and views here.
# You can also split this into multiple files (views, api, etc.) as your app grows.
""",

    "app/api/routes.py": """
from flask import jsonify
from . import api

@api.route('/hello')
def hello():
    return jsonify(message="Hello from the API!")

# Usage:
# These are example API routes. Add your own API routes here.
""",

    "app/models.py": """
from .extensions import db

# Example model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Usage:
# Define your database models here.
# Use them in your views by importing and querying, e.g.:
# from .models import User
# user = User.query.filter_by(username='example').first()
""",

    "migrations/README": """
This directory will contain database migrations.

To set up migrations:
1. from flask_migrate import Migrate
2. In your app/__init__.py, add:
   migrate = Migrate(app, db)
3. Initialize: flask db init
4. Create a migration: flask db migrate -m "Initial migration"
5. Apply the migration: flask db upgrade

For more information, see the Flask-Migrate documentation.
""",

    "tests/test_basics.py": """
import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

# Usage:
# Run tests using:
# python -m unittest discover tests
""",

    "app/templates/index.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome to your Flask App!</h1>
</body>
</html>
""",

    "app/static/style.css": """
/* Add your static CSS styles here */
body {
    font-family: Arial, sans-serif;
}
"""
}

DIRECTORIES = [
    "",
    "app",
    "app/main",
    "app/api",
    "app/templates",
    "app/static",
    "migrations",
    "tests"
]

def create_directories(base_dir: str) -> None:
    """Create the necessary directories for the Flask app."""
    for directory in DIRECTORIES:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)

def create_files(base_dir: str) -> None:
    """Create files with their respective contents."""
    for file_path, contents in FILE_CONTENTS.items():
        with open(os.path.join(base_dir, file_path), 'w') as file:
            file.write(contents.strip())

def create_flask_app_structure(base_dir: str) -> None:
    """Create the entire Flask app structure."""
    create_directories(base_dir)
    create_files(base_dir)
    print(f"Flask app structure created successfully in '{base_dir}'!")

def clear_setup():
    pass
    
def main() -> None:
    """Main function to run the script."""
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(__file__)} <project_folder_name>")
        sys.exit(1)
    
    folder_name = sys.argv[1]

    if os.path.exists(folder_name):
        response = input('The folder already exists. Overwrite? (Y/n): ').lower()
        if response in ['y', '']:
            print('Overwriting the folder...')
            shutil.rmtree(folder_name)
            create_flask_app_structure(folder_name)
        else:
            print('Operation aborted. Please choose a different folder name.')
            sys.exit(1)
    else:
        create_flask_app_structure(folder_name)

if __name__ == "__main__":
    main()
