print("Mexico, 2012:")

print("Era un niño de escasos recursos que vivia en una zona muy pobre del estado de Veracruz.")

print("")

print("El niño estaba ayudando a su mamá a lavar platos cuando un ruido muy fuerte se escucha en la parte de afuera de la casa, el niño salio de su casa para encontrarse con dos camionetas lobo blindada.")

print("")

print("Se lo llevaron apuntandole la boca de el arma en el estomago, el frio del metal del arma lo asusto tano que no pudo ni gritar.")

print("")

print("Los zetas se lo llevaron a su gefe maximo, el cual era LEAN, LEAN le dijo que no iba a pasar nada malo, pero dijo que su mamá lo iba a pagar.")

print("")

print("Entonces LEAN se llevo a la madre del pequeño niño el cual nunca la voleria a ver ")

print("")

print("La dos camionetas lobo blindadas se fueron de su casa, el niño se puso muy triste y entre lagrimas dijo, ME VOY A VENGAR, y asi es como comenzo la aventura del pequeño huerfano")

print("")

print("El pequeño huerfano furioso agarro su bicicleta y siguio a las dos camionetas sin pensar en las consecuencias")

print("")

#Propiedades del jugador

nombre = ""

salud = 120

ataque= 20

energia= 120

curacion = 30

costoCuracion= 30

#Propiedades de Zeta1

Zeta1 = "Zeta Torres"

saludZeta1 = 40

ataqueZeta1 = 5

#Comienza la aventura

print("- BIENVENIDO A LA AVENTURA")

nombre= input("- ¿COMO TE LLAMAS, VENGADOR?")

print("- ENCANTADO DE CONOCERTE, "+nombre)

print("- TE HAS ADENTRADO A LA GUARIDA DE LOS ZETAS")

print("- HA APARECIDO EL " + Zeta1)

#Comienza el combate

while salud > 0 and saludZeta1 > 0:
  print("- TU SALUD ES: " + str(salud))
  
  print("- TU ENERGIA ES: " +str(energia))
 
  print("- SALUD DEL ZETA: " + str(saludZeta1))
  
  print("- ATAQUE DEL ZETA: " + str(ataqueZeta1)) 
  
  
  respuesta = ""
  
  respuesta = input("- ¿QUE QUIERES HACER? a = Atacar: ("+str(ataque)+") / b = Curar (costo="+str(costoCuracion)+" , cantidad= "+str(curacion)+"): ")

  if respuesta == "a":
    saludZeta1 = saludZeta1 - ataque

  elif respuesta == "b" and energia >= costoCuracion:
    print("- ¡TE HAS CURADO!")
    
    energia = energia - costoCuracion
    
    salud = salud + curacion

  print("- ¡EL " + Zeta1 + " TE ATACA POR: " + str(ataqueZeta1))
  salud = salud - ataqueZeta1

print("- ¡HAS DERROTADO AL "+ Zeta1 + ", FELICIDADES!")

print("- TE HAS ADENTRADO MAS A LA GUARIDA ZETA")

print("")

print("La guarida estaba en el monte, alejado de la carretera cerca del farallon en un pueblo llamado limon, el calor del sol veracruzano lo tenia desgastado pero las ganas de ver a su madre le daban una resistensia como la de un diamante.")

print("")

print("Despues de buscar de arriba a abajo descrubio que su mamá no estaba en esa guarida estaba en otra mas al sur de veracruz por coatzacoalcos.")

print("")

print("Entonces agarro un autobus a coatzacoalcos y se adrento a la guarida en un monte.")

print("")

print("En el camino el autonbus frenó, todos los pasajeros sorpendidos pero la neblina de la carretera no los dejaba ver solamente se veian unas luces amarillas como de una camioneta, el conductor del autobus bajo.") 

print("")

print("Pasaron 12 segundos de silencio se escuchaban susurros desde afuera del autobus, era el conductor hablando con el dueño de la camioneta, al pasar los doce segundos se escucharon 12 balazos, la silueta apenas vicible del conductor se derrumbo.")

print("")

print("Los balazos seguian pero esta vez disparaban a las ventanas del autobus todos los pasajeros se tiraron al piso, los cristales dañaron al niño, el niño se armo de valor pensando en su madre y tomo el arma que robo de la guarida anterior y asi inicio el segundo enfrentamiento.")

