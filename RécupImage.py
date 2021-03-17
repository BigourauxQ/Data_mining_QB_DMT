from bs4 import BeautifulSoup
import os
import sys
import shutil
from os.path  import basename
import re
from urllib.request import Request, urlopen

import requests;


def getURLImg():

    url='https://pokemondb.net/sprites'
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    codeHTML = urlopen(req, timeout=20).read()
    
    codeHTML=codeHTML.decode("utf-8")
    
    
    soup = BeautifulSoup(codeHTML)
    
    
    images = soup.findAll("div", {"class":"infocard-list infocard-list-pkmn-sm"})
    print(images)
    listeimg=[]
    for img in images:
        image=img.find("span").get('data-src')
        listeimg.append(image)
    print(listeimg[0])       
   

    return listeimg

def saveImg(url_Img): 
    try:
        os.mkdir('Images2')
    except FileExistsError:
        print("fichier déjà crée")
    
    f = open('Images2/2.jpg','wb')
    f.write(requests.get(url_Img[0]).content)
    f.close()

   
    #shutil.move("2.jpg", "Images2" )


    

###########Main##############

#urlimg = getURLImg('https://commons.wikimedia.org/wiki/Main_Page')

getURLImg()

print("end")




