from select_menu import select_menu

def clear_flight_specs(flight_specs):
    # Change destination airport to departure airport after flight
    flight_specs["departure_airport_name"] = flight_specs["destination_airport_name"]
    flight_specs["departure_airport_ident"] = flight_specs["destination_airport_ident"]
    del flight_specs["destination_airport_name"]
    del flight_specs["destination_airport_ident"]
    return flight_specs


def end_screen(flight_specs):
    print(f"You succesfully landed at {flight_specs['destination_airport_name']}")
    print("Points: ")
    # print(f"Points: {flight_specs['points']}")
    action = input("Fly again? (yes/no) ").lower()
    if action == "yes":
        flight_specs = clear_flight_specs(flight_specs)
        return flight_specs
    elif action == "no":
        print("Thanks for playing!")
        return False
    else:
        print("Invalid input")
