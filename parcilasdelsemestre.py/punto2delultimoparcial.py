#PUNTO 2 
class Humano ():
    def __init__ (self, nombreIn, sexoIn, edadIn):
        self.nombre = nombreIn
        self.sexo = sexoIn
        self.edad = edadIn

    def hablar (self,mensaje):
        print (f'''Hola soy {self.nombre}, vengo con mensaje para ustedes...''', mensaje)

class Doctor (Humano):
    def calcularIMC (self, peso, estatura):
        imc = peso/(estatura**2)
        print (f'''hola mi nombre es {self.nombre}, voy a calcular tu IMC (indice de masa corporal)''')
        print (imc)

humano = Humano ('Bella', 18, 'femenino')
humano.hablar ('Que tengas lindo dia y te vaya super bien')
doctor = Doctor ('Bella', 18, 'femenino')
doctor.calcularIMC (56, 1.62)
