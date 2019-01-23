import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_login import LoginManager
from elasticsearch import Elasticsearch
from flask_babel import Babel
from flask_migrate import Migrate
from celery import Celery


app = Flask(__name__)
app.config['SECRET_KEY'] = '6777e0789a4ce2892f75e7ef6e55b0c4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['ELASTICSEARCH_URL']='http://localhost:9200'
ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
babel = Babel(app)
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']])


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['POSTS_PER_PAGE'] = 10


# Celery configuration
app.config['CELERY_BROKER_URL'] = 'amqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://guest@localhost//'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


from app import routes, models

