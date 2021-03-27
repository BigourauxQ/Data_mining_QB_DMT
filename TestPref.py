# This Python file uses the following encoding: utf-8

import pandas as pd
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk 

class window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master = master
        
        #bouton de Like
        BoutonValider=Button(self.master, fg ='green' ,width=12, height=2, text="Like", command=lambda:self.like())
        BoutonValider.pack(side=RIGHT, fill='both')

        #bouton de dislike
        BoutonValider=Button(self.master, fg ='red' ,width=12, height=2, text="Dislike", command=lambda:self.dislike())
        BoutonValider.pack(side=LEFT, fill='both')

   



    def like(self):
        """ met un dislike au pokémon et passe à l'image suivante s'il y en a une
        """

        choix_de_utilisateur.append('like')

        self.master.destroy()
        #création première fenêtre
        fenetre = tk.Tk()

        #paramètre de la fenêtre 
        fenetre.title("Like/dislike")
        fenetre.geometry("1080x720")
        
        # permet de selectionner le bon nom dans le dans le csv
        global i
        name = pokemon_name[i]
        i+=1

        image = Image.open('./Images2/'+name+'.jpg')

        image2 =image.resize((int(image.width/1.5),int(image.height/1.5)))
        # Remplace PhotoImage de Tkinter par celui de PIL
        photo = ImageTk.PhotoImage(image2)

        #label = tk.Label(fenetre, image=photo)
        #label.pack()
        canvas = tk.Canvas(fenetre, width=photo.width(), height=photo.height())
        canvas.create_image(540,360,anchor='center',image=photo)
        canvas.pack(side=TOP, fill='both', expand = True)

        window(fenetre)

        # affichage
        fenetre.mainloop()




    def dislike(self):
        """ met un dislike au pokémon et passe à l'image suivante s'il y en a 
        """
        choix_de_utilisateur.append('dislike')

        self.master.destroy()
        #création première fenêtre
        fenetre = tk.Tk()

        #paramètre de la fenêtre 
        fenetre.title("Like/dislike")
        fenetre.geometry("1080x720")

        # permet de selectionner le bon nom dans le dans le csv
        global i
        name = pokemon_name[i]
        i+=1
        
        image = Image.open('./Images2/'+name+'.jpg')

        image2 =image.resize((int(image.width/1.5),int(image.height/1.5)))
        # Remplace PhotoImage de Tkinter par celui de PIL
        photo = ImageTk.PhotoImage(image2)

        #label = tk.Label(fenetre, image=photo)
        #label.pack()
        canvas = tk.Canvas(fenetre, width=photo.width(), height=photo.height())
        canvas.create_image(540,360,anchor='center',image=photo)
        canvas.pack(side=TOP, fill='both', expand = True)

        window(fenetre)

        # affichage
        fenetre.mainloop()


Data = pd.read_csv("./DataFinal.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
pokemon_name = Data['Pokemon Name'][:] 

#tableau de like and dislike

choix_de_utilisateur = []

#variable utiliser pour balayer les différentes images
i = 0

#création première fenêtre
fenetre = tk.Tk()

#paramètre de la fenêtre 
fenetre.title("Like/dislike")
fenetre.geometry("1080x720")
 
image = Image.open('./Images2/arbok.jpg')

image2 =image.resize((int(image.width/1.5),int(image.height/1.5)))
# Remplace PhotoImage de Tkinter par celui de PIL
photo = ImageTk.PhotoImage(image2)

#label = tk.Label(fenetre, image=photo)
#label.pack()
canvas = tk.Canvas(fenetre, width=photo.width(), height=photo.height())
canvas.create_image(540,360,anchor='center',image=photo)
canvas.pack(side=TOP, fill='both', expand = True)

window(fenetre)

# affichage
fenetre.mainloop()

# crée un fichier csv avec les likes et dislikes de l'utilisateur sur un échantillon 

dataframe_un = pd.DataFrame(choix_de_utilisateur,columns=['like_and_dislike'])# création dataframe contenant les likes et dislikes de l'utilisateur
dataframe_deux = pd.concat([dataframe_un , Data], axis = 1)# permet de concaténer des données
dataframe_deux.to_csv('Data_like_dislike_utilisateur.csv', index=False)   #On écrit tout ca dans un nouveau CSV
