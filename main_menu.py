import os

from colorama import Fore

from select_plane_menu import choose_plane
from select_flight_menu import choose_flight
from select_menu import select_menu
from planes import plane_options

def calculate_flight_duration(flight_specs):
    distance_km = flight_specs["distance_km"]
    speed = flight_specs["user_plane"].speed
    # Define the valid range for distance and speed
    min_distance_km = 10
    max_distance_km = 20000
    min_speed_kmh = 0
    max_speed_kmh = 0

    for i, plane in enumerate(plane_options()):
        if not i:
            min_speed_kmh = plane.speed
            max_speed_kmh = plane.speed
        if plane.speed < min_speed_kmh:
            min_speed_kmh = plane.speed
        if plane.speed > max_speed_kmh:
            max_speed_kmh = plane.speed
    # Ensure the input values are within the valid range
    if not (min_distance_km <= distance_km <= max_distance_km) or not (min_speed_kmh <= speed <= max_speed_kmh):
        return "Invalid input"

    # Define the range for scaled flight duration (in seconds)
    min_scaled_duration = 15
    max_scaled_duration = 300

    # Calculate the scaled duration using linear scaling
    scaled_duration = min_scaled_duration + (max_scaled_duration - min_scaled_duration) * (
        (distance_km - min_distance_km) / (max_distance_km - min_distance_km)
    ) / (speed / min_speed_kmh)

    # Ensure the duration is within the specified range
    scaled_duration = max(min_scaled_duration, min(scaled_duration, max_scaled_duration))

    return int(round(scaled_duration))


def main_menu(flight_specs):
    os.system('cls' if os.name == 'nt' else 'clear')
    while flight_specs["menu"] == 0:
        plane_selected = bool("user_plane" in flight_specs)
        flight_selected = bool("departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs)
        plane_and_flight_selected = bool("user_plane" in flight_specs and "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs)
        print("Main menu")
        if plane_selected:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Change airplane (" + flight_specs['user_plane'].model + ")")
        else:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Choose airplane")

        if flight_selected:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Change flight (" + flight_specs['departure_airport_name'] + " -> " + flight_specs['destination_airport_name'] + ")")
        else:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Choose flight")

        if plane_and_flight_selected:
            flight_specs["flight_duration"] = calculate_flight_duration(flight_specs)
            print(Fore.GREEN + "[3] " + Fore.RESET + "Start game " + "(Flight duration: " + str(flight_specs["flight_duration"]) + ")")

        action = input("Select: ")

        if action == "1":
            flight_specs = choose_plane(flight_specs)
        elif action == "2":
            flight_specs = choose_flight(flight_specs)
        elif action == "3":
            if plane_and_flight_selected:
                # start_flight()
                return flight_specs
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid input")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input")


