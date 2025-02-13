# Importerar moduler
from dotenv import load_dotenv
# används för att läsa in miljövariabler från en .env-fil
load_dotenv()
# importera moduler
import os
import requests
import json
# Läser in API-nyckeln från miljövariabler
api_key = os.getenv("API_KEY")
# URL till API:et
url = "https://www.omdbapi.com/?apikey=" + api_key # lägger till API-nyckeln i URL:en

# Sök efter en specifik film
def search_specific_movie():
    # Fråga användaren efter en specifik film
    specific_movie = input("Ditt film val: ")
    # Lägg till filmen i URL:en
    req_url = url + "&t=" + specific_movie # &t= används för att söka efter en specifik film
    # Spara sökhistoriken
    save_searches(specific_movie)

    # Försöker ansluta till API:et
    try:
        r = requests.get(req_url) # get-metoden används för att hämta data från API:et

        # Om anslutningen lyckas
        if r.status_code == 200:
            # Om responsen är False, skriv ut felmeddelandet
            if r.json().get("Response") == "False":
                print("Fel. " + r.json().get("Error", "Okänt fel")) # om det inte finns något felmeddelande, skriv ut "Okänt fel"
                input("Tryck på enter för att fortsätta")
                return # avsluta funktionen

            # Skriv ut informationen om filmen
            print(r.json()["Title"] + " (" + r.json()["Year"] + ")")
            print("Genre: " + r.json()["Genre"])
            print("Betyg: " + r.json()["imdbRating"] + "/10")
            print("Skådespelare: " + r.json()["Actors"])
            print(r.json()["Poster"])
            input("Tryck på enter för att fortsätta")
        else:
            # Om statuskoden inte är 200, skriv ut felmeddelandet
            print("Fel. Oväntad statuskod, förväntades, 200 (OK).\n")
            input("Tryck på enter för att fortsätta")
    # Felhantering
    except requests.ConnectionError: # om det inte går att ansluta till servern
        print("Fel, kunde inte ansluta till servern")
    except requests.Timeout: # om det tar för lång tid att ansluta
        print("Fel, tog för lång tid att ansluta")
    except requests.HTTPError: # om det blir ett HTTP-fel
        print("Fel, HTTP fel")
    except requests.JSONDecodeError: # om det inte går att avkoda JSON-data
        print("Fel, kunde inte avkoda JSON data")
    except requests.RequestException: # om det blir ett okänt fel
        print("Fel, okänt fel inträffade")


# Visa sökhistorik
def show_search_history():
    # försöker öppna filen history.json för att läsa in data
    try:
        with open("history.json", "r") as file_obj:
            # läs in data från filen
            data = file_obj.read()

            # om filen är tom, skriv ut att sökhistoriken är tom
            if not data.strip():
                print("Sökhistoriken är tom")
            else:
                # om filen inte är tom, läs in data och skriv ut sökhistoriken
                movie_history = json.loads(data)
                print("Sökhistorik:")
                # loopa igenom listan och skriv ut sökhistoriken
                for i, movie in enumerate(movie_history, 1):
                    print(str(i) + ". " + movie["search_string"]) # skriv ut värdet för nyckeln "search_string"
    # om filen inte finns eller om json-filen är trasig
    except (FileNotFoundError, json.JSONDecodeError):
        # skriv ut att filen inte finns eller är trasig
        print("Fel, filen finns ej eller är trasig")


# Sök efter en film baserat på något ord i filmens titel
def search_movie():
    # Fråga användaren efter en specifik film
    specific_movie = input("Ditt film val: ")
    # Lägg till filmen i URL:en
    req_url = url + "&s=" + specific_movie # &s= används för att söka efter en film baserat på något ord i filmens titel
    # Spara sökhistoriken
    save_searches(specific_movie)
    # Försöker ansluta till API:et
    try:
        r = requests.get(req_url) # get-metoden används för att hämta data från servern

        # Om anslutningen lyckas
        if r.status_code == 200:
            # Om responsen är False, skriv ut felmeddelandet
            if r.json().get("Response") == "False":
                print("Fel. " + r.json().get("Error", "Okänt fel")) # om det inte finns något felmeddelande, skriv ut "Okänt fel"
                input("Tryck på enter för att fortsätta")
                return # avsluta funktionen

            # Loopa igenom listan som vi får tillbaka och skriv ut informationen om filmerna
            for movie in r.json().get("Search"):
                print(movie["Title"] + " (" + movie["Year"] + ")")
                print("Typ: " + movie["Type"])
                print(movie["Poster"] + "\n")
            input("Tryck på enter för att fortsätta")
        else:
            # Om statuskoden inte är 200, skriv ut felmeddelandet
            print("Fel. Oväntad statuskod, förväntades, 200 (OK).\n")
            input("Tryck på enter för att fortsätta")

    # Felhantering
    except requests.ConnectionError: # om det inte går att ansluta till servern
        print("Fel, kunde inte ansluta till servern")
    except requests.Timeout: # om det tar för lång tid att ansluta
        print("Fel, tog för lång tid att ansluta")
    except requests.HTTPError: # om det blir ett HTTP-fel
        print("Fel, HTTP fel")
    except requests.JSONDecodeError: # om det inte går att avkoda JSON-data
        print("Fel, kunde inte avkoda JSON data")
    except requests.RequestException: # om det blir ett okänt fel
        print("Fel, okänt fel inträffade")

# Spara sökhistoriken
def save_searches(search_string):
    # försöker öppna filen history.json för att läsa in data
    try:
        with open("history.json", "r") as file_obj:
            data = file_obj.read()

            # om filen är tom, skapa en tom lista movie_history
            if not data.strip():
                movie_history = []
            else:
                # om filen inte är tom, läs in data
                movie_history = json.loads(data)

    # om filen inte finns eller om json-filen är trasig, skapa en tom lista movie_history
    except (FileNotFoundError, json.JSONDecodeError):
        movie_history = []

    # skapa ett nytt objekt för sökningen
    new_search = {
        "search_string": search_string
    }

    # om listan är större eller är lika med 5, ta bort det sista objektet
    if len(movie_history) >= 5:
        movie_history.pop()

    # lägg till nya sökningen i listan
    movie_history.insert(0, new_search) # nya sökningen lägg först med insert på index 0

    # försöker skriva till json-filen
    try:
        with open("history.json", "w") as file_obj: # öppna filen history.json för att skriva data
            json.dump(movie_history, file_obj, ensure_ascii=False , indent=4) # skriv data till filen
    except (FileNotFoundError, json.JSONDecodeError): # om filen inte finns eller om json-filen är trasig
        print("Fel. Det gick inte att spara json-filen")

