import time
import os
import random
from os import system
class fg:
  BLACK='\033[30m'
  RED='\033[31m'
  GREEN='\033[32m'
  ORANGE='\033[33m'
  BLUE='\033[34m'
  PURPLE='\033[35m'
  CYAN='\033[36m'
  LIGHTGREY='\033[37m'
  DARKGREY='\033[90m'
  LIGHTRED='\033[91m'
  LIGHTGREEN='\033[92m'
  YELLOW='\033[93m'
  LIGHTBLUE='\033[94m'
  PINK='\033[95m'
  LIGHTCYAN='\033[96m'
  RESET = '\033[39m'
iniciar_trivia=True
print(fg.YELLOW+"------------Bienvenido a la TRIVIAfcesar!------------"+fg.RESET)
puntaje = 0 
puntaje = random.randint(50,150)
while iniciar_trivia==True:
  nick=input("Ingrese su nombre: ")
  while nick=="":
    print("Por favor ingresar su nombre: ")
    nick=input("Ingrese su nombre: ")
  for i in range(1,5):
    print("_______")
    time.sleep(0.1)
  print(fg.GREEN+"Bienvenido ",fg.CYAN+nick,fg.GREEN+" vamos a comenzar con el juego eligiendo el modo que deseas probarlo."+fg.RESET)
  time.sleep(0.3)
  print(fg.DARKGREY+"-------------------Elegir entre las opciones-----------------"+fg.RESET)
  print(fg.DARKGREY+"Puedes elegir entre: \n(a)Supervivencia\n(b)Normal"+fg.RESET)
  print(fg.DARKGREY+"-------------------------------------------------------------"+fg.RESET)
  eleccion = input("Elegir modo: ")
  
  if (eleccion.lower() == "a"):
      time.sleep(0.5)
      print(fg.DARKGREY+"---------------------Leer Reglas-------------------------"+fg.RESET)
      print(
          fg.DARKGREY+"Al elegir modo sobreviviente tendrás un total de 10 vidas\nlas preguntas seran variadas entre cultura general o preguntas bien random :v\nAl terminar no podra responder más preguntas"+fg.RESET
      )
      print(fg.DARKGREY+"-------------------------------------------------------------\n"+fg.RESET)
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
              print(fg.LIGHTGREEN+"Respuesta Correcta\nVez que si podias"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count, "\n")
              score += 1
              break
          else:
              count -= 1
              print(fg.LIGHTRED+
                  "Incorrecto, vuelva a intentarlo\nNo hagas llorar a tus profesores >:v"+fg.RESET
              )
              print(fg.ORANGE+"Vidas: "+fg.RESET, count)
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
                  fg.LIGHTGREEN+"Respuesta Correcta\nTu profesor de Historia estaria orgulloso."+fg.RESET
              )
              print(fg.ORANGE+"Vidas: "+fg.RESET, count, "\n")
              score += 1
              break
          else:
              count -= 1
              print(fg.LIGHTRED+"Incorrecto, vuelva a intentarlo\nNo jales en trivias"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count)
      time.sleep(0.9)
      pregunta3 = print(
          "3)¿Cuál es la bebida declarada Patrimonio Cultural de la Nación en 2007\n(a)Chilcano\n(b)Pisco Sour\n(c)Piña Colada\n(d)Sangría"
      )
      respuesta3 = "b"
      time.sleep(0.2)
      for i in range(count):
          respuesta = input("\nRespuesta: ")
  
          if respuesta.lower() == respuesta3 and count > 0:
              print(fg.LIGHTGREEN+"Respuesta Correcta, recuerda no manejar asi"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count, "\n")
              score += 1
              break
          else:
              count -= 1
              print(fg.LIGHTRED+"Incorrecto, vuelva a intentarlo\nSe que lo sabes no lo ocultes"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count)
      time.sleep(0.9)
      pregunta4 = print(
          "4)¿Qué cantante no es peruano?\n(a)Gian Marco\n(b)Pedro Suárez Vertiz\n(c)Jesús Navarro\n(d)Jorge Villamizar Ireguis"
      )
      respuesta4 = "d"
      time.sleep(0.2)
      for i in range(count):
          respuesta = input("\nRespuesta: ")
  
          if respuesta.lower() == respuesta4 and count > 0:
              print(fg.LIGHTGREEN+"Respuesta Correcta gran conocedor"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count, "\n")
              score += 1
              break
          else:
              count -= 1
              print(fg.LIGHTRED+"Incorrecto, vuelva a intentarlo\nTe ayudo no es la f"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count)
      time.sleep(0.9)
      pregunta5 = print(
          "5)¿Con qué pelicula Leonardo DiCaprio ganó el oscar?\n(a)Titanic\n(b)El Origen\n(c)Atrápame si puedes\n(d)El renacido"
      )
      respuesta5 = "d"
      time.sleep(0.2)
      for i in range(count):
          respuesta = input("\nRespuesta: ")
  
          if respuesta.lower() == respuesta5 and count > 0:
              print(fg.LIGHTGREEN+"Respuesta Correcta"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count, "\n")
              score += 1
              break
          else:
              count -= 1
              print(fg.LIGHTRED+"Incorrecto, vuelva a intentarlo\nAcuerdate de los memes"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count)
      time.sleep(0.9)
      pregunta6 = print(
          "6)¿El nucleo de un átomo se compone de protones y\nque otra particula?\n(a)Electrones\n(b)Bosones\n(c)Neutrones\n(d)Fotones"
      )
      respuesta6 = "c"
      time.sleep(0.2)
      for i in range(count):
          respuesta = input("\nRespuesta: ")
  
          if respuesta.lower() == respuesta6 and count > 0:
              print(fg.LIGHTGREEN+"Respuesta Correcta"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count, "\n")
              score += 1
              break
          else:
              count -= 1
              print(fg.LIGHTRED+"Incorrecto, vuelva a intentarlo"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count)
      time.sleep(0.9)
      pregunta7 = print(
          "7)¿De qué pais es originaria la firma Maserati\n(a)Suiza\n(b)Italia\n(c)EE-UU\n(d)Rusia"
      )
      respuesta7 = "b"
      time.sleep(0.2)
      for i in range(count):
          respuesta = input("\nRespuesta: ")
  
          if respuesta.lower() == respuesta7 and count > 0:
              print(fg.LIGHTGREEN+"Respuesta Correcta"+fg.RESET)
              print(fg.ORANGE+"Vidas: "+fg.RESET, count, "\n")
              score += 1
              break
          else:
              count -= 1
              print(
                  fg.LIGHTRED+"Incorrecto, vuelva a intentarlo\nAun te quedan intentos, champea xd"+fg.RESET
              )
              print("Vidas: ", count)
      time.sleep(0.9)
  
      while count > 0:
          print("Bien hecho completaste la Trivia!")
          break
          exit
      while count == 0:
          print(fg.RED+
              "Ya has utilizado todos tus contadores y no puedes seguir respondiendo, has perdido\nLa cantidad de preguntas que has respondido fue:"+fg.RESET,
              score)
          break
          exit
 

  # MODO NORMAL
  if (eleccion.lower() == "b"):
      time.sleep(0.5)
      chances = 1
      print(fg.DARKGREY+"-------------------------Leer Reglas-------------------------"+fg.RESET)
      print(
          fg.DARKGREY+"Al elegir modo normal tendrás un chance de elegir la respuesta correcta\nComenzaras con un puntaje dado:\nCada respuesta correcta el puntaje aumentará\nCada respuesta erronea el puntaje disminuirá\nAl final de a trivia se le dará su puntuación final\nLas preguntas seran de conocimiento general"+fg.RESET
      )
      print(fg.DARKGREY+"-------------------------------------------------------------"+fg.RESET)
      time.sleep(4)

      score2 = 0
      print(fg.CYAN+"Tu puntaje incial será de: "+fg.RESET,puntaje)
      pregunta11 = print(
          "1)¿Qué es la gangrena\n(a)Demencia\n(b)Necrosis\n(c)Reuma\n(d)Caida del cabello"
      )
      respuesta11 = "b"
      time.sleep(0.2)
      for i in range(chances):
          respuesta = input("\nRespuesta: ")
  
          if respuesta.lower() == respuesta11:
              print(fg.LIGHTGREEN+"Respuesta Correcta"+fg.RESET)
              puntaje += random.randint(10,50)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.\n")
              score2 += 1
              break
          else:
              print(fg.LIGHTRED+"Incorrecto\n"+fg.RESET)
              puntaje -= random.randint(10,20)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.")
              time.sleep(0.2)
              print(fg.ORANGE+"La respuesta correcta es: "+fg.RESET, respuesta11, "\n")
      time.sleep(0.9)
      pregunta22 = print(
          "2)¿Quién fue el primer presidente de la República del Perú?\n(a)José Bernando de Tagle\n(b)José de la Mar\n(c)José de la Riva Agüero\n(d)Agustin Gamarra\n"
      )
      respuesta22 = "c"
      time.sleep(0.2)
      for i in range(chances):
          respuesta = input("Respuesta: ")
  
          if respuesta.lower() == respuesta22:
              print(fg.LIGHTGREEN+"Respuesta Correcta\n"+fg.RESET)
              puntaje += random.randint(10,50)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.\n")
              score2 += 1
              break
          else:
              print(fg.LIGHTRED+"Incorrecto\n"+fg.RESET)
              puntaje -= random.randint(10,20)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.")
              time.sleep(0.2)
              print(fg.ORANGE+"La respuesta correcta es: "+fg.RESET,       respuesta22,"\n")
      time.sleep(0.9)
      pregunta3 = print(
          "3)¿Cuál es la montaña más alta del Perú?\n(a)Yerupajá\n(b)Huascarán\n(c)Coropuna\n(d)Huandoy\n"
      )
      respuesta33 = "b"
      time.sleep(0.2)
      for i in range(chances):
          respuesta = input("Respuesta: ")
  
          if respuesta.lower() == respuesta33:
              print(fg.LIGHTGREEN+"Respuesta Correcta\n"+fg.RESET)
              puntaje += random.randint(10,50)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.\n")
              score2 += 1
              break
          else:
              print(fg.LIGHTRED+"Incorrecto\n"+fg.RESET)
              puntaje -= random.randint(10,20)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.")
              time.sleep(0.2)
              print(fg.ORANGE+"La respuesta correcta es: "+fg.RESET,       respuesta33, "\n")
      time.sleep(0.9)
      pregunta4 = print(
          "4)¿Cuál es el elemento magnético más común en el planeta?\n(a)Plata\n(b)Plomo\n(c)Niquel\n(d)Hierro\n"
      )
      respuesta44 = "d"
      time.sleep(0.2)
      for i in range(chances):
          respuesta = input("Respuesta: ")
  
          if respuesta.lower() == respuesta44:
              print(fg.LIGHTGREEN+"Respuesta Correcta\n"+fg.RESET)
              puntaje += random.randint(10,50)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.\n")
              score2 += 1
              break
          else:
              print(fg.LIGHTRED+"Incorrecto\n"+fg.RESET)
              puntaje -= random.randint(10,20)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.")
              time.sleep(0.2)
              print(fg.ORANGE+"La respuesta correcta es: "+fg.RESET,       respuesta44, "\n")
      time.sleep(0.9)
      pregunta5 = print(
          "5)¿En qué momento un dia recibe la mayor o menor cantidad de luz solar del año?\n(a)Solsix\n(b)Soleum\n(c)Solsticio\n(d)Equinoccio\n"
      )
      respuesta55 = "c"
      time.sleep(0.2)
      for i in range(chances):
          respuesta = input("Respuesta: ")
  
          if respuesta.lower() == respuesta55:
              print(fg.LIGHTGREEN+"Respuesta Correcta\n"+fg.RESET)
              puntaje += random.randint(10,50)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.\n")
              score2 += 1
              break
          else:
              print(fg.LIGHTRED+"Incorrecto\n"+fg.RESET)
              puntaje -= random.randint(10,20)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.")
              time.sleep(0.2)
              print(fg.ORANGE+"La respuesta correcta es: "+fg.RESET,       respuesta55, "\n")
      time.sleep(0.9)
      pregunta6 = print(
          "6)¿En qué batalla murió el presidente peruano Agustin Gammarra en 1841?\n(a)Batalla de Ingavi\n(b)Batalla de la Apacheta\n(c)Batalla de Ayacucho\n(d)Batalla de Nasca\n"
      )
      respuesta66 = "a"
      time.sleep(0.2)
      for i in range(chances):
          respuesta = input("Respuesta: ")
  
          if respuesta.lower() == respuesta66:
              print(fg.LIGHTGREEN+"Respuesta Correcta\n"+fg.RESET)
              puntaje += random.randint(10,50)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.\n")
              score2 += 1
              break
          else:
              print(fg.LIGHTRED+"Incorrecto\n"+fg.RESET)
              puntaje -= random.randint(10,20)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.")
              time.sleep(0.2)
              print(fg.ORANGE+"La respuesta correcta es: "+fg.RESET,       respuesta66, "\n")
      time.sleep(0.9)
      pregunta7 = print(
          "7)¿Qué parte del ojo es transparentable?\n(a)Disco óptico\n(b)Retina\n(c)Cornea\n(d)Nervio óptico\n"
      )
      respuesta77 = "c"
      time.sleep(0.2)
      for i in range(chances):
          respuesta = input("Respuesta: ")
  
          if respuesta.lower() == respuesta77:
              print(fg.LIGHTGREEN+"Respuesta Correcta\n"+fg.RESET)
              puntaje += random.randint(10,50)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.\n")
              score2 += 1
              break
          else:
              print(fg.LIGHTRED+"Incorrecto\n"+fg.RESET)
              puntaje -= random.randint(10,20)
              print("Tienes: "+fg.ORANGE,puntaje,fg.RESET+" Puntos.")
              time.sleep(0.2)
              print(fg.ORANGE+"La respuesta correcta es: "+fg.RESET,       respuesta77, "\n")
      time.sleep(0.3)
  
      while score2 >= 4:
          print("Bien hecho has respondido", score2," correctas")
          print("Tu puntaje final es de: ",puntaje)
          break
          exit

      while score2 <= 3:
  
          print(fg.YELLOW+"Buena suerte a la proxima, has acertado:  "+fg.RESET, score2)
          print(fg.YELLOW+"Tu puntaje final es de: "+fg.RESET,puntaje)
          break
          exit
  
          
  for i in range(5):
    print("______")
    time.sleep(0.2)
  print(fg.CYAN+"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+fg.RESET).lower()
  
  if repetir_trivia != "si":  
    print(f'\nEspero que lo hayas pasado bien {nick}, hasta pronto!')
    iniciar_trivia = False  


