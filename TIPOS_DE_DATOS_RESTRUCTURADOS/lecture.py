#  lista=["abel","anthony","miguel"]
#  diccionario={"nombre":"antonio", "edad":15 "sexo":False}
#  print(diccionario["nombre"])

#  texto="hola"
#  lista_texto=list(texto)
#  lista2=[e for e in texto]

#  # ejemplos con split
#  texto_largo="hola como estan bienvenidos al salon"
#  nueva_lista=list(texto_largo)
#  print(nueva_lista)

#  texto_largo="hola como estan bienvenidos al salon"
#  nueva_lista=texto_largo.split(" ")
#  print(nueva_lista)

#  texto_largo="hola como estan bienvenidos al salon"
#  nuevo_texto=texto_largo[16:]
#  nueva_lista=nuevo_texto.split(" ")
#  print(nueva_lista)


#  texto_largo="loquitas_.mp4"
#  nuevo_texto=texto_largo.split(".")
#  print(nuevo_texto [-1])

#  texto_largo="este es un texto largo chiquitas y chiquitos"
#  nuevo_texto=texto_largo.split(" ")
#  print(" ".join(nuevo_texto))
#  alumnos = [
#     {"nombre": "Antoni", 
#      "apellido": "Gomez", "edad": 25},
#     {"nombre": "Abel",
#      "apellido": "Perez", "edad": 23},
#     {"nombre": "Ruth", 
#      "apellido":
#        "Martinez", "edad": 22},
#     {"nombre": "Lizbeth", 
#      "apellido": "Garcia", "edad": 24},
#     {"nombre": "Luz", 
#      "apellido": "Lopez", "edad": 21}
# ]

#  alumnos.append({"nombre": "Antoni", "apellido": "gomezs", "edad": 26})

#  alumnos = [alumno for alumno in alumnos if alumno["nombre"] != "Abel"]

#  posicion_alumno_4 = None
# for i, alumno in enumerate(alumnos):
#     if i == 3:  
#         posicion_alumno_4 = i
#         break

# print("Lista de alumnos actualizada:")
# for alumno in alumnos:
#     print(alumno)

# print("La posición del alumno 4 en la lista es:", posicion_alumno_4)













# # crear un programa que reciba una lista desordenada y muestre por terminal la lista ordenada y la lista previa a ser ordenada.
# lista=[4,76,1,3,6,8,2]
# copia_lista=lista.copy()
# copia_lista.sort()
# print(lista)
# print(copia_lista)



# # crear una lista de numeros enteros del siguente texto 
# texto="1,4,8,9,6"
# convertir=texto.split(",")
# print(convertir)


# # crear una lista de numeros enteros del siguente texto 
# texto="1,4,8,9,6"
# nueva_lista=[]
# for n in texto.split(","):
#    nueva_lista.append(n)
#    print(nueva_lista)
#    #aplivcando la tecnica vlc valor bucle y condicion 
#    texto="1,4,8,9,6"
#    nueva_lista=[n for n in texto.split(",") if int(n)%2==0]
#    print(nueva_lista)
# # diccionarios por comprencion.
# lista_amigos=["abel","anthony","edith","ruth"]
# diccionario={}
# for _,v in enumerate(lista_amigos):
#     diccionario[v]=len(v)
# print(diccionario)
# #aplicando el vlc
# lista_amigos=["abel","anthony","edith","ruth"]
# diccionario={amigo:len(amigo) for amigo in lista_amigos}
# print(diccionario)