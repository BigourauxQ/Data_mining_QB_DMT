
from tkinter import *

import Connexion
import RecupImage
import RecupData
import CouleurDominante
import AffichageDonnees
import Statistiques
import JoinData

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        

        etiquetteNbreImages = Label(self.master, text='Combien d\'images voulez vous charger ? :')
        etiquetteNbreImages.grid(row=0, column=0, padx=5,pady = 5)

        self.entreeNbreImages = Entry(self.master, width=10)
        self.entreeNbreImages.grid(row=0, column=1,padx=5, pady = 5)
        
        BoutonValider=Button(self.master, fg ='green' ,width=12, height=2, text="Valider", command=lambda:self.ValidDL())
        BoutonValider.grid(row=1, column=0, padx=10,pady = 10)

    
    def ValidDL(self):
        NbreImages=eval(self.entreeNbreImages.get())
        
        RecupImage.RecupImage(NbreImages) #On charge nos images dans un fichier (le param est le nombre d'images à charger)
        RecupData.RecupData(NbreImages) #On récupere d'autres informations en parcourant la page web 
        #CouleurDominante.CouleurDominante() #On récupère les 2 couleurs dominantes de chaque image /!\ Algo assez lent !!!!
        JoinData.JoinData()
        
        etiquetteNbreImages = Label(self.master,fg='green', text='Téléchargement terminé !!!')
        etiquetteNbreImages.grid(row=1, column=1, padx=5,pady = 5)
        

        BoutonAffichage=Button(self.master, fg ='blue' , height=2, text="Afficher les données", command=lambda:AffichageDonnees.AffichageDonnees())
        BoutonAffichage.grid(row=3, column=0, padx=10,pady = 15)

        BoutonStats=Button(self.master, fg ='purple' , height=2, text="Afficher les stats", command=lambda:Statistiques.Statistiques())
        BoutonStats.grid(row=3, column=1, padx=10,pady = 15, sticky='w')

        BoutonAffichage=Button(self.master, fg ='orange' , height=2, text="Afficher les données perso", command=lambda:AffichageDonnees.AffichageDonnees())
        BoutonAffichage.grid(row=2, column=0, padx=10,pady = 15)

        BoutonAffichage=Button(self.master, fg ='orange' , height=2, text="Faire le test de préférences", command=lambda:AffichageDonnees.AffichageDonnees())
        BoutonAffichage.grid(row=2, column=0, padx=10,pady = 15)


        



def PagePrincipale(): #Création de la fenetre tkinter

    fenetre = Tk()
    fenetre.title('Page Principale')
    
    Window(fenetre)

    fenetre.mainloop()

if __name__ == "__main__":
    InscriptionReussie = Connexion.Connexion()
    if (InscriptionReussie== True):
        PagePrincipale()
