from flask import Flask, render_template, request
from form import MessageForm

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    form = MessageForm(meta={"csrf": False})
    form_name = form.name
    form_email = form.email
    form_message = form.message
    form_submit = form.submit
    return render_template("index.html",
                           name=form_name,
                           email=form_email,
                           message=form_message,
                           submit=form_submit)


if __name__ == '__main__':
    app.run(debug=True)
