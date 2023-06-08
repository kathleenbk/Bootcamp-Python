from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.survey import Survey


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result', methods=['GET'])
def result():
    return render_template("result.html", survey = Survey.get_survey())