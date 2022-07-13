from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Flask-steppik</h1>"


@app.route('/test/')
def test():
    return render_template('index.html', varargs=[1, 10, 100, 1000, 10000, ],
                           kwargs={'11111': 'm', '10': 'o', '1': 'r', '111': 'i', '666': 'e', })

if __name__ == '__main__':
    app.run()
