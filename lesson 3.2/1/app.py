from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask-steppik"


@app.route('/<int:a> <int:b> <int:c>/')
def average(a, b, c):
    print(a, b, c)
    return render_template('index.html', a=a, b=b, c=c)


if __name__ == '__main__':
    app.run()
