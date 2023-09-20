import mysql.connector as mc
from colorama import Fore, Back, Style
import geopy.distance

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

def select_continent():
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

    while True:
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        for continent in continents:
            print(f"[{continent_codes[continents.index(continent)]}] {continent}")

        selected_continent = input("Select continent: ").upper()

        if selected_continent in continent_codes:
            return [2, selected_continent]
        elif selected_continent == return_code:
            return [0, False]
        else:
            print("Invalid continent")


def select_country(continent):
    query = f"SELECT DISTINCT name, iso_country FROM country WHERE continent='{continent}'"
    cursor.execute(query)
    results = cursor.fetchall()

    country_codes = [row[1] for row in results]
    countries = {}

    for row in results:
        country_name = row[0]
        iso_country = row[1]
        countries[iso_country] = country_name

    while True:
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        for country in countries:
            print(f"[{country}] {countries[country]}")
        selected_country = input("Select country: ").upper()

        if selected_country in country_codes:
            return [3, selected_country]
        elif selected_country == return_code:
            return [1, False]
        else:
            print("Invalid country")


def select_airport(country):
    query = f"SELECT name, ident FROM airport WHERE iso_country='{country}'"
    cursor.execute(query)
    results = cursor.fetchall()
    airports = [row[0] for row in results]
    airport_idents = [row[1] for row in results]

    while True:
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        for airport in airports:
            print(f"[{airport_idents[airports.index(airport)]}] [{airport}]")

        selected_airport = input("Select airport: ").upper()

        if selected_airport in airport_idents:
            return [1, selected_airport]
        elif selected_airport == return_code:
            return [2, False]
        else:
            print("Invalid airport")


def choose_airport():
    menu = 1
    while True:
        if menu == 0:
            return False # Go back to select flight menu
        if menu == 1:
            data = select_continent()
            menu = data[0]
            continent = data[1]
        elif menu == 2:
            data = select_country(continent)
            menu = data[0]
            country = data[1]
        elif menu == 3:
            data = select_airport(country)
            if data[0] == 1:
                menu = data[0]
                airport = data[1]
                break
            elif data[0] == 2:
                menu = data[0]

    return airport


def choose_flight(flight_specs):
    while True:
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")
        if "departure_airport_name" in flight_specs:
            print(f"[1] Departure airport: {flight_specs['departure_airport_name']}")
        else:
            print("[1] Departure airport:")

        if "destination_airport_name" in flight_specs:
            print(f"[2] Destination airport: {flight_specs['destination_airport_name']}")
        else:
            print("[2] Destination airport:")

        selected_airport = input("Select: ").upper()

        if selected_airport == "1":
            departure_airport_ident = choose_airport()
            departure_airport_name = get_airport_name(departure_airport_ident)
            flight_specs["departure_airport_name"] = departure_airport_name
        elif selected_airport == "2":
            destination_airport_ident = choose_airport()
            destination_airport_name = get_airport_name(destination_airport_ident)
            flight_specs["destination_airport_name"] = destination_airport_name
        elif selected_airport == return_code:
            if "departure_airport_name" in flight_specs and "destination_airport_name" in flight_specs and "distance_km" not in flight_specs:
                flight_specs["distance_km"] = get_distance(departure_airport_ident, destination_airport_ident)
            return flight_specs
        else:
            print("Invalid input")

def get_airport_name(airport_ident):
    query = f"SELECT name FROM airport WHERE ident='{airport_ident}'"
    cursor.execute(query)
    results = []
    for i in cursor.fetchall():
        results.extend(i)
    return results[0]


def get_coords(airport_ident):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident='{airport_ident}'"

    cursor.execute(sql)
    coords = cursor.fetchone()

    return coords

def get_distance(departure_airport_ident, destination_airport_ident):
    coords1 = get_coords(departure_airport_ident)
    coords2 = get_coords(destination_airport_ident)

    distance_km = round(geopy.distance.geodesic(coords1, coords2).km)
    return distance_km
