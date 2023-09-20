from colorama import Fore, Back, Style

from select_plane_menu import choose_plane
from select_flight_menu import choose_flight

def main_menu(flight_specs):
    while True:
        plane_selected = bool("user_plane" in flight_specs)
        flight_selected = bool("departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs)
        plane_and_flight_selected = bool("user_plane" in flight_specs and "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs)
        print("Main Menu")

        if plane_selected:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Change airplane")
        else:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Choose airplane")

        if flight_selected:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Change flight")
        else:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Choose flight")

        if plane_and_flight_selected:
            print(Fore.GREEN + "[3] " + Fore.RESET + "Start game")

        action = input("Select: ")

        if action == "1":
            flight_specs = choose_plane(flight_specs)
        elif action == "2":
            flight_specs = choose_flight(flight_specs)
        elif action == "3":
            if plane_and_flight_selected:
                print("Game started")
                break
            else:
                print("Invalid input")
        else:
            print("Invalid input")