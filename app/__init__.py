from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from elasticsearch import Elasticsearch
from flask_babel import Babel
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '6777e0789a4ce2892f75e7ef6e55b0c4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['ELASTICSEARCH_URL']='http://localhost:9200'
ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
babel = Babel(app)
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']])

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['POSTS_PER_PAGE'] = 10


from app import routes, models
