from selectPlainMenu import choose_plane


def main():
    user_plane = choose_plane()
    print("You chose", user_plane.model, "as your plane for the flight.")
    print(user_plane)
    return 0


if __name__ == '__main__':
    main()
