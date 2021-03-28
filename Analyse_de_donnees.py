#Demandez à l'utilisateur de sélectionner quelques images et d'ajouter des balises. Pour chaque utilisateur, 
#vous êtes maintenant prêt à construire un profil de préférences d'utilisateur,
#basé sur cette sélection. Vous pouvez recueillir les informations suivantes manuellement,
#mais l'objectif de cette tâche consiste à les obtenir en utilisant les images sélectionnées de manière automatisée :

#    Couleurs préférées
#    Orientation de l'image préférée
#    Tailles d'images préférées (vignettes, grandes images, images de taille moyenne images, etc.)
#    Balises favorites
#    ...

#support

from sklearn import tree

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import graphviz
import pydotplus
import numpy as np 
from IPython.display import Image, display
import pandas as pd
import random
import matplotlib.pyplot as plot






# l'utilisateur 1 like et dislike aléatoirement, la fonction retourne la liste d'element liké

def Utilisateur1():
        choix_de_utilisateur = []

        for i in pokemon_name:
                
                choix = random.choice([True,False])

                if(choix == True):
                        choix_de_utilisateur.append('like')
                else:
                        choix_de_utilisateur.append('dislike') 

        dataframe_un = pd.DataFrame(choix_de_utilisateur,columns=['like_and_dislike'])
        dataframe_trois = pd.concat([dataframe_un , Data[0:50]], axis = 1)# permet de concaténer des données
        dataframe_quatre = dataframe_trois.set_index('like_and_dislike')# met la colonne dislike and like index
        dataframe_like = dataframe_quatre.drop(['dislike'])#enlève ce qui possède une colonne dislike

        return dataframe_like


#l'utilisateur 2 like uniquement les types 'Bug'

def Utilisateur2():

        choix_de_utilisateur = [] #stock  les likes et dislikes de l'utilisateur

        aime = 'Bug ' # il aime les types bug

        for i in pokemon_type: #like si c'est un 'bug'
                
                if (i == aime):
                        choix_de_utilisateur.append('like')
                else:
                        choix_de_utilisateur.append('dislike')


        dataframe = pd.DataFrame(choix_de_utilisateur,columns=['like_and_dislike'])# création d'une dataframe avec les likes et dislikes de l'utilisateur
        dataframe = pd.concat([dataframe , Data[0:50]], axis = 1)# permet de concaténer des données
        dataframe = dataframe.set_index('like_and_dislike')# met la colonne dislike and like index
        dataframe_like = dataframe.drop(['dislike'])#enlèe ce qui possède une colonne dislike

        return dataframe_like

#l'utilisateur 3 like uniquement les 'grands' pokémon

def Utilisateur3():

        choix_de_utilisateur = [] #stock  les likes et dislikes de l'utilisateur

        taille_aime = 1.5

        for i in pokemon_height: #like si c'est un 'bug'
                
                if (i > taille_aime):
                        choix_de_utilisateur.append('like')
                else:
                        choix_de_utilisateur.append('dislike')


        dataframe = pd.DataFrame(choix_de_utilisateur,columns=['like_and_dislike'])# création d'une dataframe avec les likes et dislikes de l'utilisateur
        dataframe = pd.concat([dataframe , Data[0:50]], axis = 1)# permet de concaténer des données
        dataframe = dataframe.set_index('like_and_dislike')# met la colonne dislike and like index
        dataframe_like = dataframe.drop(['dislike'])#enlèe ce qui possède une colonne dislike

        return dataframe_like

def recommandation(tableau_de_like):

        Aime = [] # contient ce que l'utilisateur aime et peu aimer
        Proposition = [] # contient uniquement les images recommandées

        # cherche des pokémons dans la grande liste ayant des caractéristiques similaires a cceux liké (taille, poids similaire, type identique)
        for i in tableau_de_like:
                for j in tableau_des_pokemon:
                        if ((i[2] == j[2]) and ((j[3]-0.1)<i[3]< (j[3]+0.1)) and ((j[4]-10)<i[4]< (j[4]+10))):
                        # if (type == type and  <height< and <poids<) 
                                Aime.append(j)

        for i in Aime: # on enlève tous les pokémon ayant un id < à 52 car il font partie de la liste déjà liké et donc déja vue par l'utilisateur
                if i[0] > 52:
                        Proposition.append(i)

        for i in Proposition:# affichage
                print(i)

        return Proposition

def Analyse_de_donnees():

        Data = pd.read_csv("./Data_like_dislike_utilisateur.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
        Data = Data.set_index('like_and_dislike')# met la colonne dislike and like index
        Data = Data.drop(['dislike'])#enlèe ce qui possède une colonne dislike
        Data = Data.values.tolist()# transforme le tableau pandas en list
        
        tableau_des_pokemon = pd.read_csv("./DataTotal.csv", encoding = "ISO-8859-1")
        tableau_des_pokemon = tableau_des_pokemon.values.tolist()
        
        Aime = [] # contient ce que l'utilisateur aime et peu aimer
        Proposition = [] # contient uniquement les images recommandées

        # cherche des pokémons dans la grande liste ayant des caractéristiques similaires a cceux liké (taille, poids similaire, type identique)
        for i in Data:
                for j in tableau_des_pokemon:
                        if ((i[1] == j[1])and ((j[3]-1)<i[3]< (j[3]+1)) and ((j[4]-30)<i[4]< (j[4]+30))):
                        # if (type == type and  <height< and <poids< and couleur == couleur) 
                                Aime.append(j)
                                
        for i in range(len(Aime) ): # on enlève tous les premier pokémon de la liste car ce sont ceux tester par l'utilisateur
                if i > len(Data):
                        Proposition.append(Aime[i][0])

   
        dataframe_proposition = pd.DataFrame(Proposition,columns=['pokemon_selection'])# création dataframe contenant les propositions pour l'utilisateur
        dataframe_proposition.to_csv('Data_recommander_pour_utilisateur.csv', index=False)   #On écrit tout ca dans un nouveau CSV
        

###Main###
""" if __name__ == "__main__":

        Data = pd.read_csv("./DataPokemon.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
        Data_image = pd.read_csv("./DataCouleur.csv", encoding = "ISO-8859-1")


        Data2 = pd.read_csv("./DataPokemon.csv", encoding = "UTF -8")#on récupère les données sur les pokemons
        Data2 =  Data2.set_index('Name')
        Data_image =  Data_image.set_index('Name')
        Data2 = pd.concat([Data2 , Data_image], axis = 1)# permet de concaténer des données
        print(Data2)

        pokemon_name = Data['Name'][0:50] # on prend les 50 premières ligne de la colonne Name 
        pokemon_type = Data['Type'][0:50] #on prend les 50 premieres ligne de la colonne type
        pokemon_height = Data['height'][0:50]

        dataframe_like = Utilisateur3() # on choisie quelle utilisateur remplira notre tableau de like and dislike
        print(dataframe_like)

        tableau_de_like_U1 = dataframe_like.values.tolist()# transforme le tableau pandas en list 
        tableau_des_pokemon = Data.values.tolist() 


        recommandation(tableau_de_like_U1) """
Analyse_de_donnees()
