from bs4 import BeautifulSoup
import requests
import os
import sys
import shutil
from os.path  import basename
import re



def getURLImg():

    url='https://pokemondb.net/sprites'
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.text,features="html.parser")
    
    
    images = soup.find("a", class_="infocard")
    for image in images:
        
        shield_url=image.['data-src']
        print(shield_url)

    url_img = images.attrs({"data-src"}) #The extension you pulled earlier

    return url_img

def saveImg(url_Img): 
    try:
        os.mkdir('Images2')
    except FileExistsError:
        print("fichier déjà crée")
    
    f = open('Images2/2.jpg','wb')
    f.write(requests.get(url_Img).content)
    f.close()

   
    #shutil.move("2.jpg", "Images2" )


    

###########Main##############

#urlimg = getURLImg('https://commons.wikimedia.org/wiki/Main_Page')

saveImg(getURLImg())

print("end")




