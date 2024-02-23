import csv
import hashlib
import json
import os
import random
import uuid
import bleach
from bleach.css_sanitizer import CSSSanitizer

def check_attribute(value):
    print(value, 'before')
    # allowed_tags = {'a'}
    # allowed_attributes = {'a': ['href']}
    allowed_tags = [
        'div', 'span','p', 'a', 'ul', 'ol', 'li', 'blockquote',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'strong', 'em','i','b','u',
        'br','img','iframe','figure','figcaption','table','thead','tbody','tr','th','td','style'    
    ]
    allowed_attributes = {
        '*': ['style','class','id'],
        'div':['data-oembed-url','style','class','id'],
        'a': ['href', 'rel', 'title','style','class','id'],
        'img': ['src', 'width', 'height', 'alt','style','class','id'],
        'iframe': ['src', 'width', 'height', 'allowfullscreen','frameborder','allow','style','class','id'],
        # 'video': [
        #     'controls', 'width', 'height', 'allowfullscreen', 'preload',
        #     'poster'],
        # 'audio': ['controls', 'preload'],
    }
    css_sanitizer = CSSSanitizer(allowed_css_properties=['display',"position","top","left","right","bottom",'width', 'height','background','border','background-image','margin','margin-left','margin-right','margin-top','margin-bottom','padding','padding-left','padding-right','padding-top','padding-bottom'])                     
    cleaned_string = bleach.clean(text=value, tags=allowed_tags, attributes=allowed_attributes,css_sanitizer=css_sanitizer, strip=True)
    print(cleaned_string, 'after')
    return cleaned_string

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def get_random_string(length):
    sample_letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join((random.choice(sample_letters) for i in range(length)))

def get_random_number(length):
    sample_letters = "1234567890"
    return "".join((random.choice(sample_letters) for i in range(length)))


def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}


def setup_cities():
    import json

    from entitas.city.services import insert_city_db
    from entitas.state.services import insert_state_db

    with open("config/indonesia-cities.json") as f:
        data = json.load(f)
    for state_json in data["states"]:
        state = insert_state_db(json_object=state_json)
        for city_json in state_json["cities"]:
            city_json["state_id"] = state["id"]
            city_json["state_name"] = state["name"]
            insert_city_db(json_object=city_json)


def setup_cities_b():
    import json

    from entitas.city.services import insert_city_db
    from entitas.state.services import insert_state_db
    from res.indonesia_cities import cities

    data = cities
    state_id = 0
    for item in data:
        for state_json in item["states"]:
            state_id += 1
            state = insert_state_db(json_object=state_json)
            for city_json in state_json["cities"]:
                city_json["state_id"] = state["id"]
                city_json["state_name"] = state["name"]
                insert_city_db(json_object=city_json)


def update_lat_lon_citie():
    import json

    from entitas.city.services import find_city_db_by_name, update_city_db
    from entitas.state.services import find_state_db_by_name, update_state_db
    from res.indonesia_cities import cities

    data = cities
    count_city = 0
    state_id = 0
    for item in data:
        for state_json in item["states"]:
            state_id += 1
            state = find_state_db_by_name(name=state_json["name"], to_model=True)
            state.lat = state_json["latitude"]
            state.lon = state_json["longitude"]
            update_state_db(json_object=state.to_response())
            for city_json in state_json["cities"]:
                city = find_city_db_by_name(name=city_json["name"].upper())
                if city is None:
                    city = find_city_db_by_name(
                        name="KOTA " + city_json["name"].upper()
                    )
                if city is None:
                    continue
                count_city += 1
                city["lat"] = city_json["latitude"]
                city["lon"] = city_json["longitude"]
                city["state_id"] = state.id
                city["state_name"] = state.name
                update_city_db(json_object=city)


def raise_error(msg="", param_name=""):
    import falcon

    raise falcon.HTTPBadRequest(description=msg)
