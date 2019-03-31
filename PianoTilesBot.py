from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time

box = [
    (190 ,825, 315, 850),
    (317 ,825, 442, 850),
    (452 ,825, 577, 850),
    (587 ,825, 712, 850)
]

def Click(cordinates):
    pyautogui.click(cordinates)
    time.sleep(.5)

def imageGrab(i):
    global box
    image = ImageGrab.grab(box[i])
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(a.sum(), i)
    #time.sleep(0.2)
    return a.sum()

if __name__ == "__main__":
    coordinates = [
        (250, 650),
        (388, 650),
        (518, 650),
        (650, 650)
    ]
    while True:
        for i in range(0, 4):
            #imageGrab(i)
            if(imageGrab(i) > 5000):
                Click(coordinates[i])