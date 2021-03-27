#!/usr/bin/ev python
#coding: utf-8


from tkinter import  * #Mauvaise pratique qu'on retrouvera tout au long du projet mais plus le temps d'importer "as tk"....
import pandas as pd
import csv

class Window(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master = master

        self.InscriptionReussie =False

        self.ListUsers = pd.read_csv("Users.csv", encoding = "ISO-8859-1")

        self.MessageErreur= Label(self.master)
        self.MessageErreur.grid(row=3, column=1, pady = 10)

        # zone de texte pour mettre son pseudo
        etiquettePseudo = Label(self.master, text='Pseudo :')
        etiquettePseudo.grid(row=0, column=0,pady = 10)
        self.entreePseudo = Entry(self.master, width=30)
        self.entreePseudo.grid(row=0, column=1,padx=10, pady = 10)
        
        # zone de texte pour mettre son mote de passe
        etiquetteMdp = Label(self.master, text='Mot de passe :')
        etiquetteMdp.grid(row=1, column=0,padx=5, pady = 5)
        self.entreeMdp = Entry(self.master, width=30)
        self.entreeMdp.grid(row=1, column=1,padx=10, pady = 5)

        # zone de texte pour confirmez son mote de passe
        etiquetteMdp2 = Label(self.master, text='Confirmez le mot de passe :')
        etiquetteMdp2.grid(row=2, column=0, padx=5,pady = 0)
        self.entreeMdp2 = Entry(self.master, width=30)
        self.entreeMdp2.grid(row=2, column=1,padx=10, pady = 0)
        
        # Bouton de validation
        BoutonInscription=Button(self.master, fg ='green' ,width=12, height=2, text="Valider", command=lambda:self.ValidInscription())
        BoutonInscription.grid(row=3, column=0, padx=10,pady = 15)

    
    def ValidInscription(self):
        """ Pour valider l'inscription
        """

        if self.entreeMdp.get()==self.entreeMdp2.get():# si les mots de passes correspondes

            isInUsers = False

            with open('Users.csv','r') as users:

                reader=csv.reader(users)
                header = next(users) #On ne veut pas iterer sur la premiere ligne qui correspond au nom des clonens, on le skip donc

                for line in reader:

                    if (line[0]==self.entreePseudo.get()):# si l'utilisateur existe deja

                        self.MessageErreur.destroy()
                        self.MessageErreur= Label(self.master, text='Pseudo déjà utilisé', fg ='red')
                        self.MessageErreur.grid(row=3, column=1, pady = 10)
                        isInUsers=True
                        break

                if isInUsers==False:
                    
                    UserCourant=[]
                    UserCourant.append(['Pseudo'])
                    UserCourant.append([self.entreePseudo.get()])
                   
                    AddToUser=[]
                    AddToUser.append([self.entreePseudo.get(),self.entreeMdp.get()])
                    
                    
                    with open('UserCourant.csv','w', newline='') as f_output: #On ajoute le nouvel utilisateur a la BDD, et au fichier de l'utilisateur courant
                        csv_output = csv.writer(f_output)   
                        csv_output.writerows(UserCourant)
                        
                    with open('Users.csv','a', newline='') as f_output:
                        csv_output = csv.writer(f_output)   
                        csv_output.writerows(AddToUser)
                    
                    self.InscriptionReussie=True
                    self.master.destroy()
        else:

            self.MessageErreur.destroy()
            self.MessageErreur= Label(self.master, text='Les 2 passwords sont différents !', fg ='red')
            self.MessageErreur.grid(row=3, column=1, pady = 10)
                    

        



def Inscription(): #Création de la fenetre tkinter

    fenetre = Tk()
    fenetre.title('Interface Inscription')
    
    Win= Window(fenetre)

    fenetre.mainloop()

    return Win.InscriptionReussie

if __name__ == "__main__":
    Inscription()