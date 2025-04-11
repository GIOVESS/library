# Library Management System

A simple Django-based library management system with REST API functionality.

## Features

- Book management (CRUD operations)
- REST API endpoints for book data
- SQLite database (default)
- Django admin interface

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/GIOVESS/library.git
   cd library
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/` - List all books
- `POST /api/` - Add new book
- `GET /api/<id>/` - Get specific book details
- `PUT /api/<id>/` - Update book
- `DELETE /api/<id>/` - Remove book

## Project Structure

```
library/
├── lib/               # Main project folder
│   ├── settings.py    # Django settings
│   └── urls.py        # Main URLs
├── books/             # Books app
│   ├── models.py      # Book model
│   └── ...
├── apis/              # API app
│   ├── serializers.py # DRF serializers
│   ├── views.py       # API views
│   └── ...
└── manage.py          # Django management script
```

## Admin Access

Access the admin panel at `http://localhost:8000/admin/` after creating a superuser.

## Requirements

- Python 3.8+
- Django 5.0+
- Django REST Framework

