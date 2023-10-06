import os

from pynput import keyboard

selected_option = 0
menu_options = None
selected_menu_option = None
def kb_listener(arg_menu_options):
    global selected_option
    global menu_options
    menu_options = arg_menu_options
    def update_menu():
        global menu_options
        os.system('cls')
        for i, option in enumerate(menu_options):
            if i == selected_option:
                print(f"> {option}")
            else:
                print(f"  {option}")


    def on_key_press(key):
        global menu_options
        global selected_option
        if key == keyboard.Key.down:
            selected_option = (selected_option + 1) % len(menu_options)
            update_menu()
        elif key == keyboard.Key.up:
            selected_option = (selected_option - 1) % len(menu_options)
            update_menu()
        elif key == keyboard.Key.enter:
            global selected_menu_option
            selected_menu_option = menu_options[selected_option]
            exit()


    keyboard_listener = keyboard.Listener(on_press=on_key_press)

    keyboard_listener.start()

    update_menu()

    keyboard_listener.join()

    return selected_menu_option
