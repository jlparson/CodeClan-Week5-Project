from flask import Flask, render_template, request, redirect, Blueprint
from models.country import Country

import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

# # RESTFUL ROUTES

# INDEX
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)


# NEW
@countries_blueprint.route("/countries/new")
def new_country():
    countries = country_repository.select_all()
    return render_template("country/new.html", countries=countries)


# # CREATE
# @countries_blueprint


# SHOW
@countries_blueprint.route("/countries/<id>")
def show(id):
    countries = country_repository.select(id)
    return render_template("countries/show.html", countries=countries)

# # EDIT
# @countries_blueprint


# # UPDATE
# @countries_blueprint


# DELETE
@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('')
