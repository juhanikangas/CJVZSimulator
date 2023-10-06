from main_menu import main_menu
from start_screen import start_screen
from end_screen import end_screen

# os.system('cls' if os.name == 'nt' else 'clear')
def main():
    flight_specs = {
        "menu": 0
    }
    # start_screen()

    while flight_specs:
        flight_specs = main_menu(flight_specs)
        # flight_specs = flight(flight_specs)
        flight_specs = end_screen(flight_specs)



if __name__ == '__main__':
    main()
