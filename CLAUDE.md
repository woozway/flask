# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Flask learning repository containing multiple independent Flask applications organized by complexity level. Each application demonstrates different Flask concepts and patterns. The applications are NOT meant to run together - they are separate educational examples.

## Repository Structure

The repository contains three main learning tracks:

1. **Introduction to Flask/** - Basic Flask concepts
   - `Introduction to Flask/Adopt a Pet/` - Simple routing and templates
   - `Jinja2 Templates and Forms/Tourist Attractions/` - Template inheritance and WTForms

2. **Introduction to SQL and Databases for Back-End Web Apps/**
   - `Databases in Flask/FlaskFM/` - SQLAlchemy integration with music playlist models

3. **Advanced Flask Functionality/**
   - `Accounts and Authentication/Travel Sites/` - Full authentication system with Flask-Login

## Running Applications

Each application is self-contained in its own directory. To run an application:

```bash
# Navigate to the specific application directory
cd "Advanced Flask Functionality/Accounts and Authentication/Travel Sites"

# Set Flask environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Run the application
flask run
```

The application will typically run on `http://127.0.0.1:5000/`

## Database Operations

For applications using SQLAlchemy (FlaskFM, Travel Sites):

```bash
# Initialize database (from application directory)
python
>>> from app import app, db
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

Some applications include data seeding scripts (e.g., `add_data.py` in FlaskFM).

## Architecture Patterns

### Application Factory Pattern (Not Used)
These applications use a simple direct instantiation pattern where `app = Flask(__name__)` is called directly in `app.py`. This is appropriate for learning examples but not production applications.

### Circular Import Pattern
The Travel Sites application uses a common Flask pattern that appears circular but works due to Python's import mechanics:
- `app.py` creates the Flask app, db, and login manager, then imports `routes` and `models` at the bottom
- `models.py` imports from `app` to access `db` and `login`
- `routes.py` imports from both `app` and `models`

This pattern works because the imports at the bottom of `app.py` happen after the objects are created.

### Database Models

**Travel Sites** uses Flask-Login with User authentication:
- `User` model with password hashing (werkzeug.security)
- `Post` model for travel destinations with foreign key to User
- User loader function decorated with `@login.user_loader`

**FlaskFM** demonstrates many-to-many relationships:
- `User` → `Playlist` (one-to-one via foreign key)
- `Song` model for music tracks
- `Item` model as join table between `Playlist` and `Song`
- `Playlist` with dynamic relationship to items

### Forms and Validation

Applications use Flask-WTF for form handling:
- Forms defined as classes inheriting from `FlaskForm`
- Validators from `wtforms.validators` (DataRequired, Email, EqualTo)
- Custom validators as methods on form classes (e.g., `validate_username`)
- CSRF protection enabled by default (can be disabled with `csrf_enabled=False`)

### Template Structure

Templates use Jinja2 with inheritance:
- `base.html` provides common layout with blocks for `title` and `content`
- Child templates extend base: `{% extends "base.html" %}`
- Forms rendered with `{{ form.field_name.label }}` and `{{ form.field_name() }}`
- Flash messages displayed with `{% with messages = get_flashed_messages() %}`

## Dependencies

Key dependencies (see [requirements.txt](requirements.txt)):
- Flask 3.0.3
- Flask-SQLAlchemy 3.1.1 - ORM for database operations
- Flask-Login 0.6.3 - User session management
- Flask-WTF 1.2.1 - Form handling and CSRF protection
- WTForms 3.1.2 - Form validation
- SQLAlchemy 2.0.45 - Database toolkit
- email-validator 2.3.0 - Email validation for forms

Python version: 3.8+

## Common Issues

### Database Location
SQLite databases are created in the `instance/` directory by default (Flask 3.0+). The database URI `sqlite:///my_database.db` creates the file at `instance/my_database.db`.

### Secret Keys
All applications use hardcoded secret keys (e.g., `'you-will-never-guess'`). This is acceptable for learning examples but should use environment variables in production.

### Import Order
When modifying models or routes, be aware of the import order in `app.py`. The `import routes, models` statement must come after app, db, and login manager initialization.

### URL Parsing
The Travel Sites app uses `urllib.parse.urlparse` (not `werkzeug.urls.url_parse`) for validating redirect URLs in the login flow.
