import cv2 as cv
import numpy as np
import pyautogui as pag
import win32api, win32con
from time import sleep

def leftclick(x,y,interval):
    win32api.SetCursorPos((x,y))
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    sleep(interval)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

def rightclick(x,y,interval):
    win32api.SetCursorPos((x,y))
    
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    sleep(interval)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)


def moveto(x,y):
    win32api.SetCursorPos((x,y))


def screenshot(filename, ColorTransfer):
    screenshot = pag.screenshot(filename)
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, ColorTransfer)
    
    
def s1_img_imread(filename):
    # The file to use to scan
    return cv.imread(filename, cv.IMREAD_ANYCOLOR)

   
def s2_img_matchTemplate(filename1,filename2, flags):
    # The file to use to scan
    return cv.matchTemplate(filename1,filename2, flags)
    

def s3_img_location(result, threshold):
    x = np.where(result <= threshold)
    y = list(zip(*x[::-1]))
    
    return y
    
    
    
    
    