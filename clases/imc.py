#-----constantes-----#
PREGUNTA_PESO = "cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "cuanto mides en metros? : "
MENSAJE_BIENVENIDA = "hola, como estas? calculemos tu imc"
MENSAJE_DESPEDIDA = "tu imc es ..."

#-----entrada codigo-----#
print (MENSAJE_BIENVENIDA)
peso = float (input (PREGUNTA_PESO))
estatura = float (input (PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print (MENSAJE_BIENVENIDA, imc)
isObeso = imc >= 30
print ("el resultado de la prueba de obesidad es ...")
