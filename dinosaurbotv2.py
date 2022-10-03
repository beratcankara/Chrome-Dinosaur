#dinazorbotv2
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
import keyboard
#pyautogui.displayMousePosition()
class Kordinatlar():
    replay_butonu = (645,415)
    dinazor = (121,429)
    uzaklık = 215              
    bitki = (dinazor[0]+uzaklık,dinazor[1],dinazor[0]+uzaklık+40,dinazor[1]+30)
    safe_zone = 1455
    gray_zone = 1200
def yeniden_baslat():
    pyautogui.click(Kordinatlar.replay_butonu)
def zipla():
    pyautogui.keyDown("space")                             
    time.sleep(0.05)
    pyautogui.keyUp("space")
def bitki_tespit():
    image = ImageGrab.grab(Kordinatlar.bitki)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()
def main():
    yeniden_baslat()
    while keyboard.is_pressed("q") == False:
        if bitki_tespit() == Kordinatlar.safe_zone or bitki_tespit() == Kordinatlar.gray_zone:
            continue;
        zipla()
        time.sleep(0.03)
        
while 1:
    main()