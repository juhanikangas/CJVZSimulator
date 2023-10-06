import os
import sys
import time
import threading

from pyfiglet import Figlet

figlet = Figlet()
figlet.setFont(font="standard")
name = "CJVZSimulator"
lock = threading.Lock()
lines = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

def print_char(char):
    with lock:
        sys.stdout.write(char)
        sys.stdout.flush()

def print_smoothly(name):
    global lines
    for char in name:
        letter_ascii_art = figlet.renderText(char)
        letter_lines = letter_ascii_art.split("\n")
        i = 0


        for letter_line in letter_lines:
            lines[i].append(letter_line)
            i += 1

    lines = lines[:-2]

    output = '\n'.join([' '.join(line) for line in lines])

    threads = [threading.Thread(target=print_char, args=(char,)) for char in output]

    for thread in threads:
        thread.start()
        time.sleep(0.0001)

    for thread in threads:
        thread.join()


def start_screen():
    print_smoothly(name)
    time.sleep(3)
    os.system('cls')
