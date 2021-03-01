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

Image_de_donnee = pd.read_csv("./pokemon.csv")

print(Image_de_donnee)

choix_de_utilisateur = [ #devrat être remplis par un utilisateur
              'Favorite',
              'NotFavorite',
              'Favorite',
              'Favorite',
              'Favorite',
              ]
"""
#creating dataframes
dataframe = pd.DataFrame(data, columns=['color', 'tag', 'size', 'mode'])
resultframe = pd.DataFrame(result, columns=['favorite'])

#generating numerical labels
le1 = LabelEncoder()
dataframe['color'] = le1.fit_transform(dataframe['color'])

le2 = LabelEncoder()
dataframe['tag'] = le2.fit_transform(dataframe['tag'])

le3 = LabelEncoder()
dataframe['size'] = le3.fit_transform(dataframe['size'])

le4 = LabelEncoder()
dataframe['mode'] = le4.fit_transform(dataframe['mode'])

le5 = LabelEncoder()
resultframe['favorite'] = le5.fit_transform(resultframe['favorite'])

#Use of random forest classifier
rfc = RandomForestClassifier(n_estimators=10, max_depth=2,
                  random_state=0)
rfc = rfc.fit(dataframe, resultframe.values.ravel())

#prediction
prediction = rfc.predict([
        [le1.transform(['red'])[0], le2.transform(['nature'])[0],
         le3.transform(['thumbnail'])[0], le4.transform(['portrait'])[0]]])
print(le5.inverse_transform(prediction))
print(rfc.feature_importances_)
"""

