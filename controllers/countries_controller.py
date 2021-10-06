import re
from flask import Flask, render_template,request, redirect, Blueprint

from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/")
def countries():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("/countries/index.html", countries=countries, cities=cities)

# NEW
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new.html")

# CREATE
@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    name = request.form['name']
    visited = request.form['visited']
    country = Country(name, visited)
    country_repository.save(country)
    return redirect('/countries')


# SHOW
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)


# EDIT
@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template('countries/edit.html', country = country, all_cities = cities)

# UPDATE
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    country = country_repository.select(id)
    visited = request.form['visited']
    country = Country(country.name, visited, id)
    country_repository.update(country)
    return redirect('/countries')

# DELETE
@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    city_repository.delete(id)
    country_repository.delete(id)
    return redirect('/countries')
