# use requests
import requests as r

# use ctypes
import ctypes as c

# use time
import time as t


path = "C:\\Users\\Public\\Pictures\\Backgrounds\\background.jpg" # set the path to the background

def chg_bkgrnd(): # function to change the background
    i = True
    while(i == True): # loop to change the background
        # get a random background from unsplash.com using requests
        resp = r.get("https://source.unsplash.com/random/1920x1080")
        c.windll.user32.SystemParametersInfoW(
            20, 0, path, 0)  # set the background using ctypes
        file = open(path, 'wb') # use open to write the file to the path
        file.write(resp.content) # use write to write the content of the response to the file
        file.close() # close the file
        t.sleep(1800)  # sleep for 5 seconds
        
    
# call the function
chg_bkgrnd()