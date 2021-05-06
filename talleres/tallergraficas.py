#PUNTO 1 
#niveles de ingreso de una persona durante el 2020 
import matplotlib.pyplot as plt 
Meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Agto','Sep','Oct','Nov','Dic']
IngresosMesaMes = [1200000, 2340000, 5780000, 5990000, 8320000, 3123000, 1503000, 4222000, 2000990, 2231000, 9210000, 3098000]
plt.bar(Meses, IngresosMesaMes, width = 0.4, color = ['g','r','y','m','c','k','b','g','r','y','c','k'] )
########
plt.title('ingresos mensuales 2020')
plt.xlabel('meses')
plt.ylabel('cantidad de ingresos en $')
plt.savefig('graficoingresosmensuales.png')
plt.show()





