# use requests
import requests as r

# use shutil
import shutil as sh

# use ctypes
import ctypes as c

# use time as t
import time as t


# # get a random background image from unsplash
# response = r.get("https://source.unsplash.com/random/1920x1080")

# # save the image to a file and move to C:/Users/Public/Pictures/Backgrounds/background.jpg
# sh.copyfileobj(response.raw, open("C:/Users/Public/Pictures/Backgrounds/background.jpg", "wb"))

# use ctypes to set the background

# # repeat every 30 minutes
# t.sleep(1800)

response = r.get("https://source.unsplash.com/random/1920x1080") # get a random background image from unsplash

# complete all actions every 30 minutes
def loop_for_eternity(): 
    while True: 
        sh.copyfileobj(response.raw, open("C:/Users/Public/Pictures/Backgrounds/background.jpg", "wb")) # save the image to a file and move to C:/Users/Public/Pictures/Backgrounds/background.jpg
        c.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/Pictures/Backgrounds/background.jpg") # set the background
        t.sleep(1800) # repeat every 30 minutes
    
loop_for_eternity() # start the loop