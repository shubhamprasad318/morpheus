Prerequisites
Ensure the following are installed on your system:

Python 3.8+
Django 4.0+
Django REST Framework (DRF)

Installation
Clone the repository:

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py makemigrations
python manage.py migrate


Start the development server:
python manage.py runserver
Access the application at http://127.0.0.1:8000.