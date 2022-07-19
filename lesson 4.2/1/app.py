from flask import Flask, render_template, request
from form import ProfileForm

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    form = ProfileForm(meta={"csrf": False})
    form_name = form.username
    form_password = form.password
    form_about_me = form.about_me
    form_submit = form.submit
    return render_template("index.html",
                           name=form_name,
                           password=form_password,
                           about_me=form_about_me,
                           submit=form_submit)


if __name__ == '__main__':
    app.run(debug=True)
