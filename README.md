# Flask App Structure Template

This bad boy creates for you a template to start creating modular && maintainable flask applications...

## File structure

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

## File system

### Core app (`/app`)
- **api**: RESTful API endpoints with versioning support
- **main**: Web interface routes and views
- **models**: Database model definitions
- **services**: Business logic implementation
- **repositories**: Data access layer for database operations
- **utils**: Helper functions and utilities
- **extensions**: Flask extension configurations
- **config**: Application configuration management

### Dev support modules
- **migrations**: Database migration scripts
- **tests**: Application test suite
- **static**: Static asset files
- **templates**: HTML templates
- **requirements.txt**: Project dependencies
- **config.py**: Configuration settings
- **wsgi.py**: WSGI server entry point
- **manage.py**: Management commands
- **README.md**: Project documentation
