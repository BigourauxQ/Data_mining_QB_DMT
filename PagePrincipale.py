
# This Python file uses the following encoding: utf-8

from tkinter import *

import Connexion
import RecupImage
import RecupData
import couleurDominante
import AffichageDonnees
import Statistiques
import JoinData
import TestPref
import ImagePropose

class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master

        #demande combien d'image doit être chargé
        etiquetteNbreImages = Label(self.master, text='Combien d\'images voulez vous charger ? :')
        etiquetteNbreImages.grid(row=0, column=0, padx=5,pady = 5)
        self.entreeNbreImages = Entry(self.master, width=10)
        self.entreeNbreImages.grid(row=0, column=1,padx=5, pady = 5)
        
        #bouton de validation
        BoutonValider=Button(self.master, fg ='green' ,width=12, height=2, text="Valider", command=lambda:self.ValidDL())
        BoutonValider.grid(row=1, column=0, padx=10,pady = 10)

    
    def ValidDL(self):

        NbreImages=eval(self.entreeNbreImages.get())#récupère le nombre d'image demandé

        RecupImage.RecupImage(NbreImages) 
        RecupData.RecupData(NbreImages) #On recupere d'autres informations en parcourant la page web
  
        #CouleurDominante.CouleurDominante() 

        JoinData.JoinData()# crée un tableau contenant les images que l'utilisateur va tester
        
        etiquetteNbreImages = Label(self.master,fg='green', text='Telechargement termine !!!')
        etiquetteNbreImages.grid(row=1, column=1, padx=5,pady = 5)
        

        BoutonAffichage=Button(self.master, fg ='blue' , height=2, text="Afficher les donnees", command=lambda:AffichageDonnees.AffichageDonnees())
        BoutonAffichage.grid(row=3, column=0, padx=10,pady = 15)

        BoutonStats=Button(self.master, fg ='purple' , height=2, text="Afficher les stats", command=lambda:Statistiques.Statistiques())
        BoutonStats.grid(row=3, column=1, padx=10,pady = 15, sticky='w')

        BoutonAffichagePerso=Button(self.master, fg ='orange' , height=2, text="Afficher les donnees perso", command=lambda:AffichageDonnees.AffichageDonnees())
        BoutonAffichagePerso.grid(row=2, column=1, padx=10,pady = 15)



        BoutonTestPref=Button(self.master, fg ='orange' , height=2, text="Faire le test de preferences", command=lambda:self.Testpref())
        BoutonTestPref.grid(row=2, column=0, padx=10,pady = 15)

        BoutonTestPref=Button(self.master, fg ='purple' , height=2, text="image proposé", command=lambda:self.Imagepropose())
        BoutonTestPref.grid(row=4, column=0, padx=10,pady = 15)
    
    def Testpref(self):
        """lance la phase de like and dislike
        """
        self.master.destroy()
        TestPref.TestPref()
        
    def Imagepropose(self):
        """lance la phase de like and dislike
        """
        self.master.destroy()
        ImagePropose.ImagePropose()



def PagePrincipale(): 
    """Creation de la fenetre tkinter
    """

    fenetre = Tk()
    fenetre.title('Page Principale')
    Window(fenetre)
    fenetre.mainloop()

if __name__ == "__main__":

    InscriptionReussie = Connexion.Connexion()#appelle fonction Connexion

    if (InscriptionReussie):
        PagePrincipale()
