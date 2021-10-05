from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

# CITIES VISITED
@cities_blueprint.route("/visited")
def cities_visited():
    cities = city_repository.select_all()
    return render_template("cities/visited.html", cities=cities)

# CITIES BUCKET LIST
@cities_blueprint.route("/bucketlist")
def cities_bucket_list():
    cities = city_repository.select_all()
    return render_template("cities/bucketlist.html", cities=cities)


# NEW
# GET '/cities/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)

# CREATE
# POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country = country_repository.select(request.form['country_id'])
    visited = request.form['visited']
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect('/cities')

# EDIT
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('/cities/edit.html', city=city, all_countries = countries)

# UPDATE
# @cities_blueprint.route("/cities/<id>", methods=['POST'])
# def update_city(id):
#     name = request.form['name']
#     country = country_repository.select(request.form['country_id'])
#     visited = request.form["visited"]
#     city = City(name, country, visited)
#     print(city.country.name)
#     city_repository.update(city)
#     return redirect('/cities')

# UPDATE
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect('/cities')

# DELETE
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

