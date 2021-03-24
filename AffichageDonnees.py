import pandas as pd
import numpy as np 
from sklearn import *
from pandastable import Table
from tkinter import ttk
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.Data5 = pd.DataFrame(Data3,  columns=['Pokemon Name','Type1', 'Type2','height','poids','couleur1','couleur2'])

        self.frame = Frame(self.master)
        self.frame.pack(fill='both', expand=TRUE)
        
        Tableau = Table(self.frame, dataframe=Data4)
        Tableau.show()

        Types=["None","Normal", "Fire","Water","Grass","Electric","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dark","Dragon","Steel","Fairy"]
        Couleurs=['black','gray','red','maroon','yellow','olive','lime','green','aqua','teal','blue','navy','fuchsia','purple','white','soft blue','soft green','soft purple','purple-blue','green-yellow','very soft green','very soft blue','pink','orange','beige','soft pink','soft orange']

        
        menu = Menu(self.master)
        self.master.config(menu=menu)

        filtrage = Menu(menu)
        filtrage.add_command(label="No Filter", command=lambda:self.Reset())

        filtrageType1 =Menu(filtrage)
        filtrageType2 =Menu(filtrage)

        filtrageCouleur1 =Menu(filtrage)
        filtrageCouleur2 =Menu(filtrage)

        for param in Types:
           
            filtrageType1.add_command(label=param, command=lambda param=param:self.Filtre(param, "Type1"))
            
            filtrageType2.add_command(label=param, command=lambda param=param:self.Filtre(param, "Type2"))

        
        
        for param in Couleurs:
               
            filtrageCouleur1.add_command(label=param, command=lambda param=param:self.Filtre(param, "couleur1"))
            
            filtrageCouleur2.add_command(label=param, command=lambda param=param:self.Filtre(param, "couleur2"))
        
        filtrage.add_cascade(label="Type1", menu=filtrageType1)
        filtrage.add_cascade(label="Type2", menu=filtrageType2)
        filtrage.add_cascade(label="Couleur1", menu=filtrageCouleur1)
        filtrage.add_cascade(label="Couleur2", menu=filtrageCouleur2)
        
        

        tri = Menu(menu)
        
        triPoids =Menu(tri)
        triPoids.add_command(label="⇧", command=lambda:self.Tri("height", True))
        triPoids.add_command(label="⇩", command=lambda:self.Tri("height", False))
        
        triTaille =Menu(filtrage)
        triTaille.add_command(label="⇧", command=lambda:self.Tri("poids", True))
        triTaille.add_command(label="⇩", command=lambda:self.Tri("poids", False))

        triNom =Menu(filtrage)
        triNom.add_command(label="⇧", command=lambda:self.Tri("Pokemon Name", True))
        triNom.add_command(label="⇩", command=lambda:self.Tri("Pokemon Name", False))

        tri.add_cascade(label="Taille", menu=triPoids)
        tri.add_cascade(label="Poids", menu=triTaille)
        tri.add_cascade(label="Nom", menu=triNom)

        menu.add_cascade(label="Filtrage par", menu=filtrage)
        menu.add_cascade(label="Tri par", menu=tri)

        

    def Filtre( self, param, titre):
        
        self.Data5 = Data4[(Data4[titre].isin([param])) ]
            
        self.frame.destroy()
        
        self.frame = Frame(self.master)
        self.frame.pack(fill='both', expand=TRUE)
        Tableau = Table(self.frame, dataframe=self.Data5)
        Tableau.show()
    
    def Reset(self):

        self.Data5=Data4
        self.frame.destroy()
        
        self.frame = Frame(self.master)
        self.frame.pack(fill='both', expand=TRUE)
        Tableau = Table(self.frame, dataframe=self.Data5)
        Tableau.show()
    
    def Tri(self, param, bool):
        self.Data5=self.Data5.sort_values(by=param, ascending=bool)
        self.frame.destroy()
        
        self.frame = Frame(self.master)
        self.frame.pack(fill='both', expand=TRUE)
        Tableau = Table(self.frame, dataframe=self.Data5)
        Tableau.show()
   
        
       
Data1 = pd.read_csv("./DataPokemon.csv", encoding = "ISO-8859-1") #on récupère les données sur les pokemons
Data2= pd.read_csv("./DataCouleur.csv", encoding = "ISO-8859-1")
Data1["Pokemon Name"]=Data1["Name"]
Data1 =  Data1.set_index('Name')
Data2 =  Data2.set_index('Name')



Data3=pd.concat([Data1,Data2], axis=1)


Data4 = pd.DataFrame(Data3,  columns=['Pokemon Name','Type1', 'Type2','height','poids','couleur1','couleur2'])


fenetre = Tk()
fenetre.title('Affichage des données')
fenetre.geometry('900x800')
app = Window(fenetre)



fenetre.mainloop()





