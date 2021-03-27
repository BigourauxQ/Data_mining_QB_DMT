
# This Python file uses the following encoding: utf-8

from bs4 import BeautifulSoup
import os
import sys
#import shutil
from os.path  import basename
import re
from urllib.request import Request, urlopen
from PIL import Image

import requests;

#Va parcourir le code html du site renseigne pour extraire des noms de pokemon
def getURLImg():

    url='https://pokemondb.net/pokedex/stats/height-weight' 
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    codeHTML = urlopen(req, timeout=20).read()
    
    codeHTML=codeHTML.decode("utf-8")
    
    soup = BeautifulSoup(codeHTML,features="lxml") #On utlise Beautiful Soup pour notre web scraping
 
    names = soup.findAll('tr') #Les donnees sont cachees dans des tableaux html
    #print(images)
    
    listeimg=[] #La liste des noms des pokemons dont on va aller telecharger l'image
    for img in names:
        
        image = img.find_all('td')
        if len(image) == 0:
            continue
        image=image[1].getText().lower()
        if ' ' not in image and '♀' not in image and '♂' not in image and "'" not in image and "e" not in image: #On nettoie une premiere fois en filtrant les pokemons avec des noms comportant des caracteres speciaux qui pourraient poser probleme plus tard
            #print(image)
            
            listeimg.append(image)
    #print(listeimg[0])       
   

    return listeimg

#fonction qui permet de creer un dossier(si il n'existe pas) et d'y stocker toutes les images
def saveImg(listeimg, nbreImages):

    #shutil.rmtree('images') #permet de detruire automatiquement le fichier des images

    try:                    
            os.mkdir('images')
    except FileExistsError:
            print("fichier deja cree")
    if len(listeimg)<nbreImages:
        nbreImages=len(listeimg)
    for i in range(0,nbreImages):     #on va charger sur le meme site de belles images qui correspondent aux pokemons dont on a charge les noms
        f = open('images/'+listeimg[i]+'.jpg','wb')
        f.write(requests.get('https://img.pokemondb.net/artwork/large/'+listeimg[i]+'.jpg').content)
        im=Image.open('images/'+listeimg[i]+'.jpg')
        _, ext = os.path.splitext('images/'+listeimg[i]+'.jpg')  #On renomme correctement nos images
        #print(ext)
        f.close()

   
###########Main##############
def RecupImage(nbreImages):
    
    saveImg(getURLImg(), nbreImages)

    print("end")
if __name__ == "__main__":
    RecupImage(nbreImages=10)




