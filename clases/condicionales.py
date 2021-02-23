print (2 == 2)
print (2 != 2)
print (2 >3)
print (2 <3)
print (2 == 2 and 2 != 2 )
print ( 2 == 2 and 3 !=2 )

preguntaEdad = "Ingrese su edad : "
mensajeMayorEdad = "Puedes pasa eres mayor"
mensajeMayorEdadBienvenido = "Bienvenido a nuestro bar"
mensajeMenorEdad = "Eres menor de edad no puedes ingresar a nuestro bar"
mensajeDescuento = "Eres afortunado tienes un 40% de descuento el dia de hoy"
mensajeDescuentoAdultoMayor = "Eres afortunado tienes un 50% de descuento el dia de hoy"
edad = int (input(preguntaEdad))
if (edad >= 18 and edad <=40):
    print (mensajeMayorEdad)
    print (mensajeMayorEdadBienvenido)
elif (edad >= 40 and edad <=50):
    print (mensajeMayorEdad)
    print (mensajeMayorEdadBienvenido)
    print (mensajeDescuento)
elif (edad > 50):
    print (mensajeMayorEdad)
    print (mensajeMayorEdadBienvenido)
    print (mensajeDescuento)
else :
    print (mensajeMenorEdad) 

print ("CHAOO!!")

