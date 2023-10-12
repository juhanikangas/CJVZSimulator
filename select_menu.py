import os
import time

from pynput import keyboard

selected_option = 0
menu_options = None
selected_menu_option = None
menu_title = None

def select_menu(menu_options_arg, menu_title_arg=None):
    global selected_option, menu_options, menu_title

    menu_options = menu_options_arg
    if menu_title_arg:
        menu_title = menu_title_arg

    def update_menu():
        global menu_options
        os.system('cls' if os.name == 'nt' else 'clear')
        if menu_title:
            print(menu_title)
        for i, option in enumerate(menu_options):
            if i == selected_option:
                print(f"> {option}")
            else:
                print(f"  {option}")


    def on_key_press(key):
        global menu_options, selected_option

        if key == keyboard.Key.down:
            selected_option = (selected_option + 1) % len(menu_options)
            update_menu()
        elif key == keyboard.Key.up:
            selected_option = (selected_option - 1) % len(menu_options)
            update_menu()
        elif key == keyboard.Key.enter:
            global selected_menu_option
            selected_menu_option = menu_options[selected_option]
            keyboard_listener.stop()
            exit()

    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    keyboard_listener.start()

    update_menu()
    keyboard_listener.join()

    time.sleep(0.1)

    return selected_menu_option
