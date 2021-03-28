import pandas as pd

#On va dans ce code lier les datas de nos différents fichiers csv que nous avons rempli précédemment, pour réécrire un nouveau fichier tout beau tout neuf !


def JoinData():
    
    Data1 = pd.read_csv("./DataPokemon.csv", encoding = "ISO-8859-1") #on récupère les données sur les pokemons
    Data2= pd.read_csv("./DataCouleur.csv", encoding = "ISO-8859-1")
    Data1["Pokemon Name"]=Data1["Name"]
    Data1 =  Data1.set_index('Name')
    Data2 =  Data2.set_index('Name')
    Data3=pd.concat([Data1,Data2], axis=1,join='inner')#On fusionne nos différents tableaux avec comme PK les noms des pokemons
    Data4 = pd.DataFrame(Data3,  columns=['Pokemon Name','Type1', 'Type2','height','poids','couleur1','couleur2']) 

    Data4.to_csv('DataFinal.csv', index=False)   #On écrit tout ca dans un nouveau CSV


if __name__ == "__main__":    
    JoinData()












