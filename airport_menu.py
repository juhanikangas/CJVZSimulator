import mysql.connector as mc

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
    print("[back] Go back")
    for continent in continents:
        print(f"[{continent_codes[continents.index(continent)]}] {continent}")
    selected_continent = input("Select continent: ")
    if selected_continent == "back":
        return [1, False]
    else:
        return [2, selected_continent]

def select_country(continent):
    query = f"SELECT DISTINCT name, iso_country FROM country WHERE continent='{continent}'"
    cursor.execute(query)
    results = cursor.fetchall()

    countries = {}

    for row in results:
        iso_country = row[1]
        country_name = row[0]
        countries[iso_country] = country_name

    print("[back] Go back")
    for country in countries:
        print(f"[{country}] {countries[country]}")
    selected_country = input("Select country: ")

    if selected_country == "back":
        return [1, ""]
    else:
        return [3, selected_country]


def select_airport(country):
    query = f"SELECT DISTINCT name, ident FROM airport WHERE iso_country='{country}'"
    cursor.execute(query)
    results = cursor.fetchall()
    airports = [row[0] for row in results]
    idents = [row[1] for row in results]

    print("[back] Go back")
    for airport in airports:
        print(f"[{idents[airports.index(airport)]}] [{airport}]")

    selected_airport = input("Select airport: ")

    if selected_airport == "back":
        return [2, False]
    else:
        return [4, selected_airport]


def main():
    menu = 1
    while menu > 0 :
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
            menu = data[0]
            airport = data[1]
    print(airport)


main()
