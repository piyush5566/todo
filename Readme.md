# Todo Application

### Overview
This project is a Django-based Todo application. It allows users to manage tasks through a web interface and leverages Django's powerful admin interface for backend management.

### Features
- Create, update, and delete tasks
- Django admin interface
- Environment variable support with python-dotenv

### Prerequisites
- Python 3+
- Virtual environment tool (e.g., `venv`)

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd todo
```

2. **Create and activate a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
   - Rename the provided `.env.example` file to `.env`.
   - Open the `.env` file and set the values for all keys as they are mandatory (e.g., `DJANGO_SECRET_KEY`, `DATABASE_URL`, etc.).

5. **Apply migrations:**
```bash
python manage.py migrate
```

6. **Create a superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Collect Static Files:**
   Before starting the development server, run:
```bash
python manage.py collectstatic
```

### Running the Application

Start the development server:
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to access the application. For the admin interface, visit `http://127.0.0.1:8000/admin`.

### Project Structure
```
todo/
├── myapp/
│   ├── admin.py
│   ├── models.py
│   └── ... (other Django app files)
├── manage.py
├── requirements.txt
├── .gitignore
└── ... (other project files)
```

### Additional Information

- **Static Files:** Make sure your static files settings in `settings.py` are correctly configured.
- **Environment Configuration:** Use the `.env` file to securely store sensitive settings.

### License
MIT License

### Contributing
If you find issues or want to contribute improvements, please open an issue or submit a pull request.
