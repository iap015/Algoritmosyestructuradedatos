class Usuario ():
    def __init__ (self, nombreIn, edadIn, sexoIn, nacionalidadIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.sexo = sexoIn
        self.nacionalidad = nacionalidadIn
    def hablar (self):
        print (f'''Hola soy {self.nombre}, pertenezco al sexo {self.sexo}
        tengo {self.edad} años y soy de nacionalidad {self.nacionalidad}''')


    def mostrarAtributos (self, cancionIn):
        self.cancion = cancionIn
        print (f'''Hola soy {self.nombre} y estoy escuchando la cancion {self.cancion}
    ''')
usuario1 = Usuario('Mateo', 28, 'Masculino', 'Colombiana')
usuario1.mostrarAtributos('El color de tus ojos')


class Artista (Usuario):
    def __init__(self, nombreIn, edadIn, sexoIn, nacionalidadIn, GenmusicalIn, NumdecancionespubIn, NumdealbumnsIn):
        Usuario.__init__(self, nombreIn, edadIn, sexoIn, nacionalidadIn)
        self.generomusical = GenmusicalIn
        self.numerodecacionespublicadas = NumdecancionespubIn
        self.numerodealbumns = NumdealbumnsIn
    def cantar (self,ciudad):
        print (f'''Hola, {ciudad}. Mi nombre es {self.nombre} y nos vemos este
        28 de Noviembre. ¡Compra tu boleta ya!
        ''')
artista1 = Artista('Malbin', 21, 'Masculino', 'Colombiana', 'Reggaeton', 5, 1)
artista1.cantar('Medellín')







