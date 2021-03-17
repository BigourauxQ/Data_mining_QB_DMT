from os import listdir
from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

import csv

rows = []
rows.append(['pokemon', 'couleurs'])
for img in listdir("./Images2"):
    pokemon = img.split(".")[0]
    imgfile = Image.open("Images2/"+img)
    numarray = numpy.array(imgfile.getdata(), numpy.uint8)
    clusters = KMeans(n_clusters = 5)
    clusters.fit(numarray)
    npbins = numpy.arange(0, 6)
    histogram = numpy.histogram(clusters.labels_, bins=npbins)
    labels = numpy.unique(clusters.labels_)
    barlist = plot.bar(labels, histogram[0])
    for i in range(5):
        barlist[i].set_color('#%02x%02x%02x' % (
        math.ceil(clusters.cluster_centers_[i][0]), 
            math.ceil(clusters.cluster_centers_[i][1]),
        math.ceil(clusters.cluster_centers_[i][2])))
        
    #plot.show()
    hist=[]
    Index=[]
    for i in histogram[0]:
        hist.append(i);
    for i in range(0,3):
        Index.append(hist.index(max(hist)))
        hist[hist.index(max(hist))]=0.0
    print(Index)





    couleursMoyennes=[['black',[0,0,0]],['gray',[128,128,128]],['red',[255,0,0]],['maroon',[128,0,0]],['yellow',[255,255,0]],
    ['olive',[128,128,0]],['lime',[0,255,0]],['green',[0,128,0]],['aqua',[0,255,255]],
    ['teal',[0,128,128]],['blue',[0,0,255]],['navy',[0,0,128]],['fuchsia',[255,0,255]],['purple',[128,0,128]],['white',[255,255,255]],
    ['soft blue',[0,128,255]],['soft green',[0,255,128]],['soft purple',[128,0,255]],['purple-blue',[128,128,255]],['green-yellow',[128,255,0]],['very soft green',[128,255,128]],
    ['very soft blue',[128,255,255]],['pink',[255,0,128]],['orange',[255,128,0]],['beige',[255,128,128]],['soft pink',[255,128,255]],['soft orange',[255,255,128]]


    ]


    #couleursMoyennes=[['black',[0,0,0]],['red',[255,0,0]],['yellow',[255,255,0]],['lime',[0,255,0]],['aqua',[0,255,255]],['blue',[0,0,255]],['fuchsia',[255,0,255]],['white',[255,255,255]]]
    couleurs=[]
    for ind in Index:
        
        for i in range(0, len(couleursMoyennes)):
            if abs(round(clusters.cluster_centers_[ind][0])-couleursMoyennes[i][1][0])<64 and abs(round(clusters.cluster_centers_[ind][1])-couleursMoyennes[i][1][1])<64 and abs(round(clusters.cluster_centers_[ind][2])-couleursMoyennes[i][1][2])<64 :
                print(couleursMoyennes[i][0])
                if couleursMoyennes[i][0] !='white':
                    couleurs.append(couleursMoyennes[i][0])
                    
    rows.append([pokemon,couleurs])
    with open('DataCouleur.csv','w', newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(rows)





print("end")