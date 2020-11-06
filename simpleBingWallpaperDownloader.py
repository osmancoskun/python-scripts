import datetime
import requests
import json
import os

#Taking Jason Statham
jsonData = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")

#Turning Statham to string
wallpaperData = json.loads(jsonData.text)

#Taking url datas from first images array
wallpaperLink = wallpaperData["images"][0]["url"]

#Removing first char ("/") of wallpaper link 
wallpaperLink = wallpaperLink[1:]

#Getting new name for our wallpaper
wallpaperName = "BING-" + wallpaperData["images"][0]["startdate"] + ".jpg"

#Splitting wallpaper link till ("&") char
wallpaperLink = wallpaperLink.split("&")[0]

#Making direct link to our wallpaper to download
fullWallpaperLink = "https://www.bing.com/" + wallpaperLink

#Downloading wallpaper
os.system("wget " + fullWallpaperLink)

#Changing name of it to BING + current date
print(wallpaperLink)
