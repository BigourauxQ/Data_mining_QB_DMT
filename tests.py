# This Python file uses the following encoding: utf-8

import pandas as pd
from tkinter import *


from PIL import Image, ImageTk 




class Fenetre(Tk):
    def __init__(self):

        Tk.__init__(self)
        self.geometry("1080x720")
        self.i=0
        self.Data = pd.read_csv("./DataFinal.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
        self.pokemon_name = self.Data['Pokemon Name'][:16] 

        #tableau de like and dislike remplie par l'utilisateur
        self.choix_de_utilisateur = []
        
        self.image = Image.open('./images/'+self.pokemon_name[self.i]+'.jpg')

        self.image2 =self.image.resize((int(self.image.width/1.5),int(self.image.height/1.5)))
        # Remplace PhotoImage de Tkinter par celui de PIL
        self.photo = ImageTk.PhotoImage(self.image2)

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
            

        if (self.i < 15 ):
            
            # permet de selectionner le bon nom dans le dans le csv
            
            self.i+=1
            self.image = Image.open('./images/'+self.pokemon_name[self.i]+'.jpg')
            self.image2 =self.image.resize((int(self.image.width/1.5),int(self.image.height/1.5)))
            # Remplace PhotoImage de Tkinter par celui de PIL
            self.photo = ImageTk.PhotoImage(self.image2)

            
            self.canvas.create_image(540,360,anchor='center',image=self.photo)
            self.canvas.pack(side=TOP, fill='both', expand = True)
            
        else:
            #une fois terminé le fenêtre se détruit en l'utilisateur est renvoyé sur la fenêtre de selection des images 
            self.destroy()





def TestPref():

    #création première fenêtre
    fen= Fenetre()
    #paramètre de la fenêtre 
    fen.title("Like/dislike")
    
    

    

    # affichage
    fen.mainloop()

    # une fois la fenêtre de l'utilisateur fermée on crée un fichier csv avec les likes et dislikes de l'utilisateur sur un échantillon 
    utilisateur = pd.read_csv("./UserCourant.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
    utilisateur = utilisateur.values.tolist()
    utilisateur = utilisateur[0][0] # utilisateur actuelle
    dataframe_un = pd.DataFrame(fen.choix_de_utilisateur,columns=['like_and_dislike'])# création dataframe contenant les likes et dislikes de l'utilisateur
    dataframe_deux = pd.concat([dataframe_un , fen.Data], axis = 1)# permet de concaténer des données
    dataframe_deux.to_csv('Data_like_dislike_'+utilisateur+'.csv', index=False)   #On écrit tout ca dans un nouveau CSV propre à chaque utilisateur 

   

# permet de vérifier localement si la fonction tourne
# Attention toutefois à veiller que les csv nécessaire pour le bon fonctionnement de la fonction soit disponible
 
if __name__ == "__main__":
    TestPref()
