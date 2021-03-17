from flask import Flask, request, render_template
from GrandPy.controller.process_post import ProcessPost


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    my_process = ProcessPost(request.form["my_text"])
    return my_process.processing()