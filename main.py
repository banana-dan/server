# этот файл всего лишь создает несколько пользователей
from datetime import datetime

from flask import Flask, url_for, request, render_template

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
# запускаем базу данных (грубо говоря)
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


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route("/index/<header>")
def index(header):
    return render_template("base.html", title=header)


@app.route('/promotion')
def promote():
    return "Человечество вырастает из детства.</br>Человечеству мала одна планета." \
           "</br>Мы сделаем обитаемыми безжизненные пока планеты.</br>И начнем с Марса!" \
           "</br>Присоединяйся!"


# @app.route('/promotion_image')
# def promote():
#     return "Человечество вырастает из детства.</br>Человечеству мала одна планета." \
#            "</br>Мы сделаем обитаемыми безжизненные пока планеты.</br>И начнем с Марса!" \
#            "</br>Присоединяйся!"


@app.route('/image_mars')
def image():
    return render_template("image_mars.html", src=url_for('static', filename='img/mars.jpg'))
    # return f'''<h1>Жди нас, Марс!</h1></br><img src="{url_for('static', filename='img/mars.jpg')}"
    #        alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/promotion_image')
def promotion_image():
    param = dict()
    param['css'] = url_for('static', filename='css/style.css')
    param['src'] = url_for('static', filename='img/mars.jpg')
    return render_template("promotion.html", **param)


@app.route('/astronaut_selection')
def selection():
    pass


@app.route('/training/<prof>')
def training(prof):
    return render_template("training.html", prof=prof,
                           science_src=url_for('static', filename='img/nauchpop.png'),
                           it_src=url_for('static', filename='img/it.png'),
                           medicine_src=url_for('static', filename='img/medicine.png'),
                           default_src=url_for('static', filename="img/base.png"))


# css {url_for('static', filename='css/style.css')}


def main():
    # db_session.global_init("db/blogs.db")  # запускаем базу данных (грубо говоря)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
