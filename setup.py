import os
import shutil
import sys
from typing import Dict

DIRECTORIES = [
    "app",
    "app/api/v1",
    "app/main",
    "app/models",
    "app/services",
    "app/repositories",
    "app/utils",
    "app/extensions",
    "app/config",
    "migrations",
    "tests",
    "static",
    "templates"
]

FILE_CONTENTS = {
    "app/__init__.py": """
from flask import Flask
from app.config.config import config
from app.extensions import database, auth

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    database.init_app(app)
    auth.init_app(app)

    # Register blueprints
    from app.api.v1.routes import api as api_blueprint
    from app.main.views import main as main_blueprint
    
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    app.register_blueprint(main_blueprint)

    return app
    """,
    
    "app/api/__init__.py": """
from flask import Blueprint

api = Blueprint('api', __name__)
from .v1 import routes
    """,
    
    "app/api/v1/__init__.py": """
from flask import Blueprint

api = Blueprint('api_v1', __name__)
from . import routes, controllers, services
    """,
    
    "app/api/v1/routes.py": """
from flask import jsonify
from . import api_v1

@api_v1.route('/status')
def status():
    return jsonify({'status': 'API is running'})
    """,
    
    "app/api/v1/controllers.py": """
# Controllers for API logic
    """,
    
    "app/api/v1/services.py": """
# Business logic for API
    """,
    
    "app/main/__init__.py": """
from flask import Blueprint

main = Blueprint('main', __name__)
from . import views
    """,
    
    "app/main/views.py": """
from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')
    """,
    
    "app/models/__init__.py": """
# Models package
    """,
    
    "app/models/user.py": """
from app.extensions.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    """,
    
    "app/models/transaction.py": """
from app.extensions.database import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    """,
    
    "app/extensions/__init__.py": """
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

database = SQLAlchemy()
auth = LoginManager()
    """,
    
    "wsgi.py": """
from app import create_app

app = create_app('development')

if __name__ == "__main__":
    app.run(debug=True)
    """,
    
    "manage.py": """
from flask_script import Manager
from app import create_app

app = create_app('development')
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
    """,
    
    "README.md": """
# Add your README lines..

```
/project
├── /app
│   ├── /api                    # RESTful API routes
│   │   ├── __init__.py
│   │   └── /v1                 # API versioning
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       ├── controllers.py
│   │       └── services.py
│   ├── /main                   # Web UI routes
│   │   ├── __init__.py
│   │   └── views.py
│   ├── /models                 # Database models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── transaction.py
│   ├── /services              # Business logic
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── transaction_service.py
│   ├── /repositories         # Data access layer
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   └── transaction_repository.py
│   ├── /utils               # Helpers, utilities
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── helpers.py
│   ├── /extensions         # Flask extensions setup
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── auth.py
│   ├── /config            # Configuration management
│   │   ├── __init__.py
│   │   └── config.py
│   └── __init__.py        # App factory
│
├── /migrations           # Flask-Migrate database migrations
├── /tests               # Unit and integration tests
├── /static              # Static files (CSS, JS, images)
├── /templates           # Jinja2 templates for web
├── requirements.txt     # Python dependencies
├── config.py            # App configurations
├── wsgi.py             # Entry point for WSGI servers
├── manage.py           # Script for running commands
└── README.md           # Documentation
```
    """,

    "requirements.txt": """Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Login
Flask-WTF
Flask-CORS
Flask-RESTful
Flask-Script
Flask-JWT-Extended
Flask-Mail
Flask-Limiter
Flask-Caching
Flask-Session
Flask-Talisman
python-dotenv
gunicorn
psycopg2-binary
mysqlclient
bcrypt
"""
}

def create_directories(base_dir: str) -> None:
    for directory in DIRECTORIES:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)

def create_files(base_dir: str) -> None:
    for file_path, contents in FILE_CONTENTS.items():
        with open(os.path.join(base_dir, file_path), 'w', encoding='utf-8') as file:
            file.write(contents.strip())

def create_flask_project(base_dir: str) -> None:
    create_directories(base_dir)
    create_files(base_dir)
    print(f"Flask project structure created successfully in '{base_dir}'!")

def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(__file__)} <project_folder_name>")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    
    if os.path.exists(folder_name):
        response = input('The folder already exists. Overwrite? (Y/n): ').lower()
        if response in ['y', '']:
            print('Overwriting the existing folder...')
            shutil.rmtree(folder_name)
            create_flask_project(folder_name)
        else:
            print('Operation aborted.')
            sys.exit(1)
    else:
        create_flask_project(folder_name)

if __name__ == "__main__":
    main()
