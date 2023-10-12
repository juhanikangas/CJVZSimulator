import os

from colorama import Fore

def clear_flight_specs(flight_specs):
    # Change destination airport to departure airport after flight
    flight_specs["departure_airport_name"] = flight_specs["destination_airport_name"]
    flight_specs["departure_airport_ident"] = flight_specs["destination_airport_ident"]
    del flight_specs["destination_airport_name"]
    del flight_specs["destination_airport_ident"]
    return flight_specs


def end_screen(flight_specs):
    os.system('cls' if os.name == 'nt' else 'clear')
    input_is_invalid = False
    while flight_specs:
        if flight_specs["flight_successful"]:
            print(f"You succesfully landed at {flight_specs['destination_airport_name']}")
        else:
            print("You crashed! :(")
        print("Score: ")
        # print(f"Score: {flight_specs['score']}")
        print("Fly again? ")
        print(Fore.GREEN + "[Y] " + Fore.RESET + "Yes")
        print(Fore.GREEN + "[N] " + Fore.RESET + "No")
        if input_is_invalid:
            print(Fore.RED + "Invalid input" + Fore.RESET)

        selected_option = input("Select: ").upper()

        if selected_option == "Y" or selected_option == "YES":
            flight_specs = clear_flight_specs(flight_specs)
            return flight_specs
        elif selected_option == "N" or selected_option == "NO":
            print("Thanks for playing!")
            return False
        else:
            input_is_invalid = True
            os.system('cls' if os.name == 'nt' else 'clear')
