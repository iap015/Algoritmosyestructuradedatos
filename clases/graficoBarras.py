#Aqui explicaremos como hacer un grafico de barras
import matplotlib.pyplot as plt 
lenguajes = ['py','java', 'dart','elixir']
encuesta = [50,10,30,10]
plt.bar(lenguajes, encuesta, width = 0.6, color = 'g')
#########
#titulo
plt.title('lenguajes mas usados')
plt.xlabel('lenguajes de programacion')
plt.ylabel('% de uso de lenguajes')
plt.savefig('graficoLenguajes.png')
#########
plt.show()

