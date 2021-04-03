from pynput.keyboard import Controller
from time import sleep
import sys

if __name__ == '__main__':
    print("Started")
    keyboard = Controller()
    while True:
        import keyboard

        while True:
            sleep(.5)

            if keyboard.is_pressed('x'):
                sys.exit()

            if keyboard.is_pressed('q'):
                keyboard.press("w")

            if keyboard.is_pressed('ctrl+q'):
                keyboard.release("w")

            if keyboard.is_pressed('e'):
                break

    print("done")
