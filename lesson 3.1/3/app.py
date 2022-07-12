from math import pi

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Homepage"


@app.route('/<number>/')
def find_square(number):
    return render_template('index.html', number=float(number), pi=pi)


if __name__ == '__main__':
    app.run()
