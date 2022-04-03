# этот файл всего лишь создает несколько пользователей
from datetime import datetime

from flask import Flask, url_for, request, render_template
from werkzeug.utils import redirect

from data.loginform import LoginForm
from data import db_session
from data.jobs import Jobs
from data.users import User
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# запускаем базу данных (грубо говоря)
db_session.global_init("db/blogs.db")
session = db_session.create_session()

# запускаем flask_login
login_manager = LoginManager()
login_manager.init_app(app)


# функия, нужная для flask_login
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/index/lololololo")
        return render_template('authorisation.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('authorisation.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

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


@app.route("/list_prof/<list>")
def list_prof(list):
    data = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечивания",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]
    return render_template("list_prof.html", list=list, data=data)


# css {url_for('static', filename='css/style.css')}


def main():
    # db_session.global_init("db/blogs.db")  # запускаем базу данных (грубо говоря)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
