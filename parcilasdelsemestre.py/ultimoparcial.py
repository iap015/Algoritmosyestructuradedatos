#PUNTO 1
import matplotlib.pyplot as plt
listaAlimentos = []
listaPrecios = []
for i in range (8): 
    Alimento = input ('Por favor ingresa uno de tu alimentos favoritos:')
    Precio = input ('Por favor ingresa el precio de este alimento :')
    listaAlimentos.append(Alimento)
    listaPrecios.append(Precio)

plt.bar(listaAlimentos, listaPrecios, width= 0.5, color = 'y')
##########
plt.title('Comidas favoritas')
plt.xlabel('Alimentos')
plt.ylabel('Precios')
plt.savefig('Graficodelosalimentosfavoritosysusprecios.png')
plt.show()
