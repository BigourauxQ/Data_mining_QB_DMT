from bs4 import BeautifulSoup
import requests
import os
import sys
import shutil

def getURLImg(url):
  html_page = requests.get(url)
  soup = BeautifulSoup(html_page.text, 'html.parser')

  images = soup.findAll('img')
  example = images[0]

  url_img = example.attrs['src'] #The extension you pulled earlier

  return url_img

def saveImg(url_Img):

    f = open('2.jpg','wb')
    f.write(requests.get(url_Img).content)
    f.close()

    try:
        os.mkdir('Images2')
    except FileExistsError:
        print("fichier déjà crée")
    shutil.move("2.jpg", "Images2" )


    

###########Main##############

urlimg = getURLImg('https://commons.wikimedia.org/wiki/Main_Page')
saveImg(urlimg)

print("end")




