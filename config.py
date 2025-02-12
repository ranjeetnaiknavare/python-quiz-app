import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Secret key for forms
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quiz.db'  # Database URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable event notifications

