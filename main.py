# этот файл всего лишь создает несколько пользователей
from datetime import datetime

from flask import Flask, url_for, request, render_template

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
db_session.global_init("db/blogs.db")
session = db_session.create_session()


def create_4users():
    # создаем капитана
    capitan = User()
    capitan.surname = "Scott"
    capitan.name = "Ridley"
    capitan.age = 21
    capitan.position = "captain"
    capitan.speciality = "research engineer"
    capitan.address = "module_1"
    capitan.email = "scott_chief@mars.org"
    capitan.hashed_password = "cap"
    session.add(capitan)

    for count in range(3):
        user = User()
        user.surname = "user" + str(count)
        user.name = "name" + str(count)
        user.age = 20 * count
        user.position = "position" + str(count)
        user.speciality = "speciality" + str(count)
        user.address = "module_" + str(count)
        user.email = "email" + str(count)
        user.hashed_password = "cap" + str(count)
        session.add(user)
    session.commit()


def create_first_task():
    task = Jobs()
    task.team_leader = 1
    task.job = "deployment of residential modules 1 and 2"

    task.work_size = 15
    task.collaborators = '2, 3'
    task.start_date = datetime.now()
    task.is_finished = False
    session.commit()


def main():
    # запускаем базу данных (грубо говоря)
    create_first_task()


if __name__ == '__main__':
    main()
