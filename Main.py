# Importera movies.py
import movies

# Huvudmeny
def main_menu():
    # Skapa en evighets-loop som körs tills användaren väljer att avsluta programmet
    while True:
        print("***************************************")
        print("             Huvudmeny")
        print("***************************************")

        print("\n1. Sök efter film baserat på exakt titel")
        print("2. Sök efter film baserat på något ord i filmens titel")
        print("3. Visa sökhistorik")
        print("4. Avsluta programmet\n")
        menu_choice = input("Ditt val: ") # Fråga användaren efter ett val

        # Kontrollera vilket val användaren gjort
        if menu_choice == "1":
            movies.search_specific_movie()
        elif menu_choice == "2":
            movies.search_movie()
        elif menu_choice == "3":
            movies.show_search_history()
        elif menu_choice == "4":
            break # Avsluta programmet
        else:
            print("Felaktigt menyval!")

# Starta programmet
main_menu()


