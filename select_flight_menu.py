import os
import time

import mysql.connector as mc
import geopy.distance
from colorama import Fore

from select_menu import select_menu

connection = mc.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='luukas',
    password='s87lk#4Mi1a',
    autocommit=True
)
cursor = connection.cursor()
return_code = "BACK"

def get_airport_name(airport_ident):
    query = f"SELECT name FROM airport WHERE ident='{airport_ident}'"
    cursor.execute(query)
    results = []
    for i in cursor.fetchall():
        results.extend(i)
    return results[0]


def get_coords(airport_ident):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{airport_ident}'"

    cursor.execute(sql)
    coords = cursor.fetchone()

    return coords


def get_distance(departure_airport_ident, destination_airport_ident):
    coords1 = get_coords(departure_airport_ident)
    coords2 = get_coords(destination_airport_ident)

    distance_km = round(geopy.distance.geodesic(coords1, coords2).km)
    return distance_km


def select_continent(flight_specs):
    query = f"SELECT DISTINCT continent FROM airport"
    cursor.execute(query)
    results = cursor.fetchall()

    continent_codes = [row[0] for row in results]

    continents = [
        "North America",
        "Oceania",
        "Africa",
        "Antarctica",
        "Europe",
        "Asia",
        "South America"
    ]

    input_is_invalid = False

    while flight_specs["menu"] == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        for continent in continents:
            print(f"[{continent_codes[continents.index(continent)]}] {continent}")
        if input_is_invalid:
            print(Fore.RED + "Invalid continent" + Fore.RESET)

        selected_continent = input("Select continent: ").upper()

        if selected_continent in continent_codes:
            flight_specs["menu"] = 2
            return flight_specs, selected_continent
        elif selected_continent == return_code:
            flight_specs["menu"] = 0
            return flight_specs, None
        else:
            input_is_invalid = True


def select_country(flight_specs, continent):
    query = f"SELECT DISTINCT country.name, country.iso_country FROM airport INNER JOIN country ON country.iso_country = airport.iso_country WHERE country.continent='{continent}' AND type='large_airport';"
    cursor.execute(query)
    results = cursor.fetchall()

    country_codes = [row[1] for row in results]
    countries = {}

    for row in results:
        country_name = row[0]
        iso_country = row[1]
        countries[iso_country] = country_name

    input_is_invalid = False

    while flight_specs["menu"] == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        for country in countries:
            print(f"[{country}] {countries[country]}")
        if input_is_invalid:
            print(Fore.RED + "Invalid country" + Fore.RESET)

        selected_country = input("Select country: ").upper()

        if selected_country in country_codes:
            flight_specs["menu"] = 3
            return flight_specs, selected_country
        elif selected_country == return_code:
            flight_specs["menu"] = 1
            return flight_specs, None
        else:
            input_is_invalid = True


def select_airport(flight_specs, country):
    query = f"SELECT name, ident FROM airport WHERE iso_country='{country}' AND (type='medium_airport' OR type='large_airport')"
    cursor.execute(query)
    results = cursor.fetchall()
    airports = [row[0] for row in results]
    airport_idents = [row[1] for row in results]

    input_is_invalid = False
    airport_already_selected = False
    while flight_specs["menu"] == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        for airport in airports:
            print(f"[{airport_idents[airports.index(airport)]}] [{airport}]")
        if input_is_invalid:
            print(Fore.RED + "Invalid airport" + Fore.RESET)
            input_is_invalid = False
        if airport_already_selected:
            print(Fore.RED + "Airport already selected" + Fore.RESET)
            airport_already_selected = False
        selected_airport = input("Select airport: ").upper()

        if selected_airport in airport_idents:
            if selected_airport in flight_specs.values():
                airport_already_selected = True
            else:
                flight_specs["menu"] = 0
                return flight_specs, selected_airport
        elif selected_airport == return_code:
            flight_specs["menu"] = 2
            return flight_specs, None
        else:
            input_is_invalid = True


def choose_airport(flight_specs):
    flight_specs["menu"] = 1
    while flight_specs:
        if flight_specs["menu"] == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            return flight_specs, None  # Go back to select flight menu
        elif flight_specs["menu"] == 1:
            flight_specs, continent = select_continent(flight_specs)
        elif flight_specs["menu"] == 2:
            flight_specs, country = select_country(flight_specs, continent)
        elif flight_specs["menu"] == 3:
            flight_specs, airport = select_airport(flight_specs, country)
            if airport is not None:
                os.system('cls' if os.name == 'nt' else 'clear')
                return flight_specs, airport


def choose_flight(flight_specs):
    os.system('cls' if os.name == 'nt' else 'clear')
    while flight_specs["menu"] == 0:
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        if "departure_airport_name" in flight_specs:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Departure airport: " + flight_specs['departure_airport_name'])
        else:
            print(Fore.GREEN + "[1] " + Fore.RESET + "Departure airport:")

        if "destination_airport_name" in flight_specs:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Destination airport: " + flight_specs['destination_airport_name'])
        else:
            print(Fore.GREEN + "[2] " + Fore.RESET + "Destination airport:")

        selected_airport = input("Select: ").upper()

        if selected_airport == "1":
            flight_specs, ident = choose_airport(flight_specs)
            if ident:
                flight_specs["departure_airport_ident"] = ident
                flight_specs["departure_airport_name"] = get_airport_name(flight_specs["departure_airport_ident"])
                if "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs:
                    flight_specs["distance_km"] = get_distance(flight_specs["departure_airport_ident"],flight_specs["destination_airport_ident"])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    flight_specs["menu"] = 0
                    return flight_specs
        elif selected_airport == "2":
            flight_specs, ident = choose_airport(flight_specs)
            if ident:
                flight_specs["destination_airport_ident"] = ident
                flight_specs["destination_airport_name"] = get_airport_name(flight_specs["destination_airport_ident"])
                if "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs:
                    if "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs:
                        flight_specs["distance_km"] = get_distance(flight_specs["departure_airport_ident"], flight_specs["destination_airport_ident"])
                        os.system('cls' if os.name == 'nt' else 'clear')
                        flight_specs["menu"] = 0
                        return flight_specs
        elif selected_airport == return_code:
            if "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs:
                flight_specs["distance_km"] = get_distance(flight_specs["departure_airport_ident"],flight_specs["destination_airport_ident"])
                os.system('cls' if os.name == 'nt' else 'clear')
                flight_specs["menu"] = 0
                return flight_specs
        else:
            input_is_valid = False
