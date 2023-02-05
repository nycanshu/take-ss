#screenshot application by okay.anshu
import time 
import pyautogui
from PIL import Image
import tkinter as tk

#creating a function for taking the screenshot

def screenshot():
    #picking a random name for the ss image
    
    name = int(round(time.time()*1000))
    
    #storing the image file into an address
    #user need to create a folder for storing the clicked img
    #then replace this file address to your file address.
    name = f"D:/Coding files/pyhton/screenshot/screenshot_saved/{name}.png"
    
    #calling the predefined screenshot method from pyautogui package 
    
    img = pyautogui.screenshot(name)
    #using the Pillow module to show the image
    img.show()
    
#working for the gui 

#creating a basic frame and adding two buttons one is for take ss one is for exit.

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
#assigning the screenshot command to the take screenshot button
button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
#assigning the exit command to the exit button
button.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    text= "EXIT",
    command=quit
)

close.pack(side=tk.LEFT)

root.mainloop()

#this code is contributed by Himanshu
