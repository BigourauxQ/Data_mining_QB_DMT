# This Python file uses the following encoding: utf-8

import pandas as pd
from tkinter import *
import tkinter as tk
import PagePrincipale
import Analyse_de_donnees
from PIL import Image, ImageTk 


def ImagePropose():

    class window(Frame):
        def __init__(self, master=None):

            Frame.__init__(self, master)

            self.master = master
            
            #bouton suivant
            Boutonsuivant=Button(self.master, fg ='green' ,width=12, height=2, text="Suivant", command=lambda:self.suivant())
            Boutonsuivant.pack(side=BOTTOM, fill='both')




        def suivant(self):
            """ passe au pokémon qui devrait plaire suivant
            """
            global i
            if (i < len(pokemon_name) ):

                self.master.destroy()
                #création première fenêtre
                fenetre = tk.Tk()

                #paramètre de la fenêtre 
                fenetre.title("pokémon")
                fenetre.geometry("1080x720")
                
                name = pokemon_name[i]
                i+=1
                image = Image.open('./images/'+name+'.jpg')
                image2 =image.resize((int(image.width/1.5),int(image.height/1.5)))

                # Remplace PhotoImage de Tkinter par celui de PIL
                photo = ImageTk.PhotoImage(image2)

                canvas = tk.Canvas(fenetre, width=photo.width(), height=photo.height())
                canvas.create_image(540,360,anchor='center',image=photo)
                canvas.pack(side=TOP, fill='both', expand = True)

                window(fenetre)

                # affichage
                fenetre.mainloop()
            else:
                self.master.destroy()

    Analyse_de_donnees.Analyse_de_donnees()#genere le fichier csv contenant les recommendation pour l'utilisateur courant 

    pokemon_name = pd.read_csv("./Data_recommander_pour_utilisateur.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
    pokemon_name = pokemon_name['pokemon_selection']
    print(pokemon_name)


    #variable utiliser pour balayer les différentes images
    global i 
    i = 0
    #création première fenêtre
    fenetre = tk.Tk()

    #paramètre de la fenêtre 
    fenetre.title("Pokémon")
    fenetre.geometry("1080x720")
    
    image = Image.open('./images/'+pokemon_name[i]+'.jpg')

    i+=1

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

    PagePrincipale.PagePrincipale()

# Permet de tester ImagePropose seul
# Attention, le programme à besoin de certain csv pour fonctionner 
if __name__ == "__main__":
    ImagePropose()
