from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Flask-steppik</h1>"


@app.route('/test/')
def test():
    return render_template(values_min=(1, 2, 3), action_min='find', x_min=1, y_min=3.141592653589793)


if __name__ == '__main__':
    app.run()
