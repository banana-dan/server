from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


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


# css {url_for('static', filename='css/style.css')}

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
