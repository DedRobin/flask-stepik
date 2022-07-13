from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask-steppik"


@app.route('/<a>/<sign>/<b>/')
def arithmetic_operation(a, b, sign):
    print(a, sign, b)
    return render_template('index.html', a=a, b=b, sign=sign)


if __name__ == '__main__':
    app.run()
