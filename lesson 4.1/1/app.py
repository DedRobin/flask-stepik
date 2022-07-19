from flask import Flask, render_template, request, abort

news = {}

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def render():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if not title or not content:
            abort(404)
        news[title] = content
    return render_template("index.html", news=news)


if __name__ == '__main__':
    app.run()
