from main_menu import main_menu
from start_screen import start_screen
from end_screen import end_screen

flight_specs = {
        "menu": 0,
        "exp": 0
    }

def main():
    global flight_specs
    # start_screen()

    while flight_specs:
        flight_specs = main_menu(flight_specs)
        # flight_specs = flight(flight_specs)
        flight_specs = end_screen(flight_specs)


if __name__ == '__main__':
    main()
