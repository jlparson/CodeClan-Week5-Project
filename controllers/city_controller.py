from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

