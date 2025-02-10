from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("API_KEY")
url = "https://www.omdbapi.com/?apikey=" + api_key

def search_specific_movie():
    pass

def show_search_history():
    pass

def search_movie():
    pass
