from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import db

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"


    id = db.column(db.integer,primary_Key = True)
    name = db.column(db.String(100),
    nullable=False)