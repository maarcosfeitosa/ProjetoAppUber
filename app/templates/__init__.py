import pyodbc
from app.controllers import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd


app = Flask(__name__)
db = SQLAlchemy(app)



SERVER = 'DESKTOP-8J8RVEB\SQLEXPRESS'
DATABASE = 'GanhosUber'
DRIVER = 'SQL Server'
USERNAME = ''
PASSWORD = ''
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()
data = pd.read_sql_query(f"SELECT * FROM Usuario", connection)
print(data)

