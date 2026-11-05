# #Nombre = "Gabriel Alvarez "
#Edad = "19"
#print(f"¡hola, {Nombre} !")
#print(f"🎉 ¡Felíz {Edad} años!,espero sigas cumpliendo muchos mas ")
#El programa te hace preguntas 
#Nombre = input("¿Como te llamas?")
#Edad = input("¿Cuántos años tienes?")
#Nombre = "Gabriel"
#Edad = "19"
#El programa te responde usando tus preguntas 
#print(f"¡hola!,me llamo {Nombre} ")
#print(f"voy a cumplir {Edad} años")
#Primera conversación= Nombre 
#Nombre = input("¿Cómo te llamas?")
#Nombre = "Gabriel Alvarez "
#print(f"¡Hola!, me llamo {Nombre} mucho gusto")
#Segunda conversación = Edad 
#Edad = input("¿cuántos años tienes?")
#Edad = "19"
#print(f"voy a cumplir {Edad} años este año")
#El programa te oregunta tu nombre
#Nombre = input("¿Cómo te llamas?")
#Nombre = "Emilio"
#print(f"¡Hola!,me llamo {Nombre} es un placer")
# Te pregunta tu edad actual
#Edad = input("¿Cuántos años tienes?")
#Edad = 19
#print(f"Actualmente tengo {Edad} años")
#Cual seria tu edad el próximo año 
#Edad_siguiente = input("¿Cuál seria tu edad el próximo año? ")
#Convertirmos la edad en número y le sumamos +1 para el próximo año 
#Edad_siguiente = int(Edad) +1
#print(f" el próximo año tendre {Edad_siguiente} años")
#python if/else mas .lower()
#---Bienvenida al jugador---
Nombre = input("¿Cómo te llamas?\n")
print(f"\n ¡Hola, Bienvenido {Nombre} a tu exmanen de trivia!")
print(f" ¡Prepárate,vamos a empezar!\n ")
#---SISTEMA DE CALIFICACION---
#Empezamos el examen con 0 puntos 
puntos = 0

#--- Pregunta 1 ---
respuesta = input("¿Cuál es el mejor lenguaje para empezar a programar?")
if respuesta.lower() == "python" :
    print(f"☑️ ¡Excelente!, ¡bien hecho! ☑️")
    puntos = puntos + 33.3 # <--¡Sumamos 33.3 puntos aquí!
else :
    print(f"✖️ ¡Incorrecto!, el mejor lenguaje para empezar es python. ")
  
#--- Pregunta 2 ---
print(f"\n¡Vamos con la segunda pregunta!") 
respuesta_2 = input("¿cuál es el río mas largo del mundo?\n")                                                      
#Convertimos la respuesta a minúsculas para evitar errores
if respuesta_2.lower() == "amazonas" :
    print(f"✔️ ¡Excelente! , ¡Sigue asi !")
    puntos = puntos + 33.3 # <--¡Sumamos otros 33.3 puntos aquí!
else :
    print(f"✖️ ¡Fallaste!, la respuesta corecta era el amazonas")
  
#--- Pregunta 3 ---
print(f"\n ¡Vamos con la tercera pregunta!")
respuesta_3 = input("¿Cuál es la serpiente más grande del amazonas?\n ")
if respuesta_3.lower() == "anaconda verde" :
    print(f"✔️¡Excelente, bien dicho!")
    puntos = puntos + 33.3 # <--¡Sumamos otros 33.3 puntos aquí!
else :
    print(f"✖️¡Fallaste!, la respuesta correcta era anaconda 🐍")
  
#--- Pregunta 4 ---
print(f"\n ¡Vamos con la cuarta pregunta!")
respuesta_4 = input("¿Qué país tiene forma de bota en europa?\n ")
if respuesta_4.lower() == "italia" :
    print(f"¡Excelente!, ¡Vas con todo!🇮🇹")
    puntos = puntos + 33.3 #<--¡Sumamos otros 33.3 puntos aquí!
else :
    print(f"✖️¡Fallaste!, la respuesta correcta era italia")
  
#--- Pregunta 5 ---
print(f"\n¡Última pregunta por los 100 puntos!")
respuesta_5 = input("¿Cuál es el océano más grande del mundo?\n")
if respuesta_5.lower() == "pacífico" or respuesta_5.lower() == "pacifico" :
    print(f"☑️¡Perfecto!, terminaste el examen")
    puntos = puntos + 33.3  
else :
  print(f"✖️ ¡Fallaste!, la respuesta correcta era el pacifico")
  
#--- Pregunta 6 ---
print(f"\n¡Vamos con la sexta pregunta!")
respuesta_6 = input("¿Cuál es el animal terrestre más rápido del mundo?\n")
if respuesta_6.lower() == "guepardo" or respuesta_6.lower() == "chita":
    print(f"☑️ ¡Increíble, eres muy rápido!")
    puntos = puntos + 33.33 
