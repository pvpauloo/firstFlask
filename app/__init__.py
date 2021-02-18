from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_cors import CORS
import os


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

manager = Manager(app)
manager.add_command('db', MigrateCommand)
lm = LoginManager()
lm.init_app(app)

from app.models import tables, forms
from app.controllers import defalt
