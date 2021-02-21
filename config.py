import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.envrc')
load_dotenv(dotenv_path)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


print(os.environ['DATABASE_URL'])
basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = True


SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'CHAVE_BEM_SEGURA'

# Baseado nas aulas de Julia Rizzi
# https://www.youtube.com/c/J%C3%BAliaRizza/about
