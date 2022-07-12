from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<float:number>/')
def index(number):
    return render_template('index.html', number=f"Ваше число {number}, умноженное на 2: {number * 2}")


if __name__ == '__main__':
    app.run()
