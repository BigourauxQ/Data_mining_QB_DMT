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
"""
### code affichage des statistique d'une image

from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

imgfile = Image.open("./images/images/wailord.png")#lit bien les .png
#print(imgfile.size)# taille de l'image
#print(imgfile.mode)#donne des info sur le format pixel
#print(imgfile.format)#type d'image

n_clusters = 5

numarray = numpy.array(imgfile.getdata(), numpy.uint8)#tableau contenant les pixels de l'image sous forme de matrice

clusters = KMeans(n_clusters)# algo de k means

clusters.fit(numarray)

npbins = numpy.arange(0, n_clusters+1)

histogram = numpy.histogram(clusters.labels_, bins=npbins)

labels = numpy.unique(clusters.labels_)

barlist = plot.bar(labels, histogram[0])

for i in range(n_clusters):

    barlist[i].set_color('#%02x%02x%02x' % (
    math.ceil(clusters.cluster_centers_[i][0]), 
        math.ceil(clusters.cluster_centers_[i][1]),
    math.ceil(clusters.cluster_centers_[i][2])))
"""
#plot.show()

### Utilisateur qui 'like' tous les 'bug'

Utilsateur1 = 'Bug' # il aime les types bug

Image_de_donnee = pd.read_csv("./DataPokemon.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
pokemon_name = Image_de_donnee['Name'][0:50] # on prend les 50 premières ligne de la colonne Name 
pokemon_type = Image_de_donnee['Type'][0:50] #on prend les 50 premieres ligne de la colonne type

choix_de_utilisateur1 = [] #stock  les likes et dislikes de l'utilisateur

for i in pokemon_type: #like si c'est un 'bug'
        
        if (i == Utilsateur1):
                choix_de_utilisateur1.append('like')
        else:
                choix_de_utilisateur1.append('dislike')


dataframe_U1 = pd.DataFrame(choix_de_utilisateur1,columns=['like_and_dislike'])# création d'une dataframe avec les likes et dislikes de l'utilisateur
dataframe_U1_2 = pd.concat([dataframe_U1 , Image_de_donnee[0:50]], axis = 1)# permet de concaténer des données

dataframe_U1_4 = dataframe_U1_2.set_index('like_and_dislike')# met la colonne dislike and like index
dataframe_U1_like = dataframe_U1_4.drop(['dislike'])#enlèe ce qui possède une colonne dislike


### Utilisateur aléatoire ###

choix_de_utilisateur = []
choix_de_utilisateur_deux = []

for i in pokemon_name:
        
        choix = random.choice([True,False])

        if(choix == True):
                choix_de_utilisateur.append('like')
        else:
                choix_de_utilisateur.append('dislike') 
        
        choix_de_utilisateur_deux.append(random.choice(['mignon','drole','moche','cool','puissant','enorme','petit']))# rajoute une colonne de donnée de l'utilisateur

dataframe_un = pd.DataFrame(choix_de_utilisateur,columns=['like_and_dislike'])
dataframe_un_bis = pd.DataFrame(choix_de_utilisateur_deux,columns=['Mot'])
dataframe_un_bis_deux = pd.concat([dataframe_un , dataframe_un_bis], axis = 1)

dataframe_trois = pd.concat([dataframe_un_bis_deux , Image_de_donnee[0:50]], axis = 1)# permet de concaténer des données

dataframe_quatre = dataframe_trois.set_index('like_and_dislike')# met la colonne dislike and like index
dataframe_like = dataframe_quatre.drop(['dislike'])#enlève ce qui possède une colonne dislike

print(dataframe_like)

# teste de corrélation 

tableau_de_like = dataframe_like.values.tolist()# récupéra
tableau_des_pokemon = Image_de_donnee.values.tolist()
Aime = []

# cherche des pokémons dans la grande liste ayant des caractéristiques similaires a cceux liké (taille, poids similaire, type identique)
for i in tableau_de_like:
        for j in tableau_des_pokemon:
                if ((i[3] == j[2]) and ((j[3]-1)<i[4]< (j[3]+1)) and ((j[3]-50)<i[4]< (j[3]+50))):
                        Aime.append(j)


for i in Aime:
        print(i)




grouped = dataframe_trois.groupby(['Type','like_and_dislike'])['Mot'].count()

groupedplot = grouped.plot(x=0,kind='bar',title="like and dislike per type ")# graphe avec  le nombre de like et de dislike par type de pokemon

#print(grouped)




plot.gca().xaxis.set_tick_params(labelsize = 5) # change la taille des labels en x
#plot.show()