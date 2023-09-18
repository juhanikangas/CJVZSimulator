import mysql.connector as mc
from colorama import Fore, Back, Style

connection = mc.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='luukas',
         password='s87lk#4Mi1a',
         autocommit=True
        )
cursor = connection.cursor()

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
        elif selected_continent == "back":
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
        elif selected_country == "back":
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
        elif selected_airport == "BACK":
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

def choose_flight():
    departure_airport = {}
    destination_airport = {}
    while True:
        print(Fore.RED + "[BACK] " + Fore.RESET + "Go back")

        if bool(departure_airport):
            print(f"[1] Departure airport: {departure_airport['name']}")
        else:
            print("[1] Departure airport:")

        if bool(destination_airport):
            print(f"[2] Destination airport: {destination_airport['name']}")
        else:
            print("[2] Destination airport:")

        selected_airport = input("Select: ").upper()

        if selected_airport == "1":
            departure_airport_ident = choose_airport()
            query = f"SELECT name FROM airport WHERE ident='{departure_airport_ident}'"
            cursor.execute(query)
            results = []
            for i in cursor.fetchall():
                results.extend(i)
            departure_airport["name"] = results[0]
        elif selected_airport == "2":
            destination_airport_ident = choose_airport()
            query = f"SELECT name FROM airport WHERE ident='{destination_airport_ident}'"
            cursor.execute(query)
            results = []
            for i in cursor.fetchall():
                results.extend(i)
            destination_airport["name"] = results[0]
        elif selected_airport == "BACK":
            if bool(departure_airport) and bool(destination_airport):
                return f"{departure_airport['name']} to {destination_airport['name']}"
            else:
                return ""
        else:
            print("Invalid input")
