from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Homepage"


@app.route('/<numbers>/')
def find_square(numbers):
    return render_template('index.html', numbers=tuple(numbers))


if __name__ == '__main__':
    app.run()
