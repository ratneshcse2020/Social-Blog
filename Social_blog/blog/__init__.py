#this is social blog/_init__.py

from flask import Flask
from blog.core.views import core
from blog.error_pages.handlers import error_pages
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


########DATABASE SETUP#########

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(db,app)


###############################

#########LOGIN CONFIG#######

login_manager=LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

app.register_blueprint(core)
app.register_blueprint(error_pages)