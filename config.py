# config.py

import os

# Secret key for session management (use a random secret in production)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-random-secret-key'

# Database configuration (example using SQLite)
DATABASE = {
    'ENGINE': 'sqlite',
    'NAME': os.path.join(os.getcwd(), 'database.db'),  # Path to the SQLite database file
}

# For production, you might use environment variables to store sensitive information like this
DB_USERNAME = os.environ.get('DB_USERNAME') or 'your_db_username'
DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'your_db_password'

# Session timeout (in seconds)
SESSION_TIMEOUT = 3600  # 1 hour

# Enable or disable debug mode
DEBUG = True

# Email settings (if you want to add email functionality for user verification or password reset)
EMAIL = {
    'SMTP_SERVER': 'smtp.example.com',
    'SMTP_PORT': 587,
    'EMAIL_ADDRESS': os.environ.get('EMAIL_ADDRESS') or 'your-email@example.com',
    'EMAIL_PASSWORD': os.environ.get('EMAIL_PASSWORD') or 'your-email-password',
}
