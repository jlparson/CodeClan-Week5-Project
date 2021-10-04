from flask import Flask, render_template, request, redirect, Blueprint
from models.country import Country

import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

#Index
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)

#Show
@countries_blueprint.route("/countries/<id>")
def show(id):
    countries = country_repository.select(id)
    return render_template("countries/show.html", countries=countries)

#New
#