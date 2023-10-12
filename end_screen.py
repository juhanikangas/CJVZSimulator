import os

from colorama import Fore

def clear_flight_specs(flight_specs):
    # Change destination airport to departure airport after flight
    flight_specs["departure_airport_name"] = flight_specs["destination_airport_name"]
    flight_specs["departure_airport_ident"] = flight_specs["destination_airport_ident"]
    del flight_specs["destination_airport_name"]
    del flight_specs["destination_airport_ident"]
    flight_specs["player_exp"] += flight_specs["flight_exp"]
    del flight_specs["flight_exp"]
    flight_specs["flight_successful"] = False
    return flight_specs


def end_screen(flight_specs):
    os.system('cls' if os.name == 'nt' else 'clear')
    input_is_invalid = False
    while flight_specs:
        if flight_specs["flight_successful"]:
            print(f"You successfully landed at {flight_specs['destination_airport_name']}!")
        else:
            print("Oopsie poopsie, you crashed and caused an international tragedy just like Mr. Van Zanten :(")
        print(f"You got {flight_specs['flight_exp']} exp")
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
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thanks for playing!")
            return False
        else:
            input_is_invalid = True
            os.system('cls' if os.name == 'nt' else 'clear')
