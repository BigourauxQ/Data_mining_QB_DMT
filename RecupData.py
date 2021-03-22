from bs4 import BeautifulSoup
import os
import sys
import shutil
from os.path  import basename
import re
from urllib.request import Request, urlopen
from PIL import Image
import csv
import requests;


def getURLImg():

    url='https://pokemondb.net/pokedex/stats/height-weight'
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    codeHTML = urlopen(req, timeout=50).read()
    
    codeHTML=codeHTML.decode("utf-8")
    
    
    soup = BeautifulSoup(codeHTML)
    
    
    results = soup.findAll('tr')
    rows = []
    rows.append(['Id','Name', 'Type1','Type2', 'height', 'poids'])
    # loop over results
    for result in results:
        # find all columns per result
        data = result.find_all('td')
        # check that columns have data
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
        if ' ' not in name and '♀' not in name and '♂' not in name and "'" not in name:
            rows.append([id, name, type[0],type[1], height,poids])
        with open('DataPokemon.csv','w', newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(rows)

###########Main##############


table = getURLImg()

