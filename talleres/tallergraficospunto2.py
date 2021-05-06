#PUNTO 2 
#Cinco ciudades de Colombia, sobresaliendo la ciudad mas grande
import matplotlib.pyplot as plt 
pielabels = ['Cartagena, Barraqnuilla','Cucuta, Bogota','Medellin']
sizes = [15,10,30,25,20]
pieExplode = [0,0,1,0]
plt.pie (sizes,labels = pielabels,explode = pieExplode)
#######
plt.title ('Poblacion de habitantes en las ciudades de Colombia')
plt.show()