from colorama import Fore, Back, Style

from select_plane_menu import choose_plane
from select_flight_menu import choose_flight

def main_menu():
    user_plane = ""
    user_flight = ""
    while True:
        print("Main Menu")
        print(f"[1] Choose airplane {user_plane}")
        print(f"[2] Choose flight {user_flight}")
        print(Fore.GREEN + "[3] " + Fore.RESET + "Start game")
        action = input("Select: ")
        if action == "1":
            user_plane = choose_plane()
        elif action == "2":
            user_flight = choose_flight()
        elif action == "3":
            print("Game started")
            break
        else:
            print("Invalid input")
