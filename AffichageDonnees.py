import pandas as pd

from pandastable import Table

from tkinter import *

#On va afficher dans un tableau les données récoltées. On va pouvoir trier et filtrer ce tableau 
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.Data4 = pd.read_csv("DataFinal.csv", encoding = "ISO-8859-1")

        self.Data5 = pd.read_csv("DataFinal.csv", encoding = "ISO-8859-1")

        self.frame = Frame(self.master)
        self.frame.pack(fill='both', expand=TRUE)
        
        Tableau = Table(self.frame, dataframe=self.Data4)
        Tableau.show()

        Types=["None","Normal", "Fire","Water","Grass","Electric","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dark","Dragon","Steel","Fairy"]
        Couleurs=['black','gray','red','maroon','yellow','olive','lime','green','aqua','teal','blue','navy','fuchsia','purple','white','soft blue','soft green','soft purple','purple-blue','green-yellow','very soft green','very soft blue','pink','orange','beige','soft pink','soft orange']

        
        menu = Menu(self.master) #Création des menus d'option pour le tri et le filtrage
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

        

    def Filtre( self, param, titre): #Filtrage de la data en fonction des parametres
        
        self.Data5 = self.Data4[(self.Data4[titre].isin([param])) ]
            
        self.frame.destroy()
        
        self.frame = Frame(self.master) #On détruit puis recontruit le tableau avec les nouvelles données
        self.frame.pack(fill='both', expand=TRUE)
        Tableau = Table(self.frame, dataframe=self.Data5)
        Tableau.show()
    
    def Reset(self):#Permet de revenir au tabeau d'origine.

        self.Data5=self.Data4
        self.frame.destroy()
        
        self.frame = Frame(self.master)
        self.frame.pack(fill='both', expand=TRUE)
        Tableau = Table(self.frame, dataframe=self.Data5)
        Tableau.show()
    
    def Tri(self, param, bool): #On tri le tableau courant en fonction des parametres d'entrée
        self.Data5=self.Data5.sort_values(by=param, ascending=bool)
        self.frame.destroy()
        
        self.frame = Frame(self.master)
        self.frame.pack(fill='both', expand=TRUE)
        Tableau = Table(self.frame, dataframe=self.Data5)
        Tableau.show()
   
        
def AffichageDonnees(): #Création de la fenetre tkinter

    fenetre = Tk()
    fenetre.title('Affichage des données')
    fenetre.geometry('900x800')
    Window(fenetre)

    fenetre.mainloop()

if __name__ == "__main__":
    AffichageDonnees()




