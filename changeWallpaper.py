'''
1. Download a favorite wallpaper from unsplash
2. Save to a temp directory
3. Set wallpaper

'''

import requests
import urllib.request
import ctypes
import os

def get_wallpaper():
    #print("Hello world")
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY1')
    url = 'https://api.unsplash.com/photos/random?client_id='+access_key
    params = {
        #these are the parameters of random image api
        "query" : "HD Wallpapers",
        "orientation" : "landscape"
    }

    response = requests.get(url,params).json() #generating response object , ie , it is a json object
    image_url = response['urls']['full'] #finding image url from response 
    wallpaper = urllib.request.urlretrieve(image_url, '/Users/HP/Pictures/Wallpaper Python/wallpaper.jpg') #downloading image from image_url to the specified directory and with specified name
    print(wallpaper)
    print("Wallpaper succefully downloaded...")


def set_wallpaper():
    get_wallpaper()
    #python command to set wallpaper in windows
    ctypes.windll.user32.SystemParametersInfoA(20, 0, 'c:/Users/HP/Pictures/Wallpaper Python/wallpaper.jpg'.encode() , 0)
    print("Wallpaper succefully changed...")

def main():
    op = "n"
    while op=="n":
        set_wallpaper()
        op = input("Confirm the current wallpaper ? (y/n)")


if __name__ == '__main__':
    main()

