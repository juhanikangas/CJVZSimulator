from colorama import Fore, Back, Style

from select_plane_menu import choose_plane
from select_flight_menu import choose_flight

def main_menu(flight_specs):
    while True:
        print("Main Menu")
        if "user_plane" in flight_specs:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Change airplane")
        else:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Choose airplane")
        if "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Change flight")
        else:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Choose flight")
        print(Fore.GREEN + "[3] " + Fore.RESET + "Start game")
        action = input("Select: ")
        if action == "1":
            flight_specs = choose_plane(flight_specs)
        elif action == "2":
            flight_specs = choose_flight(flight_specs)
        elif action == "3":
            # Must have flight and airplane selected to be able to start game
            print("Game started")
            break
        else:
            print("Invalid input")