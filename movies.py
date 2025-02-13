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
    save_searches(specific_movie)
    try:
        r = requests.get(req_url)

        if r.status_code == 200:
            if r.json().get("Response") == "False":
                print("Fel. " + r.json().get("Error", "Okänt fel"))
                input("Tryck på enter för att fortsätta")
                return

            print(r.json()["Title"] + " (" + r.json()["Year"] + ")")
            print("Genre: " + r.json()["Genre"])
            print("Betyg: " + r.json()["imdbRating"] + "/10")
            print("Skådespelare: " + r.json()["Actors"])
            print(r.json()["Poster"])
            input("Tryck på enter för att fortsätta")
        else:
            print("Fel. Filmen kunde ej hittas.\n")
            input("Tryck på enter för att fortsätta")
    except requests.ConnectionError:
        print("Fel, kunde inte ansluta till servern")
    except requests.Timeout:
        print("Fel, tog för lång tid att ansluta")
    except requests.HTTPError:
        print("Fel, HTTP fel")
    except requests.JSONDecodeError:
        print("Fel, kunde inte avkoda JSON data")
    except requests.RequestException:
        print("Fel, okänt fel inträffade")


def show_search_history():
    try:
        with open("history.json", "r") as file_obj:
            data = file_obj.read()
            if not data.strip():
                print("Sökhistoriken är tom")
            else:
                movie_history = json.loads(data)
                print("Sökhistorik:")
                for movie in movie_history:
                    print(movie["search_string"])
    except (FileNotFoundError, json.JSONDecodeError):
        print("Fel, filen finns ej eller är trasig")



def search_movie():
    specific_movie = input("Ditt film val: ")
    req_url = url + "&s=" + specific_movie
    save_searches(specific_movie)
    try:
        r = requests.get(req_url)

        if r.status_code == 200:
            if r.json().get("Response") == "False":
                print("Fel. " + r.json().get("Error", "Okänt fel"))
                input("Tryck på enter för att fortsätta")
                return

            for movie in r.json().get("Search"):
                print(movie["Title"] + " (" + movie["Year"] + ")")
                print("Typ: " + movie["Type"])
                print(movie["Poster"] + "\n")
        else:
            print("Fel. Filmen kunde ej hittas.\n")
            input("Tryck på enter för att fortsätta")
        input("Tryck på enter för att fortsätta")
    except requests.ConnectionError:
        print("Fel, kunde inte ansluta till servern")
    except requests.Timeout:
        print("Fel, tog för lång tid att ansluta")
    except requests.HTTPError:
        print("Fel, HTTP fel")
    except requests.JSONDecodeError:
        print("Fel, kunde inte avkoda JSON data")
    except requests.RequestException:
        print("Fel, okänt fel inträffade")


def save_searches(search_string):
    try:
        with open("history.json", "r") as file_obj:
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
    except (FileNotFoundError, json.JSONDecodeError):
        print("Fel. Det gick inte att spara json-filen")




