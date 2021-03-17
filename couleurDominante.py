from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
imgfile = Image.open("Images2/charizard.jpg")
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
    
plot.show()
couleursMoyennes=[['black',[0,0,0]],['gray',[128,128,128]],['red',[255,0,0]],['maroon',[128,0,0]],['yellow',[255,255,0]],
['olive',[128,128,0]],['lime',[0,255,0]],['green',[0,128,0]],['aqua',[0,255,255]],
['teal',[0,128,128]],['blue',[0,0,255]],['navy',[0,0,128]],['fuchsia',[255,0,255]],['purple',[128,0,128]]],['white',[255,255,255]]








print("end")