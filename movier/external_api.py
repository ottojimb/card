from flask import current_app
import requests
import json

BASE_URL="https://api.themoviedb.org/"
IMAGE_URL="https://image.tmdb.org/"


def get_images(movie_id):
    auth_key = current_app.config["AUTH_KEY_MV"]
    url = f"{BASE_URL}3/movie/{movie_id}/images?api_key={auth_key}"

    q = requests.get(url)
    return json.loads(q.text)


def find_movie_by_title(title):
    auth_key = current_app.config["AUTH_KEY_MV"]
    url = f"{BASE_URL}3/search/movie?api_key={auth_key}&query={title}"

    q = requests.get(url)
    objs = json.loads(q.text)["results"]

    for idx, obj in enumerate(objs):
        objs[idx]["images"] = get_images(obj["id"])
    
    return objs
