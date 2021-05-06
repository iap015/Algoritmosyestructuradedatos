#PUNTO 3
import panda as pd 
ecgData = pd.read_csv ('ppg.csv',encoding = 'UTF-8', header =  0, delimiter= ';').to_dict()
print(ecgData)
muestras = list(ecgData['muestra'].values())
voltaje = list (ecgData['valor'].values())
import matplotlib.pyplot as plt 
plt.plot (muestras,voltaje)
plt.title('Fotoplestimografía')
plt.xlabel('Tiempor en segundos')
plt.ylabel('Voltaje en mv')
plt.show()