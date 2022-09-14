import time
import os
from os import system

print("Bienvenido a la TRIVIAfcesar!")
time.sleep(1)
print("-------------------Elegir entre las opciones-----------------")
print("Puedes elegir entre: \n(a)Supervivencia\n(b)Normal")
print("---------------------------------------------------------")
eleccion = input("Elegir modo: ")
if (eleccion.lower() == "a"):
    time.sleep(0.5)
    print("---------------------Leer Reglas-------------------------")
    print(
        "Al elegir modo sobreviviente tendrás un total de 10 vidas\nAl terminar sus vidas se cerrará el juego\nlas preguntas seran variadas entre cultura general o preguntas bien random"
    )
    print("-------------------------------------------------------------\n")
    time.sleep(4)
    count = 10
    score = 0
    pregunta1 = print(
        "1)¿Cuál es la provincia donde se encuentra el Santuario\nHistórico de Machu Picchu?\n(a)Urubamba\n(b)Calca\n(c)Acomayo\n(d)Canas"
    )
    respuesta1 = "a"
    time.sleep(0.2)
    for i in range(count):
        respuesta = input("\nRespuesta: ")
        if respuesta.lower() == respuesta1 and count > 0:
            print("Respuesta Correcta\nVez que si podias")
            print("Vidas: ", count, "\n")
            score += 1
            break
        else:
            count -= 1
            print(
                "Incorrecto, vuelva a intentarlo\nNo hagas llorar a tus profesores >:v"
            )
            print("Vidas: ", count)
    time.sleep(0.9)
    pregunta2 = print(
        "2)¿Quién fue el primer Virrey del Perú?\n(a)Andrés Hurtado de Mendoza\n(b)Blasco Nuñez de Vela\n(c)Diego López de Zuñiga y Velasco\n(d)Martín Enriquez de Almansa"
    )
    respuesta2 = "b"
    time.sleep(0.2)
    for i in range(count):
        respuesta = input("\nRespuesta: ")

        if respuesta.lower() == respuesta2 and count > 0:
            print(
                "Respuesta Correcta\nTu profesor de Historia estaria orgulloso."
            )
            print("Vidas: ", count, "\n")
            score += 1
            break
        else:
            count -= 1
            print("Incorrecto, vuelva a intentarlo\nNo jales en trivias")
            print("Vidas: ", count)
    time.sleep(0.9)
    pregunta3 = print(
        "3)¿Cuál es la bebida declarada Patrimonio Cultural de la Nación en 2007\n(a)Chilcano\n(b)Pisco Sour\n(c)Piña Colada\n(d)Sangría"
    )
    respuesta3 = "b"
    time.sleep(0.2)
    for i in range(count):
        respuesta = input("\nRespuesta: ")

        if respuesta.lower() == respuesta3 and count > 0:
            print("Respuesta Correcta")
            print("Vidas: ", count, "\n")
            score += 1
            break
        else:
            count -= 1
            print(
                "Incorrecto, vuelva a intentarlo\nSe que lo sabes no lo ocultes"
            )
            print("Vidas: ", count)
    time.sleep(0.9)
    pregunta4 = print(
        "4)¿Qué cantante no es peruano?\n(a)Gian Marco\n(b)Pedro Suárez Vertiz\n(c)Chabuca Granda\n(d)Jorge Villamizar Ireguis"
    )
    respuesta4 = "d"
    time.sleep(0.2)
    for i in range(count):
        respuesta = input("\nRespuesta: ")

        if respuesta.lower() == respuesta4 and count > 0:
            print("Respuesta Correcta")
            print("Vidas: ", count, "\n")
            score += 1
            break
        else:
            count -= 1
            print("Incorrecto, vuelva a intentarlo\nTe ayudo no es la f")
            print("Vidas: ", count)
    time.sleep(0.9)
    pregunta5 = print(
        "5)¿Con qué pelicula Leonardo DiCaprio ganó el oscar?\n(a)Titanic\n(b)El Origen\n(c)Atrápame si puedes\n(d)El renacido"
    )
    respuesta5 = "d"
    time.sleep(0.2)
    for i in range(count):
        respuesta = input("\nRespuesta: ")

        if respuesta.lower() == respuesta5 and count > 0:
            print("Respuesta Correcta")
            print("Vidas: ", count, "\n")
            score += 1
            break
        else:
            count -= 1
            print("Incorrecto, vuelva a intentarlo\nAcuerdate de los memes")
            print("Vidas: ", count)
    time.sleep(0.9)
    pregunta6 = print(
        "6)¿El nucleo de un átomo se compone de protones y\nque otra particula?\n(a)Electrones\n(b)Bosones\n(c)Neutrones\n(d)Fotones"
    )
    respuesta6 = "c"
    time.sleep(0.2)
    for i in range(count):
        respuesta = input("\nRespuesta: ")

        if respuesta.lower() == respuesta6 and count > 0:
            print("Respuesta Correcta")
            print("Vidas: ", count, "\n")
            score += 1
            break
        else:
            count -= 1
            print("Incorrecto, vuelva a intentarlo")
            print("Vidas: ", count)
    time.sleep(0.9)
    pregunta7 = print(
        "7)¿De qué pais es originaria la firma Maserati\n(a)Suiza\n(b)Italia\n(c)EE-UU\n(d)Rusia"
    )
    respuesta7 = "b"
    time.sleep(0.2)
    for i in range(count):
        respuesta = input("\nRespuesta: ")

        if respuesta.lower() == respuesta7 and count > 0:
            print("Respuesta Correcta")
            print("Vidas: ", count, "\n")
            score += 1
            break
        else:
            count -= 1
            print(
                "Incorrecto, vuelva a intentarlo\nAun te quedan intentos, champea xd"
            )
            print("Vidas: ", count)
    time.sleep(0.9)

    while count > 0:
        print("Bien hecho completaste la Trivia!")
        break
        exit
    while count == 0:
        print(
            "Ya has utilizado todos tus contadores y no puedes seguir respondiendo, has perdido\nLa cantidad de preguntas que has respondido fue:",
            score)
        time.sleep(3)
        os.system("clear")
        exit

