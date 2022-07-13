from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Flask-steppik</h1>"


@app.route('/loop')
def loop():
    return render_template('index.html', numbers={'string': 0, 'f2': 1, '15': 6, 'g3': -8, '19': 19,
                                                  'b2c5f': 11, '09': 90})


if __name__ == '__main__':
    app.run()
