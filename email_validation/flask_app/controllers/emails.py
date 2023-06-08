from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html", emails=Email.get_all())