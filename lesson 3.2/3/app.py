from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask-steppik"


@app.route('/<a>/<b>/<c>/')
def loop(a, b, c):
    some_list = [a, b, c]
    return render_template('index.html', numbers=some_list)


if __name__ == '__main__':
    app.run()
