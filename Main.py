#Main de notre programme. 
#C'est d'ici qu on va pouvoir lancer toutes nos fonctionalités.

import RecupImage
import RecupData
import CouleurDominante
import AffichageDonnees
import Statistiques
import JoinData

RecupImage.RecupImage() #On charge nos images dans un fichier

RecupData.RecupData() #On récupere d'autres informations en parcourant la page web 

#CouleurDominante.CouleurDominante() #On récupère les 2 couleurs dominantes de chaque image /!\ Algo assez lent !!!!

JoinData.JoinData()

AffichageDonnees.AffichageDonnees() #On affiche toutes les données dans un tabelau interractif tkinter

Statistiques.Statistiques() # affiche des graphs représentant les statistiques pour les différentes données de nos pokemons.