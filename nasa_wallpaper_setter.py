import requests
from bs4 import BeautifulSoup
from os import path, getcwd
import ctypes
import time
import os


def set_wallpaper(image):

    # for Windows
    # SPI_SETDESKWALLPAPER = 20
    # ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, 0)

    os.system(
        'gsettings set org.gnome.desktop.background picture-uri "' +
        image +
        '"')


def getimage(url):
    # Get the data from the website
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    date = soup.findAll("p")[1].text.strip()
    image = soup.find("img")
    url += image["src"]
    page = requests.get(url)
    filename = f"image {date}.jpg"
    # Create the .jpg file
    with open(filename, "wb") as f:
        f.write(page.content)
    # Gets the current directory, and creates the directory of the .jpg file out of it.
    # for Windows
    #filepath = getcwd() + r"\\" + filename
    filepath = "file:///" + getcwd() + r"/" + filename
    # Set the wallpaper to the .jpg file
    set_wallpaper(filepath)


url = "https://apod.nasa.gov/"

getimage(url)

# while True:
#    getimage(url)
#    time.sleep(3600) #Calls getimage() every hour the program is ran
