from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

counter = 1

class Cordinates:
    replayBtn = (480, 460)
    dinosaur = (209, 469)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    global counter
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print(f'Jump {counter}')
    counter += 1
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinosaur[0] + 60, Cordinates.dinosaur[1], Cordinates.dinosaur[0] + 100, Cordinates.dinosaur[1] + 30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

if __name__ == "__main__":
    restartGame()
    while True:
        if(imageGrab() != 1447):
            pressSpace()
            time.sleep(0.1)