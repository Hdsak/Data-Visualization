from pygal.maps.world import COUNTRIES

def country_code(country):
    for code,name in COUNTRIES.items():
        if name==country:
            return str(code)
    return None
