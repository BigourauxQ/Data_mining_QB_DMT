from bs4 import BeautifulSoup
import requests
import os
import sys
import shutil
from os.path  import basename
import re
from pathlib import Path
from urllib.request import urlretrieve as download



def getURLImg():

    url='https://pokemondb.net/sprites'
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.text,features="html.parser")
    
    
    for tag in soup.find_all("img"):
        print(tag['src'])