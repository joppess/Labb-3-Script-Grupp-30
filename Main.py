import movies

def main_menu():
    while True:
        print("***************************************")
        print("             Huvudmeny")
        print("***************************************")

        print("\n1. Sök efter film baserat på exakt titel")
        print("2. Sök efter film baserat på något ord i filmens titel")
        print("3. Visa sökhistorik")
        print("4. Avsluta programmet\n")
        menu_choice = input("Ditt val: ")
h
        if menu_choice == "1":
            movies.search_specific_movie()
        elif menu_choice == "2":
            movies.search_movie()
        elif menu_choice == "3":
            movies.show_search_history()
        elif menu_choice == "4":
            break
        else:
            print("Felaktigt menyval")

main_menu()

