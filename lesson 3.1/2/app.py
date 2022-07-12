from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", text="Ваше число 1.0, умноженное на 2:", number=2.0)


if __name__ == '__main__':
    app.run()
