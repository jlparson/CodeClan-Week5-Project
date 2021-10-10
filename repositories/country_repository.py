from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


# SAVE COUNTRY TO DATABASE
def save(country):
    sql = "INSERT INTO countries (name, visited) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


# SELECT ALL COUNTRIES
def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['visited'], row['id'])
        countries.append(country)
    return countries


# SELECT COUNTRY BY ID
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['visited'], result['id'])
    return country


# DELETE ALL COUNTRIES
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


 # DELETE COUNTRY BY ID
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# UPDATE COUNTRY DETAILS
def update(country):
    sql = "UPDATE countries SET (name, visited) = (%s, %s) WHERE id = %s"
    values = [country.name, country.visited, country.id]
    run_sql(sql, values)


# LIST ALL CITIES IN A COUNTRY BY COUNTRY ID
def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['city_name'], row['visited'], row['country_id'], row ['id'])
        cities.append(city)
    return cities
