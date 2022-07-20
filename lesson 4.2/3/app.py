from flask import Flask, render_template, request

from form import ProfileForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = 'i1am2stupped'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "<h1>Data is recorded!</h1>"
    form = ProfileForm()
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
