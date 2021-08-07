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
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY1') #provide the unsplash access key for random image
    url = 'https://api.unsplash.com/photos/random?client_id='+access_key
    params = {
        #these are some of parameters of random image api
        "query" : "HD Wallpapers",
        "orientation" : "landscape"
    }

    response = requests.get(url,params).json() #generating response object , ie , it is a json object
    image_url = response['urls']['full'] #finding image url from response
    absolute_path = 'c:/Users/HP/Pictures/Wallpaper Python/wallpaper.jpg' #absolute path of the directory to which image will be downloaded
    wallpaper = urllib.request.urlretrieve(image_url, absolute_path) #downloading image from image_url to the specified directory and with specified name
    print(wallpaper)
    print("Wallpaper succefully downloaded...")


def set_wallpaper():
    get_wallpaper()
    #python command to set wallpaper in windows
    absolute_path = 'c:/Users/HP/Pictures/Wallpaper Python/wallpaper.jpg'
    ctypes.windll.user32.SystemParametersInfoA(20, 0, absolute_path.encode() , 0)
    print("Wallpaper succefully changed...")

def main():
    op = "n"
    while op=="n":
        set_wallpaper()
        op = input("Confirm the current wallpaper ? (y/n)")


if __name__ == '__main__':
    main()

