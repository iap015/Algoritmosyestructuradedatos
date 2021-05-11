#PUNTO 1: pida al usuario 5 snacks y sus respectivos precios
import matplotlib.pyplot as plt 
lista1= []
lista2= []
for i in range (5):
    snacks= input('Ingresa tu snacks favorito :')
    lista1.append(snacks)
print(lista1)
for i in range(5):
    precios= input('¿cuanto cuestan tus snacks?:')
    lista2.append(precios)
print(lista2)
plt.bar(lista1,lista2, width= 0.6, color= 'g')
plt.title('SNAKCS FAVORITOS Y SUS PRECIOS')
plt.xlabel('SANCKS')
plt.ylabel('PRECIO')
plt.savefig('graficosnacks.png')
plt.show()
