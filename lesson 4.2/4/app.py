from flask import Flask, render_template, request, redirect, url_for

from form import ProfileForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = 'i1am2stupped'





@app.route('/', methods=["GET", "POST"])
def index():
    form = ProfileForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        about_me = form.about_me.data
        return render_template("index.html", form=form, username=username, password=password, about_me=about_me)
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
