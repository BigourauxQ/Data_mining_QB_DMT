from os import listdir
from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

import csv

def CouleurDominante():
    rows = [] #On crée la liste qu'on va remplire au fur et à mesure puis stocker dans un fichier csv
    rows.append(['Name', 'couleur1','couleur2'])
    for img in listdir("images"): #On va récuperer les images téléchargées
        pokemon = img.split(".")[0]
        imgfile = Image.open("images/"+img)  #Algo Kmeans largement inspiré de celui des tps
        numarray = numpy.array(imgfile.getdata(), numpy.uint8)
        clusters = KMeans(n_clusters = 5)
        clusters.fit(numarray)
        npbins = numpy.arange(0, 6)
        histogram = numpy.histogram(clusters.labels_, bins=npbins)
        
        hist=[]
        Index=[]
        for i in histogram[0]:   #On ne récupère que les 3 couleurs les plus dominantes en retriant 3 fois notre tableau
            hist.append(i); #Il faut d'abord transformer l'histogramme en tableau triable
        for i in range(0,3):
            Index.append(hist.index(max(hist))) #On récupere les indexes des 3 couleurs dominantes une par une 
            hist[hist.index(max(hist))]=0.0
        #print(Index)




    #Liste de toutes les couleurs principales avec leur code RGB hexa
        couleursMoyennes=[['black',[0,0,0]],['gray',[128,128,128]],['red',[255,0,0]],['maroon',[128,0,0]],['yellow',[255,255,0]],
        ['olive',[128,128,0]],['lime',[0,255,0]],['green',[0,128,0]],['aqua',[0,255,255]],
        ['teal',[0,128,128]],['blue',[0,0,255]],['navy',[0,0,128]],['fuchsia',[255,0,255]],['purple',[128,0,128]],['white',[255,255,255]],
        ['soft blue',[0,128,255]],['soft green',[0,255,128]],['soft purple',[128,0,255]],['purple-blue',[128,128,255]],['green-yellow',[128,255,0]],['very soft green',[128,255,128]],
        ['very soft blue',[128,255,255]],['pink',[255,0,128]],['orange',[255,128,0]],['beige',[255,128,128]],['soft pink',[255,128,255]],['soft orange',[255,255,128]]
        ]

        couleurs=[]
        for ind in Index: #On va maintenant arrondir les couleurs dominantes par la couleur principale la plus proche. 
            
            for i in range(0, len(couleursMoyennes)):
                if abs(round(clusters.cluster_centers_[ind][0])-couleursMoyennes[i][1][0])<64 and abs(round(clusters.cluster_centers_[ind][1])-couleursMoyennes[i][1][1])<64 and abs(round(clusters.cluster_centers_[ind][2])-couleursMoyennes[i][1][2])<64 :
                    #print(couleursMoyennes[i][0])
                    if couleursMoyennes[i][0] !='white':
                        couleurs.append(couleursMoyennes[i][0])
        while len(couleurs)!=2:
            couleurs.append('white')
                        
        rows.append([pokemon,couleurs[0],couleurs[1]]) #On ajoute ce résultat à un tableau csv. Comme nos images ont un fond blanc , on traite spécialement cette couleur.
        with open('DataCouleurTest.csv','w', newline='') as f_output:
                csv_output = csv.writer(f_output)
                csv_output.writerows(rows)


    print("end")
if __name__ == "__main__":    
    CouleurDominante()