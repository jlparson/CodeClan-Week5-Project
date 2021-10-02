from db.run_sql import run_sql
from models.city import City

from models.sight import Sight

import repositories.city_repository as city_repository


def save(sight):
    sql = "INSERT INTO sights (name, city_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [sight.name, sight.city.id, sight.visited]
    results = run_sql(sql, values)
    sight.id = results[0]['id']
    return sight


def select_all():
    sights = []
    
    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'], city, row['visited'], row['id'])