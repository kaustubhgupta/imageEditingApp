from flask import Flask, render_template, request, flash, redirect, url_for
from utils import processImage, allowed_file
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "uploads"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "this is key"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/howtouse")
def howtouse():
    return render_template("howtouse.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        operation = request.form.get("inputaction")
        if "file" not in request.files:
            return render_template("error.html")

        file = request.files["file"]
        if file.filename == "":
            return render_template("error.html")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            filename = processImage(filename, operation)
            flash(
                f"Your image is processed and available <a target='_blank' href='/{filename}'>here</a>"
            )
            return redirect(url_for("home"))


app.run(debug=True, port=433)
