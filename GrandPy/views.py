from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    sentence = "hello :) je suis grandPy, tu as une question à me poser ? "
    return render_template("index.html", sentence=sentence)


if __name__ == "__main__":
    app.run()
