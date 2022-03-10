"""
Takes a series of screenshots with input in the respec-screen in ELDEN RING
Uses OCR to read values and compile them into a simple table.
"""
import pyautogui
from os import path


class EldenEye:
    def __init__(self):
        # search for windowed Elden Ring Icon and offset image map by it's location
        self.offset = pyautogui.locateOnScreen('screen_key.png', region=(0,0, 500,500))

    def reconfigure(self, attribute):
        """ Reset to position of one attribute, relative to the offset icon"""
        with open('locations.csv', 'a') as locations:
            input("Top left: (press enter)")
            # move the cursor to the top left of the intended capture box
            pos = []
            pos.append(pyautogui.position()[0]-self.offset.left)
            pos.append(pyautogui.position()[1]-self.offset.top)
            input("Bottom Right: (press enter)")
            # move the cursor to the bottom of the intended capture box
            pos.append(pyautogui.position()[0]-self.offset.left-pos[0])
            pos.append(pyautogui.position()[1]-self.offset.top-pos[1])
            print(f'{attribute},{pos}\n')
            locations.write(f'{attribute},{pos}\n')

    def capture_all(self):
        pass

if __name__ == "__main__":
    Eye = EldenEye()
    for i in range(2):
        Eye.reconfigure(input('Attribute: '))