else:
    print(f"✖️ ¡Fallaste!, era el guepardo o chita 🐆")

#--- Pregunta 7 ---
print(f"\n¡Vamos con la séptima pregunta!")
respuesta_7 = input("¿De qué color es la clorofila de las plantas?\n")
if respuesta_7.lower() == "verde":
    print(f"☑️ ¡Muy bien hecho!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era verde 🍃")

#--- Pregunta 8 ---
print(f"\n¡Vamos con la octava pregunta!")
respuesta_8 = input("¿Qué animal es conocido como el rey de la selva?\n")
if respuesta_8.lower() == "león" or respuesta_8.lower() == "leon":
    print(f"☑️ ¡Excelente, rugiste fuerte!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Incorrecto!, la respuesta era el león 🦁")

#--- Pregunta 9 ---
print(f"\n¡Vamos con la novena pregunta!")
respuesta_9 = input("¿Cuál es el mamífero más grande de todo el planeta?\n")
if respuesta_9.lower() == "ballena azul" or respuesta_9.lower() == "ballena":
    print(f"☑️ ¡Impresionante, respuesta correcta!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, era la ballena azul 🐋")

#--- Pregunta 10 ---
print(f"\n¡Vamos con la décima pregunta!")
respuesta_10 = input("¿Qué insecto produce miel?\n")
if respuesta_10.lower() == "abeja" or respuesta_10.lower() == "abejas":
    print(f"☑️ ¡Dulce respuesta, correcto!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era la abeja 🐝")

#--- Pregunta 11 ---
print(f"\n¡Vamos con la pregunta 11!")
respuesta_11 = input("¿Cómo se llama el satélite natural de la Tierra?\n")
if respuesta_11.lower() == "luna":
    print(f"☑️ ¡Correcto, brillas como ella!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era la luna 🌕")

#--- Pregunta 12 ---
print(f"\n¡Vamos con la pregunta 12!")
respuesta_12 = input("¿Qué estrella le da calor y luz a nuestro sistema solar?\n")
if respuesta_12.lower() == "sol":
    print(f"☑️ ¡Muy bien, respuesta brillante!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Incorrecto!, la respuesta correcta era el sol ☀️")

#--- Pregunta 13 ---
print(f"\n¡Vamos con la pregunta 13!")
respuesta_13 = input("¿Qué ave es el símbolo natural de la región andina?\n")
if respuesta_13.lower() == "cóndor" or respuesta_13.lower() == "condor":
    print(f"☑️ ¡Excelente, volaste alto!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el cóndor 🦅")

#--- Pregunta 14 ---
print(f"\n¡Vamos con la pregunta 14!")
respuesta_14 = input("¿Qué recurso natural vital para la vida no tiene color, olor ni sabor?\n")
if respuesta_14.lower() == "agua":
    print(f"☑️ ¡Muy bien, respuesta fresca!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta correcta era el agua 💧")

#--- Pregunta 15 ---
print(f"\n¡Vamos con la pregunta 15!")
respuesta_15 = input("¿Qué tipo de planta crece en el desierto y tiene espinas?\n")
if respuesta_15.lower() == "cactus":
    print(f"☑️ ¡Bien hecho, no te pinchaste!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el cactus 🌵")

#--- Pregunta 16 ---
print(f"\n¡Vamos con la pregunta 16!")
respuesta_16 = input("¿Qué gas respiramos los seres humanos para poder vivir?\n")
if respuesta_16.lower() == "oxígeno" or respuesta_16.lower() == "oxigeno":
    print(f"☑️ ¡Excelente, respuesta vital!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Incorrecto!, respiramos oxígeno 💨")

#--- Pregunta 17 ---
print(f"\n¡Vamos con la pregunta 17!")
respuesta_17 = input("¿Cuál es el mamífero terrestre más grande del mundo?\n")
if respuesta_17.lower() == "elefante":
    print(f"☑️ ¡Enorme! Respuesta correcta.")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el elefante 🐘")

#--- Pregunta 18 ---
print(f"\n¡Vamos con la pregunta 18!")
respuesta_18 = input("¿Cómo se le llama al bosque tropical más grande del mundo?\n")
if respuesta_18.lower() == "amazonas" or respuesta_18.lower() == "selva amazónica":
    print(f"☑️ ¡Perfecto, conoces bien el planeta!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el amazonas 🌳")

#--- Pregunta 19 ---
print(f"\n¡Vamos con la pregunta 19!")
respuesta_19 = input("¿Qué animal marino tiene ocho brazos y tres corazones?\n")
if respuesta_19.lower() == "pulpo":
    print(f"☑️ ¡Increíble, respuesta correcta!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el pulpo 🐙")

