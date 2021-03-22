from bs4 import BeautifulSoup
import os
import sys
import shutil
from os.path  import basename
import re
from urllib.request import Request, urlopen
from PIL import Image

import requests;

def getURLImg():

    url='https://pokemondb.net/pokedex/stats/height-weight'
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    codeHTML = urlopen(req, timeout=20).read()
    
    codeHTML=codeHTML.decode("utf-8")
    
    
    soup = BeautifulSoup(codeHTML)
    
    
    images = soup.findAll('tr')
    #print(images)
    listeimg=[]
    for img in images:
        
        image = img.find_all('td')
        if len(image) == 0:
            continue
        image=image[1].getText().lower()
        if ' ' not in image and '♀' not in image and '♂' not in image and "'" not in image:
            #print(image)
            
            listeimg.append(image)
    #print(listeimg[0])       
   

    return listeimg

def saveImg(url_Img):

    #shutil.rmtree('images')


    try:
            os.mkdir('images')
    except FileExistsError:
            print("fichier déjà crée")
    for i in range(0,20): 
        f = open('images/'+url_Img[i]+'.jpg','wb')
        f.write(requests.get('https://img.pokemondb.net/artwork/large/'+url_Img[i]+'.jpg').content)
        im=Image.open('images/'+url_Img[i]+'.jpg')
        _, ext = os.path.splitext('images/'+url_Img[i]+'.jpg')
        #print(ext)
        f.close()

   
    


    

###########Main##############

saveImg(getURLImg())

print("end")




