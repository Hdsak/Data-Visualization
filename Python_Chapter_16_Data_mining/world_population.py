from pygal.maps.world import COUNTRIES
from country_codes import country_code
import json
import pygal

filename='population_data.json'
with open(filename) as data:
    pop_data=json.load(data)
cc_population={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country=pop_dict["Country Name"]
        population=int(float(pop_dict["Value"]))
        code=country_code(country)
        if code:
            cc_population[code]=country
wm=pygal.maps.world.World()
wm.title="Population of earth in 2010"
wm.add("2010",cc_population)
wm.render_to_file('world.svg')