#-----PRIMER PUNTO-----#
#Crear una funcion que muestre en pantalla la suma, la resta, la multiplicacion, la division y la potencia.
def la_funcion(numero1, numero2, numero3):
    print (numero1 + numero2 + numero3)
    print (numero1 - numero2 - numero3)
    print (numero1*numero2*numero3)
    print (numero1/numero2/numero3)
    print (numero1**numero2**numero3)

la_funcion(5,6,2)


#-----SEGUNDO PUNTO-----#
#Crear una funcion dada tres listas del mismo tamaño.
def MostrarElemento (lista):
    for elemento in lista :
        print (elemento)
ObjetosDeCocina = ["cuchara", "olla", "tenedor", "espatula", "trapo"]
ObjetosDeCasa = ["sillon", "cama", "comedor","cuadro", "toalla"]
Zapatos = ["tacones", "botas", "zapatillas","chanclas","baletas"]

MostrarElemento (ObjetosDeCocina)
MostrarElemento (ObjetosDeCasa)
MostrarElemento (Zapatos)


#-----TERCER PUNTO-----#
#Crear una funcion que calcule el área y la devuelva.
BasePregunta = "ingerese la cifra que quiera para el valor de la base del triangulo:"
AlturaPregunta = "ingerese la cifra que quiera para el valor de la altura del triangulo"

Base = float (input(BasePregunta))
Altura = float (input(AlturaPregunta))

def ÁreaDelTriangulo ():
    área = (Base*Altura)/2
    return área

resultado = ÁreaDelTriangulo ()
print (resultado)


#-----CUARTO PUNTO-----#
#Crear una funcion que muestre el promedio, el minimo y el maximo.
def NumerosEnteros (lista):
    máximo = max (lista)
    mínimo = min (lista)
    datos = 0
    for elemento in lista:
        datos += elemento
    tamañoLista = len (lista)
    promedio = datos / tamañoLista
    print (f"numero mayor en la lista es el {máximo}, el menor {mínimo} y el promedio es {promedio}")

numeros = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
NumerosEnteros (numeros)


#-----QUINTO PUNTO-----#
def Sucesión (posicion):
    L = 0
    I = 0
    for elemento in range (posicion -1):
        A = L + I
        L = I
        I = A
    return (L)

número = Sucesión (5)
print ("El número que corresponde a el patrón es", número)

