from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Flask-steppik</h1>"


@app.route('/test/')
def test():
    return render_template('index.html', email='popov@gmail.com', message='Flask - это прекрасно!', title='Обучение')


if __name__ == '__main__':
    app.run()
