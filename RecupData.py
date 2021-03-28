
from bs4 import BeautifulSoup
from os.path  import basename
from urllib.request import Request, urlopen
import csv


#On va de nouveau parcourir le tableau html à la recherche d'informations utilies sur nos pokemons
def getData(nbreImages):

    url='https://pokemondb.net/pokedex/stats/height-weight'
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    codeHTML = urlopen(req, timeout=50).read()
    
    codeHTML=codeHTML.decode("utf-8")
    
    
    soup = BeautifulSoup(codeHTML,features="lxml")
    
    
    results = soup.findAll('tr')
    rows = []
    rows.append(['Id','Name', 'Type1','Type2', 'height', 'poids']) #On va ordonner les informations qu'on poche dans un tableau 
    # boucle sur les résultats de la recherche
    i=0
    for result in results :
        if i < nbreImages:
            # On trouve toutes les colonnes
            data = result.find_all('td')
            # On va récuperer les infos qui nous intéressent dans chacune des colonnes
            if len(data) == 0:
                continue
            id = data[0].getText()
            name = data[1].getText().lower()
            strtype =data[2].getText()
            type =[]
            for mot in strtype.split(" "):
                if mot !="":
                    type.append(mot)
            if len(type)==1:
                type.append("None")
            height=data[4].getText()
            poids=data[6].getText()
            #print(height)
            if ' ' not in name and '♀' not in name and '♂' not in name and "'" not in name and "é" not in name: #De nouveau le filtrage pour les caracteres indésirables
                rows.append([id, name, type[0],type[1], height,poids])
                i+=1
            with open('DataPokemon.csv','w', newline='') as f_output:
                csv_output = csv.writer(f_output)   #On réécrit notre tableau dans un fichier csv, ligne par ligne
                csv_output.writerows(rows)
            

###########Main##############

def RecupData(nbreImages):
    getData(nbreImages)
    print("done")

if __name__ == "__main__":
    RecupData(nbreImages=100)

