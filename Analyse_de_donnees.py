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
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import graphviz
import pydotplus
import numpy as np 
from IPython.display import Image, display
import pandas as pd
import random
import matplotlib.pyplot as plot

#plot.show()

### Utilisateur qui 'like' tous les 'bug'


Data = pd.read_csv("./DataPokemon.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
pokemon_name = Data['Name'][0:50] # on prend les 50 premières ligne de la colonne Name 
pokemon_type = Data['Type'][0:50] #on prend les 50 premieres ligne de la colonne type
pokemon_height = Data['height'][0:50]

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

###Main###

dataframe_like = Utilisateur3() # on choisie quelle utilisateur remplira notre tableau de like and dislike
print(dataframe_like)

tableau_de_like_U1 = dataframe_like.values.tolist()# transforme le tableau pandas en list 
tableau_des_pokemon = Data.values.tolist() 


recommandation(tableau_de_like_U1)


"""

grouped = dataframe_trois.groupby(['Type','like_and_dislike']).count()
groupedplot = grouped.plot(x=0,kind='bar',title="like and dislike per type ")# graphe avec  le nombre de like et de dislike par type de pokemon

#print(grouped)

plot.gca().xaxis.set_tick_params(labelsize = 5) # change la taille des labels en x
#plot.show()
"""