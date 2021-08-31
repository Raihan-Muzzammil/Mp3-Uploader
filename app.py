from os import path
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from flask_autoindex import AutoIndex


app = Flask(__name__)
browse = "C:\\Users\\raiha\\PycharmProjects\\Mp3 Uploader\\static\\uploads"

@app.route("/")
def home():
    return render_template("Index.html")


@app.route("/main")
def audio():
    return render_template("mp3uploader.html")


@app.route("/upload", methods=["POST"])
def generate():
    file = request.files['audio']
    filename = secure_filename(file.filename + ".mp3")
    file.save(path.join("C:\\Users\\raiha\\PycharmProjects\\Mp3 Uploader\\static\\uploads", filename))
    return render_template("Download.html")



@app.route("/random")
def rand():
    return render_template("HTML.html")


if __name__ == "__main__":
    app.run(debug=True)