print("")

#Propiedades de Zeta2

Zeta2 = "Zeta Mencho"

saludZeta2 = 60

ataqueZeta2 = 20

print("- TE HAS BAJADO DEL BUS Y TE ATACA EL "+ Zeta2 )

#Comienza el combate

while salud > 0 and saludZeta2 > 0:
  print("- TU SALUD ES: " + str(salud))
  
  print("- TU ENERGIA ES: " +str(energia))
 
  print("- SALUD DEL ZETA: " + str(saludZeta2))
  
  print("- ATAQUE DEL ZETA: " + str(ataqueZeta2)) 
  
  
  respuesta = ""
  
  respuesta = input("- ¿QUE QUIERES HACER? a = Atacar: ("+str(ataque)+") / b = Curar (costo="+str(costoCuracion)+" , cantidad= "+str(curacion)+"): ")

  if respuesta == "a":
    saludZeta2 = saludZeta2 - ataque

  elif respuesta == "b" and energia >= costoCuracion:
    print("- ¡TE HAS CURADO!")
    
    energia = energia - costoCuracion
    
    salud = salud + curacion

  print("- ¡EL " + Zeta2 + " TE ATACA POR: " + str(ataqueZeta2))
  salud = salud - ataqueZeta2

print("- ¡HAS DERROTADO AL "+ Zeta2 + ", FELICIDADES!")

print("")

print("Siguiendo su camino a coatzacoalcos el niño huerfano encuentra el cuartel de los Zetas, intenta entrar pero se encuantra a un grupo de Zetas resguardando el cuartel")

#Propiedades del Zeta3

Zeta3  = "Zeta Pepe"

saludZeta3 = 80

ataqueZeta3 = 25

print("- INTENTAS ENTRAR Y TE ATACA EL "+ Zeta3 )

#Comienza el combate

while salud > 0 and saludZeta3 > 0:
  print("- TU SALUD ES: " + str(salud))
  
  print("- TU ENERGIA ES: " +str(energia))
 
  print("- SALUD DEL ZETA: " + str(saludZeta3))
  
  print("- ATAQUE DEL ZETA: " + str(ataqueZeta3)) 
  
  
  respuesta = ""
  
  respuesta = input("- ¿QUE QUIERES HACER? a = Atacar: ("+str(ataque)+") / b = Curar (costo="+str(costoCuracion)+" , cantidad= "+str(curacion)+"): ")

  if respuesta == "a":
    saludZeta3 = saludZeta3 - ataque

  elif respuesta == "b" and energia >= costoCuracion:
    print("- ¡TE HAS CURADO!")
    
    energia = energia - costoCuracion
    
    salud = salud + curacion

  print("- ¡EL " + Zeta3 + " TE ATACA POR: " + str(ataqueZeta3))
  salud = salud - ataqueZeta3

print("- ¡HAS DERROTADO AL "+ Zeta3 + ", FELICIDADES!")

print(" LE LLEGA POR LAS ESPALDAS EL ZETA")

#Propiedades del Zeta4

Zeta4  = "Zeta Persian"

saludZeta4 = 100

ataqueZeta4 = 25

print("- INTENTAS ENTRAR Y TE ATACA EL "+ Zeta4 )

#Comienza el combate

while salud > 0 and saludZeta4 > 0:
  print("- TU SALUD ES: " + str(salud))
  
  print("- TU ENERGIA ES: " +str(energia))
 
  print("- SALUD DEL ZETA: " + str(saludZeta4))
  
  print("- ATAQUE DEL ZETA: " + str(ataqueZeta4)) 
  
  
  respuesta = ""
  
  respuesta = input("- ¿QUE QUIERES HACER? a = Atacar: ("+str(ataque)+") / b = Curar (costo="+str(costoCuracion)+" , cantidad= "+str(curacion)+"): ")

  if respuesta == "a":
    saludZeta4 = saludZeta4 - ataque

  elif respuesta == "b" and energia >= costoCuracion:
    print("- ¡TE HAS CURADO!")
    
    energia = energia - costoCuracion
    
    salud = salud + curacion

  print("- ¡EL " + Zeta4 + " TE ATACA POR: " + str(ataqueZeta4))
  salud = salud - ataqueZeta4

print("- ¡HAS DERROTADO AL "+ Zeta4 + ", FELICIDADES!")