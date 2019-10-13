from web_travel.models import db, User, Country, City, Place
import json


def save_user(username, password, email):
    user_exists = User.query.filter(User.email == email).count()
    if not user_exists:
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()


def save_country(country_name):
    if not Country.query.filter(Country.country_name == country_name).count():
        new_country = Country(country_name=country_name)
        db.session.add(new_country)
        db.session.commit()


def save_city(city_name, related_country):
    print('city_exists', city_exists(city_name, related_country))
    if not city_exists(city_name, related_country):
        country = Country.query.filter(Country.country_name == related_country).first()
        new_city = City(city_name=city_name, country_id=country.id)
        db.session.add(new_city)
        db.session.commit()


def city_exists(city_name, releated_country):
    save_country(releated_country)
    same_cities_objects = City.query.filter(City.city_name == city_name).all()
    for city_object in same_cities_objects:
        country_object = Country.query.filter(Country.id == city_object.country_id)
        if country_object.first().country_name == releated_country:
            return True
    return False


def save_place(place_name, description, related_country, related_city):
    save_city(related_city, related_country)
    print('place exists', place_exists(place_name, related_country, related_city))
    if not place_exists(place_name, related_country, related_city):
        country = Country.query.filter(Country.country_name == related_country).first()
        city = City.query.filter(City.city_name == related_city).first()
        new_place = Place(place_name=place_name, description=description, country_id=country.id, city_id=city.id)
        db.session.add(new_place)
        db.session.commit()


def place_exists(place_name, related_country, related_city):
    same_places_objects = Place.query.filter(Place.place_name == place_name).all()
    for place_object in same_places_objects:
        city_object = City.query.filter(City.id == place_object.city_id)
        country_object = Country.query.filter(Country.id == place_object.country_id)
        if city_object.first().city_name == related_city and country_object.first().country_name == related_country:
            return True
    return False
    # place_to_check = Place.query.filter(Place.place_name == name)
    # if place_to_check.count():
    #     place_country = Country.query.filter(Country.id == place_to_check.first().country_id)
    #     place_city = City.query.filter(City.id == place_to_check.first().city_id)
    #     if place_country.count() and place_city.count():
    #         if place_country.first().country_name == related_country and place_city.first().city_name == related_city:
    #             return True
    # return False


def get_users():
    users = User.query.all()
    all_users = []
    for user in users:
        new_user = {
            'id': user.id,
            'name': user.username,
            'password': user.password,
            'email': user.email
        }
        all_users.append(new_user)
    return json.dumps(all_users)


def get_countries():
    countries = Country.query.all()
    all_countries = []
    for country in countries:
        new_country = {
            'id': country.id,
            'name': country.country_name
        }
        all_countries.append(new_country)
    return json.dumps(all_countries)


def get_cities():
    cities = City.query.all()
    all_cities = []
    for city in cities:
        new_city = {
            'id': city.id,
            'name': city.city_name,
            'country': city.country_id
        }
        all_cities.append(new_city)
    return json.dumps(all_cities)


def get_places():
    places = Place.query.all()
    all_places = []
    for place in places:
        new_place = {
            'id': place.id,
            'name': place.place_name,
            'description': place.description,
            'country': place.country_id,
            'city': place.city_id
        }
        all_places.append(new_place)
    return json.dumps(all_places)
