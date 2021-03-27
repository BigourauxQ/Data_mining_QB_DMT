from tkinter import  * #Mauvaise pratique qu'on retrouvera tout au long du projet mais plus le temps d'importer "as tk"....
import pandas as pd
import Inscriptions
import csv

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.isInUsers =False

        self.ListUsers = pd.read_csv("Users.csv", encoding = "ISO-8859-1")

        etiquettePseudo = Label(self.master, text='Pseudo :')
        etiquettePseudo.grid(row=0, column=0,pady = 10)

        self.entreePseudo = Entry(self.master, width=30)
        self.entreePseudo.grid(row=0, column=1,padx=10, pady = 10)
        

        etiquetteMdp = Label(self.master, text='Mot de passe :')
        etiquetteMdp.grid(row=1, column=0, pady = 10)

        self.entreeMdp = Entry(self.master, width=30, show="*")
        self.entreeMdp.grid(row=1, column=1,padx=10, pady = 10)


        BoutonCo=Button(self.master, fg ='green' ,width=12, height=2, text="Se connecter", command=lambda:self.VerifCo())
        BoutonCo.grid(row=2, column=0,padx=10, pady = 10)

        BoutonNewco=Button(self.master, fg ='blue' ,width=12, height=2, text="S'inscrire", command=lambda:self.GoInscription())
        BoutonNewco.grid(row=2, column=1, padx=10, pady = 10,sticky='w')

    def VerifCo(self):
        user =[self.entreePseudo.get(), self.entreeMdp.get()]
        
        with open('Users.csv','r') as users:
            reader=csv.reader(users)
            header = next(users) #On ne veut pas iterer sur la premiere ligne qui correspond au nom des clonens, on le skip donc
            for line in reader:
                if (line[0:2]==user):
                    UserCourant=[]
                    UserCourant.append(['Pseudo'])
                    UserCourant.append([self.entreePseudo.get()])
                    with open('UserCourant.csv','w', newline='') as f_output:
                        csv_output = csv.writer(f_output)   
                        csv_output.writerows(UserCourant)
                        
                    self.isInUsers=True
                    self.master.destroy()

                    break
            if (self.isInUsers==False):
                MessageErreur= Label(self.master, text='Identification ratée', fg ='red')
                MessageErreur.grid(row=3, column=1, pady = 10)
            
        
    
    def GoInscription(self):
        
        self.master.destroy()
        self.isInUsers=Inscriptions.Inscription()



def Connexion(): #Création de la fenetre tkinter

    fenetre = Tk()
    fenetre.title('Interface Connexion')
    fenetre.geometry()
    Win =Window(fenetre)

    fenetre.mainloop()
    return Win.isInUsers


if __name__ == "__main__":
    Connexion()