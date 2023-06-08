from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas/new')
def ninjas():
    ninjas = Ninja.get_all()
    return render_template("newninja.html", dojos=Dojo.get_all())

@app.route('/ninjas/create', methods=["POST"])
def create_ninja():
    if not Ninja.validate_ninja(request.form):
        return redirect('/ninjas/new')
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age'],
        "dojo_id":request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/dojos')