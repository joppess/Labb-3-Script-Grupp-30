from dotenv import load_dotenv
load_dotenv()
import os
import requests
import json
api_key = os.getenv("API_KEY")
url = "https://www.omdbapi.com/?apikey=" + api_key

def search_specific_movie():
    specific_movie = input("Ditt film val: ")
    req_url = url + "&t=" + specific_movie
    r = requests.get(req_url)

    if r.status_code == 200:
        print(r.json()["Title"] + " (" + r.json()["Year"] + ")")
        print("Genre: " + r.json()["Genre"])
        print("Betyg: " + r.json()["imdbRating"] + "/10")
        print("Skådespelare: " + r.json()["Actors"])
        print(r.json()["Poster"])
        input("Tryck på enter för att fortsätta")
    else:
        print("Fel. Filmen kunde ej hittas.\n")
        input("Tryck på enter för att fortsätta")
    save_searches(specific_movie)

def show_search_history():
    pass

def search_movie():
    specific_movie = input("Ditt film val: ")
    req_url = url + "&s=" + specific_movie
    r = requests.get(req_url)
    print(r.json())

def save_searches(search_string):
    try:
        with open("history.json", "r", encoding="utf-8") as file_obj:
            data = file_obj.read()
            if not data.strip():
                movie_history = []
            else:
                movie_history = json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        movie_history = []

    new_search = {
        "search_string": search_string
    }
    if len(movie_history) >= 5:
        movie_history.pop()

    movie_history.insert(0, new_search) # nya sökningen lägg först med insert på index 0

    try:
        with open("history.json", "w") as file_obj:
            json.dump(movie_history, file_obj, ensure_ascii=False , indent=4)
        print("Sökhistoriken sparad")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Fel. Det gick inte att spara json-filen")




