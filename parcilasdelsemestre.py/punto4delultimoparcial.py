#PUNTO 4 
nombreArchivo = 'pacientes.txt'

try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    descripcionArchivo = 'Consultorio de neurología'
    archivo.writelines(descripcionArchivo)
    archivo.close()

nombrePaciente = input('Por favor ingresa el nombre del paciente:')
enfermedad = input('Por favor ingresa la descripcion de la enfermedad:')
valorConsulta = 0

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        valorConsulta= int(input('Por favor ingresa el valor de la consulta:'))
        isCorrectInfo = True 
    except ValueError:
        print('Lo siento, ingresaste un dato no valido')


archivo = open (nombreArchivo, 'a', encoding='UTF-8')
archivo.write(f"Equipo: {nombrePaciente}\n")
archivo.write(f"Descripcion: {enfermedad}\n")
archivo.write(f"Precio mantenimiento: {valorConsulta}\n")
archivo.write("======================\n")
archivo.close()
