#https://automatetheboringstuff.com/chapter18/

import pyautogui
import time
import os
# print(pyautogui.size())
# print(pyautogui.position())

# #pyautogui.move(0,100,duration=0.25)

# print(pyautogui.position())
# x = pyautogui.position()[0]
# print(x)

###Tøm papirkurven
# print(pyautogui.position()[0])
# print(pyautogui.position()[1])

# pyautogui.click(x=1365,y=756,duration=0.5)

# pyautogui.moveTo(x=59, y=39,duration=0.5)
# pyautogui.rightClick(x=59,y=39,duration=0.5)

# pyautogui.click(x=65,y=68,duration=0.5)
# time.sleep(5)
# pyautogui.press('enter')
######################################

###Kører musen hen til der hvor billedet kan findes
# os.chdir(r'C:\Users\KlausPC\Documents\VsCodePythonfiler\VirtualEnv')
# pngLoc = pyautogui.locateOnScreen(r'Udklip.PNG')
# pyautogui.click(pngLoc,duration=2.0)
#######################################

def activeWindows(title):
    aktiveWin = pyautogui.getAllTitles()
    maxwindows = []
    for elem in aktiveWin:
        if title.lower() in elem.lower():
            maxwindows.append(elem)
    if len(maxwindows)>0:
        return maxwindows
    else:
        return 'Har du stavet det korrekt?'

def activateWindowsbyTitle(titel):
    x=pyautogui.getWindowsWithTitle(titel)
    for elem in x:
        elem.activate()
        elem.maximize()

activateWindowsbyTitle(titel = 'Microsoft')
print(activeWindows('Microsoft'))

# for elem in activeWindows('chrome'):

# x = pyautogui.getWindowsWithTitle('Chrome')
# print(x)
    
    


