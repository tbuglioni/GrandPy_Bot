from flask import Flask, render_template
from GrandPy.controller.process_post import ProcessPost


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    my_process = ProcessPost()
    return my_process.processing()


if __name__ == "__main__":
    app.run(debug=True)
