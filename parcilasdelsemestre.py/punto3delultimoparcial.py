#PUNTO 3
def ConversorEurosEnDolares ():
    isCorrectInfo = False
    while (isCorrectInfo == False):
        try:
            nombre = input("Por favor ingresa tu nombre:")
            assert (nombre.isalpha())
            isCorrectInfo = True
        except AssertionError:
            print("Lo siento, ingresaste un dato no valido")
    
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            dinero = float(input("Por Favor ingresa la cantidad de dinero en dolares:"))
            isCorrectInfo = True
        except ValueError:
            print("Lo siento, ingresaste un dato no valido")

    print(f'''Hola {nombre}, tu cantidad de dinero en euros es {dinero*0.82}''')
ConversorEurosEnDolares()
