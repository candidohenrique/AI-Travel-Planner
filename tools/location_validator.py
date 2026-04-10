import pycountry
import geonamescache
import unicodedata


def _normalize(text):
    text = text.lower().strip()
    text = unicodedata.normalize("NFD", text)
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


def _build_city_index(city_data):
    return {
        _normalize(city["name"]): city
        for city in city_data.values()
    }


def _build_name_index(items):
    return {
        _normalize(item.name): item
        for item in items
    }


geonames_cache = geonamescache.GeonamesCache()
cities = geonames_cache.get_cities()

city_index = _build_city_index(cities)
countries = _build_name_index(pycountry.countries)
states = _build_name_index(pycountry.subdivisions)


def validate_location(location):
    normalized_location = _normalize(location)

    if normalized_location in countries:
        return {
            "type": "country",
            "name": countries[normalized_location].name
        }

    if normalized_location in states:
        return {
            "type": "state",
            "name": states[normalized_location].name
        }

    if normalized_location in city_index:
        matched_city = city_index[normalized_location]
        return {
            "type": "city",
            "name": matched_city["name"],
            "country": matched_city["countrycode"]
        }

    return None