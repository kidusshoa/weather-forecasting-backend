# weather-forecasting-backend

University Machine Learning Class Project backend source code

# Install virtual environment

python -m venv env
source env/bin/activate # On Mac

# Install Django and DRF

pip install django djangorestframework

# Create Django project

django-admin startproject weather_backend
cd weather_backend

# Create Django app

python manage.py startapp api
