import json

filename='population_data.json'
with open(filename) as data:
    pop_data=json.load(data)
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
        print(country+' has '+str(population)+" people")