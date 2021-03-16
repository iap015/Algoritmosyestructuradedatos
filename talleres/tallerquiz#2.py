#-----constantes-----#
listaTemperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
PreguntaTemperatura = '''
    C- mostrar lista original en Celsius
    K- mostrar en grados Kelvin
    F- mostrar en grados Farenheit
'''
#-----MENSAJES-----#
MensajeGradosKelvin = 'exponiendo la lista en grados Kelvin'
MensajeGradosCelsius = 'la lista ya está en celsius, no es necesaria la conversión'
MensajeGradoFarenheit = 'exponiendo la lista en grados Farenheit'
MensajeEntradaNoValido = 'número depositado no es valido'
MensajeOpción = 'tu elegiste la opción {}'
MensajeTemMáxima = 'la temperatura máxima es -->'
MensajeTemMínima = 'la temperatura mínima es -->'

masAlto = max (listaTemperaturaCorporal)
masBajo = min (listaTemperaturaCorporal)
MensajeSalida = 'Gracias por contar con este programa, ¡tenga lindo dia!'

#-----pregunta inicial-----#
PreguntaNumeros = '''Deposite una de estas opciones
    1.Hacer conversión de grados Celsius a Kelvin o a Farenheit.
    2.Mostrar si es una hipotermia, una fiebre o temperatura normal.
    3.Mostrar la temperatura máxima y la temperatura mínima.
    4.Salir.
'''
#----PUNTO1-----#
listaFarenheit = []
listaKelvin = []
for elemento in listaTemperaturaCorporal : 
    farenheit = round (elemento * 1.8) + 32
    listaFarenheit.append (farenheit)
for elemento in listaTemperaturaCorporal : 
    kelvin = round (elemento + 273.15)
    listaKelvin.append(kelvin)

#-----PUNTO2-----#
listaClasificación = []
for elemento in listaTemperaturaCorporal : 
    clasificación = ""
    if (elemento < 36):
        clasificación = "HIPOTERMIA"
    elif (elemento >= 36 and elemento <= 37.5): 
        clasificación = "TEMPERATURA ES NORMAL"
    elif (elemento >= 37.6):
        clasificación = "FIEBRE"
    else:
        clasificación = "DATOS NO POSIBLES"
    listaClasificación.append(clasificación)

#-----PUNTO3-----#

#-----OPCIONES DE INICIO-----#
opcionSelecta = int(input(PreguntaNumeros))
while (opcionSelecta !=4):
    if (opcionSelecta == 1): 
        opcionTemperatura = input (PreguntaTemperatura)
        if (opcionTemperatura == 'C'):
            print (MensajeGradosCelsius)
            print (listaTemperaturaCorporal)
        elif (opcionTemperatura == 'K'): 
            print (listaKelvin)
        elif (opcionTemperatura == 'F'):
            print (listaFarenheit)
        else : 
            print (MensajeEntradaNoValido)
    elif (opcionSelecta == 2): 
        print (MensajeOpción.format(2))
        print (listaClasificación)
    elif (opcionSelecta == 3): 
        print (MensajeOpción.format(3))
        print ("temperatura máxima", masAlto)
        print ("temperatura mínima", masBajo)
    else :
        print (MensajeEntradaNoValido)
    opcionSelecta = int (input(PreguntaNumeros))
print (MensajeSalida)
