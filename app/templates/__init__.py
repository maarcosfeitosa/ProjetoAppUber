from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers import default

app = Flask(__name__)
db = SQLAlchemy(app)





