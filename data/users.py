from datetime import datetime

import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    # id (Integer, primary_key, autoincrement)
    # surname (String) (фамилия)
    # name (String) (имя)
    # age (Integer) (возраст)
    # position (String) (должность)
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)

    # speciality (String) (профессия)
    # address (String) (адрес)
    # email (String, unique) (электронная почта)
    # hashed_password (String) (хэшированный пароль)
    # modified_date (DateTime) (дата изменения)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime)

    def check_password(self, password):
        return self.hashed_password == password
