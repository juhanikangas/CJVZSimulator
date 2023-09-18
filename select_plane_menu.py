from planes import plane_options
from colorama import Fore, Back, Style


# Shows the options for planes and asks what plane the user wants to use
def choose_plane():
    user_plane = False
    planes = plane_options()
    show_full_plane_status = False
    while not user_plane:
        print("Choose plane model:")
        print(Fore.RED + '[back]' + Fore.RESET, ' Go back to main menu')
        if show_full_plane_status:
            print(Fore.YELLOW + '[info]' + Fore.RESET, 'Close plane info')
        else:
            print(Fore.YELLOW + '[info]' + Fore.RESET + ' Open plane info')
        for i, plane in enumerate(planes):
            print(Fore.GREEN + '[' + str(i+1) + ']', Fore.RESET + plane.model)
            if show_full_plane_status:
                print("  Nickname:", plane.name, "\n  Weight:",
                      f'{plane.weight}kg', "\n  Flight speed:", f'{plane.flight_speed}km/h', "\n  Hp:", plane.hp)
        chosen_plane_index = input("Type option: ")
        try:
            chosen_plane_index = int(chosen_plane_index)
            if chosen_plane_index > len(planes) or chosen_plane_index < 1:
                print("Invalid option.")
            else:
                user_plane = planes[chosen_plane_index - 1]
        except ValueError:
            if chosen_plane_index == "info":
                show_full_plane_status = not show_full_plane_status
            elif chosen_plane_index == 'back':
                return False
            else:
                print("Invalid option")
    return user_plane
