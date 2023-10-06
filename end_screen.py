def clear_flight_specs(flight_specs):
    return flight_specs

def end_screen(flight_specs):
    print(f"You succesfully landed at {flight_specs['destination_airport_name']}")
    print("Points: ")
    # print(f"Points: {flight_specs['points']}")
    action = input("Fly again? (y/n) ")
    if action == "y":
        flight_specs = clear_flight_specs(flight_specs)
        return flight_specs
    elif action == "n":
        print("Thanks for playing!")
        return False
    else:
        print("Invalid input")
