from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sight import Sight

import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository
import repositories.country_repository as country_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", sights = sights)


# SIGHTS VISITED
@sights_blueprint.route("/sights/visited")
def sights_visited():
    sights = sight_repository.select_all()
    return render_template("sights/visited.html", sights=sights)

# SIGHTS BUCKET LIST
@sights_blueprint.route("/sights/bucketlist")
def sights_bucket_list():
    sights = sight_repository.select_all()
    return render_template("sights/bucketlist.html", sights=sights)


# NEW
# GET '/sights/new'
@sights_blueprint.route("/sights/new", methods=['GET'])
def new_sight():
    cities = city_repository.select_all()
    return render_template("sights/new.html", cities=cities)

# CREATE
# POST '/sights'
@sights_blueprint.route("/sights", methods=['POST'])
def create_sight():
    name = request.form['name']
    city = city_repository.select(request.form['city_id'])
    visited = request.form["visited"]
    sight = Sight(name, city, visited)
    sight_repository.save(sight)
    return redirect('/sights')

# EDIT
@sights_blueprint.route("/sights/<id>/edit", methods=['GET'])
def edit_sight(id):
    sights = sight_repository.select(id)
    cities = city_repository.select_all()
    return render_template('/sights/edit.html', sights=sights)

# UPDATE
@sights_blueprint.route("/sights/<id>", methods=['POST'])
def update_sight(id):
    name = request.form['name']
    city = city_repository.select(request.form['city_id'])
    visited = request.form["visited"]
    sight = Sight(name, city, visited)
    print(sight.city.name)
    sight_repository.update(sight)
    return redirect('/sights')

# DELETE
@sights_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sight(id):
    sight_repository.delete(id)
    return redirect('/sights')



