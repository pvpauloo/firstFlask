import os
basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'CHAVE_BEM_SEGURA'

# Baseado nas aulas de Julia Rizzi
# https://www.youtube.com/c/J%C3%BAliaRizza/about
