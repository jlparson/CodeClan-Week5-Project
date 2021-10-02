from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)