
# This Python file uses the following encoding: utf-8

from tkinter import *
import pandas as pd
from PIL import Image, ImageTk 

import Connexion
import RecupImage
import RecupData
import couleurDominante
import AffichageDonnees
import AffichDonneesPerso
import Statistiques
import JoinData

import ImagePropose


class Fenetre(Toplevel):
    def __init__(self,master=None):

        Toplevel.__init__(self,master)
        self.title("Like/dislike")
        self.geometry("1080x720")
        self.i=1
        self.Data = pd.read_csv("./DataFinal.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
        self.pokemon_name = self.Data['Pokemon Name'][:16] 

        #tableau de like and dislike remplie par l'utilisateur
        self.choix_de_utilisateur = []
        self.choix_de_utilisateur.append('dislike')
        
        self.image = Image.open('./images/'+self.pokemon_name[self.i]+'.jpg')

        self.image2 =self.image.resize((int(self.image.width/1.5),int(self.image.height/1.5)))
        # Remplace PhotoImage de Tkinter par celui de PIL
        self.photo = ImageTk.PhotoImage( self.image2)

        self.canvas = Canvas(self, width=self.photo.width(), height=self.photo.height())
        
        self.canvas.pack(side=TOP, fill='both', expand = True)
        #self.canvas.create_text(500, 360, text="Boom !", fill="red")
        self.canvas.create_image(500, 360,anchor='center',image=self.photo)

        #bouton de Like
        BoutonLike=Button(self, fg ='green' ,width=12, height=2, text="Like", command=lambda:self.LikeOrDislike("like"))
        BoutonLike.pack(side=RIGHT, fill='both', padx=50, pady=20)

        #bouton de dislike
        BoutonDislike=Button(self, fg ='red' ,width=12, height=2, text="Dislike", command=lambda:self.LikeOrDislike("dislike"))
        BoutonDislike.pack(side=LEFT, fill='both', padx=50, pady=20)


    def LikeOrDislike(self, appreciation):
        """ met un dislike au pokémon et passe à l'image suivante s'il y en a une
        """
        if appreciation=="like":
            self.choix_de_utilisateur.append('like')
        else:
            self.choix_de_utilisateur.append('dislike')
            

        if (self.i < 14 ):
            
            # permet de selectionner le bon nom dans le dans le csv
            
            self.i+=1
            self.image = Image.open('./images/'+self.pokemon_name[self.i]+'.jpg')
            self.image2 =self.image.resize((int(self.image.width/1.5),int(self.image.height/1.5)))
            # Remplace PhotoImage de Tkinter par celui de PIL
            self.photo = ImageTk.PhotoImage(self.image2)

            
            self.canvas.create_image(540,360,anchor='center',image=self.photo)
            self.canvas.pack(side=TOP, fill='both', expand = True)
            self.Write()
        else:
            #une fois terminé le fenêtre se détruit en l'utilisateur est renvoyé sur la fenêtre de selection des images 
            self.destroy()
    
    def Write(self):
        utilisateur = pd.read_csv("./UserCourant.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
        utilisateur = utilisateur.values.tolist()
        utilisateur = utilisateur[0][0] # utilisateur actuelle
        dataframe_un = pd.DataFrame(self.choix_de_utilisateur,columns=['like_and_dislike'])# création dataframe contenant les likes et dislikes de l'utilisateur
        dataframe_deux = pd.concat([dataframe_un , self.Data[:14]], axis = 1)# permet de concaténer des données
        dataframe_deux.to_csv('Data_like_dislike_'+utilisateur+'.csv', index=False)   #On écrit tout ca dans un nouveau CSV propre à chaque utilisateur 

class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master

        #demande combien d'image doit être chargé
        etiquetteNbreImages = Label(self.master, text='Combien d\'images voulez vous charger ? (minimum 20) :')
        etiquetteNbreImages.grid(row=0, column=0, padx=5,pady = 5)
        self.entreeNbreImages = Entry(self.master, width=10)
        self.entreeNbreImages.grid(row=0, column=1,padx=5, pady = 5)
        
        #bouton de validation
        self.BoutonValider=Button(self.master, fg ='green' ,width=12, height=2, text="Valider", command=lambda:self.ValidDL())
        self.BoutonValider.grid(row=1, column=0, padx=10,pady = 10)

    
    def ValidDL(self):

        NbreImages=eval(self.entreeNbreImages.get())#récupère le nombre d'image demandé

        RecupImage.RecupImage(NbreImages) 
        RecupData.RecupData(NbreImages) #On recupere d'autres informations en parcourant la page web
  
        #CouleurDominante.CouleurDominante() 

        JoinData.JoinData()# crée un tableau contenant les images que l'utilisateur va tester
        
        self.BoutonValider.destroy()

        etiquetteNbreImages = Label(self.master,fg='green', text='Telechargement termine !!!')
        etiquetteNbreImages.grid(row=1, column=1, padx=5,pady = 5, sticky='w')
        

        BoutonAffichage=Button(self.master, fg ='blue' , height=2, text="Afficher les donnees", command=lambda:AffichageDonnees.AffichageDonnees())
        BoutonAffichage.grid(row=3, column=0, padx=10,pady = 15)

        BoutonStats=Button(self.master, fg ='purple' , height=2, text="Afficher les stats", command=lambda:Statistiques.Statistiques())
        BoutonStats.grid(row=3, column=1, padx=10,pady = 15, sticky='w')

        BoutonAffichagePerso=Button(self.master, fg ='orange' , height=2, text="Afficher les donnees perso", command=lambda:AffichDonneesPerso.AffichDonneesPerso())
        BoutonAffichagePerso.grid(row=2, column=1, padx=10,pady = 15)


        BoutonTestPref=Button(self.master, fg ='orange' , height=2, text="Faire le test de preferences", command=lambda:self.Testpref())
        BoutonTestPref.grid(row=2, column=0, padx=10,pady = 15)

        
    
    def Testpref(self):
        """lance la phase de like and dislike
        """
        fen1= Fenetre()
        #TestPref.TestPref()
        self.BoutonPropositons=Button(self.master, fg ='purple' , height=2, text="images proposées", command=lambda:self.Imagepropose())
        self.BoutonPropositons.grid(row=1, column=0, padx=10,pady = 15)
        
    def Imagepropose(self):
        """Propose des images par l'algorithme de rapporchement préférentiels
        """
        
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
