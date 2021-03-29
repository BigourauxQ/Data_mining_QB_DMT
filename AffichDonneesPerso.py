import pandas as pd

import matplotlib.pyplot as plot



from tkinter import *



#affichage de différents diagrammes représentant les statistiques de nos données
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        
        utilisateur = pd.read_csv("./UserCourant.csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
        utilisateur = utilisateur.values.tolist()
        utilisateur = utilisateur[0][0] # utilisateur actuelle

        self.Data4 = pd.read_csv("./Data_like_dislike_"+utilisateur+".csv", encoding = "ISO-8859-1")#on récupère les données sur les pokemons
        self.Data4 = self.Data4.set_index('like_and_dislike')# met la colonne dislike and like index
        self.Data4 = self.Data4.drop(['dislike'])#enlèe ce qui possède une colonne dislike

        
        StatType1 = Button(self.master, fg ='blue' ,width=30, height=2, text="Nombre de likes par Type1", command=lambda:self.PrintHist("Type1"))
        StatType1.pack(padx=10, pady=10)

        StatType2 = Button(self.master,fg ='purple' ,width=30, height=2, text="Nombre de likes par Type2", command=lambda:self.PrintHist("Type2"))
        StatType2.pack(padx=10, pady=10)

        StatCouleur1 = Button(self.master, fg ='blue' ,width=30, height=2,text="Nombre de likes par Couleur1", command=lambda:self.PrintHist("couleur1"))
        StatCouleur1.pack(padx=10, pady=10)

        StatCouleur2 = Button(self.master,fg ='purple' ,width=30, height=2, text="Nombre de likes par Couleur2", command=lambda:self.PrintHist("couleur2"))
        StatCouleur2.pack(padx=10, pady=10)

        StatGroupPoids = Button(self.master,fg ='blue' ,width=40, height=2, text="Poids moyen des pokemons likés par Type1", command=lambda:self.PrintHistGrouped("poids","(en kg)"))
        StatGroupPoids.pack(padx=10, pady=10)

        StatGroupTaille = Button(self.master,fg ='purple' ,width=40, height=2, text="Taille moyenne des pokemons likés par Type1", command=lambda:self.PrintHistGrouped("height","(en m)"))
        StatGroupTaille.pack(padx=10, pady=10)

        # StatHeigh = Button(self.master, text="Nombre de pokemons par taille ", command=lambda:self.PrintHist("taille (en m)"))
        # StatHeigh.pack(padx=10, pady=10)


    def PrintHist(self, param):#On affiche le graphe adéquat en appliquant value_counts a la colonne souhaitée avant de plot
        
        plot.clf()
        self.graph= self.Data4[param].value_counts(normalize=False).plot(kind="bar", title="Nombre de likes par "+param)
        
        plot.show()

    def PrintHistGrouped(self, param, unité):
        
        plot.close() #probleme avec clr pour cette fct
        self.Data5=self.Data4[["Type1",param]].groupby("Type1").mean()
        
        self.Data5.plot(kind='bar', title= param+" moyen "+unité+" des pokemons likés par type")#pas pertinent de mettre un affichage "pie" pour ces stats
        
        plot.show()

    def ChangeMode(self):
        if (self.var2.get()==1):
            self.modeAffichage='pie'
        else:
            self.modeAffichage='bar'

    def ChangeTri(self):
        if (self.var.get()==1):
            self.tri=True
        else:
            self.tri=False
        
        
def     AffichDonneesPerso(): #Création de la fenetre tkinter

    fenetre = Tk()
    fenetre.title('Affichage des données statistiques')
    fenetre.geometry('300x450')
    Window(fenetre)

    fenetre.mainloop()

if __name__ == "__main__":
    AffichDonneesPerso()
