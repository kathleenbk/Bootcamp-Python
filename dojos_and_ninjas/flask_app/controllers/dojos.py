from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route('/dojos/new', methods=["POST"])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show(id):
    data ={
        "id": id
    }
    return render_template("ninjas.html", dojo=Dojo.get_dojo_with_ninjas(data))