#--- Pregunta 20 ---
print(f"\n¡Vamos con la pregunta 20!")
respuesta_20 = input("¿Qué fenómeno natural produce un arco de colores en el cielo cuando llueve y sale el sol?\n")
if respuesta_20.lower() == "arcoíris" or respuesta_20.lower() == "arcoiris":
    print(f"☑️ ¡Muy bien, llenaste de color el examen!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el arcoíris 🌈")

#--- Pregunta 21 ---
print(f"\n¡Vamos con la pregunta 21!")
respuesta_21 = input("¿Qué animal es el pariente vivo más cercano de los dinosaurios?\n")
if respuesta_21.lower() == "ave" or respuesta_21.lower() == "aves" or respuesta_21.lower() == "pájaro":
    print(f"☑️ ¡Genial, un dato muy curioso!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, las aves son sus parientes más cercanos 🐔")

#--- Pregunta 22 ---
print(f"\n¡Vamos con la pregunta 22!")
respuesta_22 = input("¿Qué estación del año es la más fría?\n")
if respuesta_22.lower() == "invierno":
    print(f"☑️ ¡Correcto, una respuesta congelante!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el invierno ❄️")

#--- Pregunta 23 ---
print(f"\n¡Vamos con la pregunta 23!")
respuesta_23 = input("¿Cuál es el desierto más grande y caluroso más grande del planeta?\n")
if respuesta_23.lower() == "sahara" or respuesta_23.lower() == "el sahara" :
    print(f"☑️ ¡Excelente, una respuesta muy ardiente!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta correcta es el sahara 🏜️")
  
#--- Pregunta 24 ---
print(f"\n¡Vamos con la pregunta 24!")
respuesta_24 = input("¿Qué animal lento y con caparazón puede vivir más de 100 años?\n")
if respuesta_24.lower() == "tortuga" or respuesta_24.lower() == "tortuga marina":
    print(f"☑️ ¡Lento pero seguro, correcto!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era la tortuga 🐢")

#--- Pregunta 25 ---
print(f"\n¡Vamos con la pregunta 25!")
respuesta_25 = input("¿Qué sustancia caliente y líquida expulsa un volcán cuando entra en erupción?\n")
if respuesta_25.lower() == "lava" or respuesta_25.lower() == "magma":
    print(f"☑️ ¡Fuego puro, muy bien!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era lava 🌋")

#--- Pregunta 26 ---
print(f"\n¡Vamos con la pregunta 26!")
respuesta_26 = input("¿Qué animal es capaz de cambiar el color de su piel para camuflarse?\n")
if respuesta_26.lower() == "camaleón" or respuesta_26.lower() == "camaleon":
    print(f"☑️ ¡Eso es, te adaptas rápido!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, era el camaleón 🦎")

#--- Pregunta 27 ---
print(f"\n¡Vamos con la pregunta 27!")
respuesta_27 = input("¿Cuál es el continente más frío y cubierto de hielo del planeta?\n")
if respuesta_27.lower() == "antártida" or respuesta_27.lower() == "antartida":
    print(f"☑️ ¡Perfecto, directo al polo sur!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era la Antártida 🏔️")

#--- Pregunta 28 ---
print(f"\n¡Vamos con la pregunta 28!")
respuesta_28 = input("¿Cómo se llama el desierto más seco del mundo, ubicado en Sudamérica?\n")
if respuesta_28.lower() == "atacama" or respuesta_28.lower() == "desierto de atacama":
    print(f"☑️ ¡Espectacular, buena memoria geográfica!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era Atacama 🏜️")

#--- Pregunta 29 ---
print(f"\n¡Vamos con la pregunta 29!")
respuesta_29 = input("¿Qué animal marino es conocido por ser un mamífero muy inteligente y juguetón?\n")
if respuesta_29.lower() == "delfín" or respuesta_29.lower() == "delfin":
    print(f"☑️ ¡Excelente, nadaste directo al éxito!")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste!, la respuesta era el delfín 🐬")

#--- Pregunta 30 ---
print(f"\n¡Última pregunta por la puntuación perfecta!")
respuesta_30 = input("¿Cómo se llama el proceso por el cual las plantas fabrican su propio alimento usando la luz solar?\n")
if respuesta_30.lower() == "fotosíntesis" or respuesta_30.lower() == "fotosintesis":
    print(f"☑️ ¡Magnífico!, terminaste el examen de forma perfecta.")
    puntos = puntos + 33.33
else:
    print(f"✖️ ¡Fallaste en la última!, la respuesta era la fotosíntesis 🌿")

#---Resultado Final---
print(f"\n=====================================")
print(f"📝 ¡Examen terminado!")
# Usamos int(round(puntos)) para que el puntaje final se muestre como un número entero limpio (1000)
print(f"Tu calificación final es: {int(round(puntos))} / 1000 puntos")
print(f"=====================================")