# MODO NORMAL

if (eleccion.lower() == "b"):
    time.sleep(0.5)
    chances = 1
    print("-------------------------Leer Reglas-------------------------")
    print(
        "Al elegir modo normal tendrás un chance de elegir la respuesta correcta\nAl final de a trivia se le dará su puntuación\nlas preguntas seran de conocimiento general"
    )
    print("-------------------------------------------------------------")
    time.sleep(4)
    score2 = 0
    pregunta11 = print(
        "1)¿Qué es la gangrena\n(a)Demencia\n(b)Necrosis\n(c)Reuma\n(d)Caida del cabello"
    )
    respuesta11 = "b"
    time.sleep(0.2)
    for i in range(chances):
        respuesta = input("\nRespuesta: ")

        if respuesta.lower() == respuesta11:
            print("Respuesta Correcta\n")
            score2 += 1
            break
        else:
            print("Incorrecto\n")
            time.sleep(0.2)
            print("La respuesta correcta es: ", respuesta11, "\n")
    time.sleep(0.9)
    pregunta22 = print(
        "2)¿Quién fue el primer presidente de la República del Perú?\n(a)José Bernando de Tagle\n(b)José de la Mar\n(c)José de la Riva Agüero\n(d)Agustin Gamarra\n"
    )
    respuesta22 = "c"
    time.sleep(0.2)
    for i in range(chances):
        respuesta = input("Respuesta: ")

        if respuesta.lower() == respuesta22:
            print("Respuesta Correcta\n")
            score2 += 1
            break
        else:
            print("Incorrecto\n")
            time.sleep(0.2)
            print("La respuesta correcta es: ", respuesta22, "\n")
    time.sleep(0.9)
    pregunta3 = print(
        "3)¿Cuál es la montaña más alta del Perú?\n(a)Yerupajá\n(b)Huascarán\n(c)Coropuna\n(d)Huandoy\n"
    )
    respuesta33 = "b"
    time.sleep(0.2)
    for i in range(chances):
        respuesta = input("Respuesta: ")

        if respuesta.lower() == respuesta33:
            print("Respuesta Correcta\n")
            score2 += 1
            break
        else:
            print("Incorrecto\n")
            time.sleep(0.2)
            print("La respuesta correcta es: ", respuesta33, "\n")
    time.sleep(0.9)
    pregunta4 = print(
        "4)¿Cuál es el elemento magnético más común en el planeta?\n(a)Plata\n(b)Plomo\n(c)Niquel\n(d)Hierro\n"
    )
    respuesta44 = "d"
    time.sleep(0.2)
    for i in range(chances):
        respuesta = input("Respuesta: ")

        if respuesta.lower() == respuesta44:
            print("Respuesta Correcta\n")
            score2 += 1
            break
        else:
            print("Incorrecto\n")
            time.sleep(0.2)
            print("La respuesta correcta es: ", respuesta44, "\n")
    time.sleep(0.9)
    pregunta5 = print(
        "5)¿En qué momento un dia recibe la mayor o menor cantidad de luz solar del año?\n(a)Solsix\n(b)Soleum\n(c)Solsticio\n(d)Equinoccio\n"
    )
    respuesta55 = "c"
    time.sleep(0.2)
    for i in range(chances):
        respuesta = input("Respuesta: ")

        if respuesta.lower() == respuesta55:
            print("Respuesta Correcta\n")
            score2 += 1
            break
        else:
            print("Incorrecto\n")
            time.sleep(0.2)
            print("La respuesta correcta es: ", respuesta55, "\n")
    time.sleep(0.9)
    pregunta6 = print(
        "6)¿En qué batalla murió el presidente peruano Agustin Gammarra en 1841?\n(a)Batalla de Ingavi\n(b)Batalla de la Apacheta\n(c)Batalla de Ayacucho\n(d)Batalla de Nasca\n"
    )
    respuesta66 = "a"
    time.sleep(0.2)
    for i in range(chances):
        respuesta = input("Respuesta: ")

        if respuesta.lower() == respuesta66:
            print("Respuesta Correcta\n")
            score2 += 1
            break
        else:
            print("Incorrecto\n")
            time.sleep(0.2)
            print("La respuesta correcta es: ", respuesta66, "\n")
    time.sleep(0.9)
    pregunta7 = print(
        "7)¿Qué parte del ojo es transparentable?\n(a)Disco óptico\n(b)Retina\n(c)Cornea\n(d)Nervio óptico\n"
    )
    respuesta77 = "c"
    time.sleep(0.2)
    for i in range(chances):
        respuesta = input("Respuesta: ")

        if respuesta.lower() == respuesta77:
            print("Respuesta Correcta\n")
            score2 += 1
            break
        else:
            print("Incorrecto\n")
            time.sleep(0.2)
            print("La respuesta correcta es: ", respuesta77, "\n")
    time.sleep(0.3)

    while score2 >= 4:
        print("Bien hecho has respondido", score2)
        os.system("clear")
        break
    while score2 <= 3:

        print("Buena suerte a la proxima tu puntuación fue:  ", score2)
        time.sleep(3)
        os.system("clear")
        break

elif eleccion != 'a' or eleccion != 'b':
    print("Eleccion incorrecta, vuelva a intentar el juego")
    time.sleep(2)
    os.system("clear")
    exit
