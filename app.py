from os import path
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request


app = Flask(__name__)
browse = "C:\\Users\\raiha\\PycharmProjects\\Mp3 Uploader\\static\\uploads"

app.config['MAX_CONTENT_LENGTH'] = 20 * 1000 * 1000

@app.route("/")
def home():
    return render_template("Index.html")


@app.route("/main")
def audio():
    return render_template("mp3uploader.html")



@app.route("/upload", methods=["POST"])
def generate():
    file = request.files['audio']
    filename = secure_filename(file.filename)
    file.save(path.join("C:\\Users\\raiha\\PycharmProjects\\Mp3 Uploader\\static\\uploads", filename))
    return render_template("Download.html")

@app.errorhandler(413)
def error413(e):
    return render_template('413.html'), 413

@app.route("/random")
def rand():
    return render_template("HTML.html")


if __name__ == "__main__":
    app.run(debug=True)
