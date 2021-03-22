import pandas as pd
import numpy as np 
from sklearn import *


Data1 = pd.read_csv("./DataPokemon.csv", encoding = "ISO-8859-1") #on récupère les données sur les pokemons
Data2= pd.read_csv("./DataCouleur.csv", encoding = "ISO-8859-1")

Data1 =  Data1.set_index('Name')
Data2 =  Data2.set_index('Name')



Data3=pd.concat([Data1,Data2], axis=1)
#TestCouleur = Data3[(Data3['Type1'].isin(['Grass'])) & (Data3['Type2'].isin(['None']))]
#print(TestCouleur)

TestTri = Data3.sort_values(by='height')
print(TestTri)

#Colonne = input("Filtrer la colonne :")
#Critere = input("Critère : ")

#DataTriee = Data3[(Data3[Colonne].isin([Critere])) ]
#print(DataTriee)



























