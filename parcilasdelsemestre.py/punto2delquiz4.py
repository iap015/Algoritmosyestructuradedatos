#PUNTO 2 pida al usuario 5 ciudades favoritas en el mundo y sus poblaciones
import matplotlib.pyplot as plt
listaCiudades = []
listaPoblaciones = []
for i in range (5):
    ciudad = input ('Ingresa una ciudad :')
    poblacion = input('Ingresa la población correspondiente de la ciudad:')
    listaCiudades.append(ciudad)
    listaPoblaciones.append(poblacion)

print (listaCiudades)
print (listaPoblaciones)
maximo = listaPoblaciones.index(max(listaPoblaciones))
pieExplode = [0,0,0,0,0]

pieExplode [maximo]= 0.2

plt.pie(listaPoblaciones, labels=listaCiudades, explode= pieExplode)
plt.title('Ciudades favoritas y su población')

plt.savefig('graficaciudades.png')
plt.show()
