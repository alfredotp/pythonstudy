# Examen
# Realiza un examen con 3 preguntas que tu desees, el usuario deberá responder "SI" o "NO" y al final otorgarle una calificación (La calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)

preguntas={"¿2+2? = 4": "SI", "¿3+5=8?" : "SI","¿7+7=15?" : "NO"}
resultado = 0

for i in preguntas.keys():

     print(i)
     respuesta=input(": ")
     if respuesta == preguntas.get(i, "Sin valor"):
         resultado += 1

print(resultado)

