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
        BoutonValider.pack(side=BOTTOM, fill='both')

        #bouton de dislike
        BoutonValider=Button(self.master, fg ='red' ,width=12, height=2, text="Dislike", command=lambda:self.dislike())
        BoutonValider.pack(side=BOTTOM, fill='both')

   



    def like(self):
        """ met un dislike au pokémon et passe à l'image suivante s'il y en a une
        """
        self.master.destroy()
        #création première fenêtre
        fenetre = tk.Tk()

        #paramètre de la fenêtre 
        fenetre.title("Like/dislike")
        fenetre.geometry("1080x720")
        
        image = Image.open('./images/charizard.jpg')

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
        self.master.destroy()
        #création première fenêtre
        fenetre = tk.Tk()

        #paramètre de la fenêtre 
        fenetre.title("Like/dislike")
        fenetre.geometry("1080x720")
        
        image = Image.open('./images/bulbasaur.jpg')

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



#création première fenêtre
fenetre = tk.Tk()

#paramètre de la fenêtre 
fenetre.title("Like/dislike")
fenetre.geometry("1080x720")
 
image = Image.open('./images/arbok.jpg')

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