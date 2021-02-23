#-----constantes-----#
PREGUNTA_PESO = "cuanto pesas? : "
PREGUNTA_ESTATURA = "cuanto mides en metros? : "
MENSAJE_BIENVENIDA = "hola, como estas? vamos a calcular tu imc"
MENSAJE_DESPEDIDA = "tu imc es ..."
MENSAJE_BAJO_PESO = "estas muy delgado"
MENSAJE_PESO_ADECUADO = "estas en forma"
MENSAJE_SOBRE_PESO = "ten cuidado, estas en sobre peso"
MENSAJE_OBESO = "estas obeso, cuidado"

#-----entrada codigo-----#
print (MENSAJE_BIENVENIDA)
peso = float (input (PREGUNTA_PESO))
estatura = float (input (PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
isBajoPeso = imc < 18.5
isAdecuado = imc >=18.5 and imc < 25
isSobrePeso = imc >= 25 and imc < 30
resultado = ""
if (isBajoPeso) :
    resultado = MENSAJE_BAJO_PESO
elif (isAdecuado) : 
    resultado = MENSAJE_PESO_ADECUADO
elif (isSobrePeso) : 
    resultado = MENSAJE_SOBRE_PESO
else : 
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA)
print (resultado)

