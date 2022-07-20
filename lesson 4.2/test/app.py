from flask import Flask, render_template, request
from form import MessageForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = 'boobs'


@app.route('/', methods=["GET"])
def index():
    form = MessageForm()
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
