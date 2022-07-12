from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Homepage"


@app.route('/<val>/')
def find_square(val):
    return render_template('index.html', val=val)


if __name__ == '__main__':
    app.run()
