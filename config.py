import os.path
basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'CHAVE_BEM_SEGURA'

# Baseado nas aulas de Julia Rizzi
# https://www.youtube.com/c/J%C3%BAliaRizza/about