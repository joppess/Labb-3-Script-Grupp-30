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

def show_search_history():
    pass

def search_movie():
    specific_movie = input("Ditt film val: ")
    req_url = url + "&s=" + specific_movie
    r = requests.get(req_url)
    print(r.json())

