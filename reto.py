# Examen

preguntas={"¿2+2? = 4": "SI", "¿3+5=8?" : "SI","¿7+7=15?" : "NO"}
#cont = 0
resultado = 0


for i in preguntas.keys():

     print(i)
     respuesta=input(": ")
     if respuesta == preguntas.get(i, "Sin valor"):
         resultado += 1


print(resultado)