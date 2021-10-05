import pdb
from models.country import Country
from models.city import City
from models.sight import Sight

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

country_repository.delete_all()
city_repository.delete_all()
sight_repository.delete_all()

country1 = Country("Spain")
country_repository.save(country1)
country2 = Country("France")
country_repository.save(country2)
country3 = Country("Japan")
country_repository.save(country3)

city1 = City("Granada", country1, True)
city_repository.save(city1)
city2 = City("Paris", country2, True)
city_repository.save(city2)
city3 = City("Versailles", country2, False)
city_repository.save(city3)
city4 = City("Tokyo", country3, False)
city_repository.save(city4)

sight1 = Sight("Alhambra", city1, True)
sight_repository.save(sight1)
sight2 = Sight("Palace of Versailles", city3, False)
sight_repository.save(sight2)
sight3 = Sight("Eiffel Tower", city2, True)
sight_repository.save(sight3)
sight4 = Sight("Meiji Jingu Shrine", city4, False)
sight_repository.save(sight4)
sight5 = Sight("Tokyo Tower", city4, False)
sight_repository.save(sight5)
sight6 = Sight("Louvre Museum", city2, True)
sight_repository.save(sight6)



pdb.set_trace()