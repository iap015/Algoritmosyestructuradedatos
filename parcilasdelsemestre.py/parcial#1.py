#-----constantes-----#
mensajeBienvenida = "Hola, BIENVENIDO, hoy vamos averificar los valores del perfil lipidico"
mensajePreguntaHomocisteína = "Ingresar el nivel de Homocisteína en el paciente : "
mensajePreguntaTriglicéridos = "Ingresar el nivel de los triglicéridos en el paciente : "
mensajeresultado = "El resultado es {}"
MENSAJE_DESPEDIDA = "Que tenga un buen dia!"


#-----entrada codigo-----#
Homocisteína = float (input(mensajePreguntaHomocisteína))
if (Homocisteína > 2 and Homocisteína < 15):
    print (mensajeresultado.format("optimo, tiene un estado de salud bueno"))
elif (Homocisteína > 15 and Homocisteína > 30):
    print (mensajeresultado.format("sobre limite optimo, tenga cuidado"))
elif (Homocisteína > 30 and Homocisteína < 100):
    print (mensajeresultado.format("alto, debe cuidarse mas"))
else : 
    print (mensajeresultado.format("Muy alto! esta en riesgo"))

triglicéridos = float (input(mensajePreguntaTriglicéridos))
if (triglicéridos <= 150):
    print (mensajeresultado.format("optimo, esta en un nivel adecuado"))
elif (triglicéridos > 150 and triglicéridos < 199):
    print (mensajeresultado.format("sobre el limite optimo, cuiedese mas"))
elif (triglicéridos > 200 and triglicéridos < 499):
    print (mensajeresultado.format("Alto, tenga cuidado con su salud"))
else :
    print (mensajeresultado.format("Muy alto, consulte al medico mas frecuente"))

print (MENSAJE_DESPEDIDA)
