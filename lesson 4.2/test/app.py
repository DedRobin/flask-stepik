from flask import Flask, render_template, request, redirect, url_for
from form import MessageForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = 'boobs'


@app.route('/', methods=["GET"])
def index():
    return "Index page"


@app.route('/message/', methods=["GET", "POST"])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name, email, message, "Data received. Now redirecting...", sep="\n")
        return redirect(url_for("index"))
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
