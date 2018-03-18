import logging

from flask import Flask

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from application import views
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dabase import views as db_declear

engine = create_engine('sqlite:///argo_food.db')
try:
    engine.connect()
    engine.execute('SELECT 1;')
except OperationalError:
    db_declear()