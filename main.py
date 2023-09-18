from planes import plane_options


# Shows the options for planes and asks what plane the user wants to use
def choose_plane():
    user_plane = False
    planes = plane_options()
    show_full_plane_status = False
    while not user_plane:
        print("Choose plane model:")
        for i, plane in enumerate(planes):
            print(f'[{i + 1}]', plane.model)
            if show_full_plane_status:
                print("Nickname: ", plane.name, "\nWeight: ", plane.weight, "\nFlight speed", plane.flight_speed)
        chosen_plane_index = int(input("Type model number to continue or \ntype 0 to see more info of the planes: "))
        if chosen_plane_index > len(planes) or chosen_plane_index < 0:
            print("Invalid option.")
        elif chosen_plane_index == 0:
            show_full_plane_status = True
        else:
            user_plane = planes[chosen_plane_index - 1]
    return user_plane


def main():

    user_plane = choose_plane()
    print(user_plane)
    return 0


if __name__ == '__main__':
    main()
