import os

from colorama import Fore, Back, Style

from planes import plane_options

# Shows the options for planes and asks what plane the user wants to use
def choose_plane(flight_specs):
    input_is_invalid = False
    not_enough_exp = False
    planes = plane_options()
    show_full_plane_status = False
    os.system('cls' if os.name == 'nt' else 'clear')
    while flight_specs:
        print("Choose plane model:")
        print(Fore.RED + '[BACK]' + Fore.RESET, ' Go back to main menu')
        if show_full_plane_status:
            print(Fore.YELLOW + '[INFO]' + Fore.RESET, 'Close plane info')
        else:
            print(Fore.YELLOW + '[INFO]' + Fore.RESET + ' Open plane info')
        print(f"Your exp: {flight_specs['player_exp']}")
        for i, plane in enumerate(planes):
            if plane.exp <= flight_specs["player_exp"]:
                print(Fore.GREEN + '[' + str(i + 1) + ']', Fore.RESET + plane.model)
            else:
                print(Fore.RED + '[' + str(i + 1) + ']', Fore.RESET + plane.model)
            if show_full_plane_status:
                print(f'  Nickname: {plane.name} \n  Weight:  {plane.weight}kg \n  Flight speed: {plane.speed}km/h \n  HP: {plane.hp}, \n  Exp required: {plane.exp}')
        if input_is_invalid:
            print(Fore.RED + "Invalid input" + Fore.RESET)
        if not_enough_exp:
            print(Fore.RED + "Not enough exp" + Fore.RESET)
        chosen_plane_index = input("Select: ").upper()
        try:
            chosen_plane_index = int(chosen_plane_index)
            if chosen_plane_index > len(planes)-1 or chosen_plane_index < 1:
                input_is_invalid = True
                not_enough_exp = False
            elif flight_specs["player_exp"] < planes[chosen_plane_index - 1].exp:
                not_enough_exp = True
                input_is_invalid = False
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                flight_specs["user_plane"] = planes[chosen_plane_index - 1]
                os.system('cls' if os.name == 'nt' else 'clear')
                return flight_specs
        except ValueError:
            if chosen_plane_index == "INFO":
                not_enough_exp = False
                input_is_invalid = False
                show_full_plane_status = not show_full_plane_status
            elif chosen_plane_index == 'BACK':
                os.system('cls' if os.name == 'nt' else 'clear')
                return flight_specs
            else:
                input_is_invalid = True
                not_enough_exp = False
                os.system('cls' if os.name == 'nt' else 'clear')
