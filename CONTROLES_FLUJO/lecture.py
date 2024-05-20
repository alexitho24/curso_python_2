#  almacenar el if en un variable 
# ``` python  -->
# primer ejemplo if estructurado
# edad:int=int(input("escribe tu edad:"))
# if edad>=18:
#     print("eres mayor")
# else:
#     print("eres menor de edad")
# segundo ejemplo if almacenado en variable
# edad:int=int(input("escribe tu edad: "))
# respuesta:str="eres mayor" if edad>=18 else "eres menor" 
# print(respuesta)


# for n in range(1,11):
#     print(n)



# vocales= str="aeiou"
# for n in range(0,5):
#     print(vocales[n])
#crear un programa que me muestre los 8 primeros numeros pares
# for n in range(1, 17):
#     if n % 2 == 0:
#      print(n)

#      crear un programa que me pida al usuario escribir una oracion y mostrar por terminal la cantidad de vocales a que tiene esa oracion 
# OJO SOLO LA "a" MINUSCULA

# oracion = input("Escribe una oración: ")
# contador = 0

# for letra in oracion:
#     if letra == 'a':
#         contador += 1

# print(contador)
# oracion = input("Escribe una oración: ")
# contador = 0
# for n in range(0,len(oracion)):
#     if oracion [n]== 'a':
#         contador=contador+1
    
# #         #contador += 1

# # print(f"la cantidad de letras a que tengo es {contador}
# # sentence = input("Escribe una oración: ")
# # count = 0
# # for i in range(len(sentence)):
# #     if sentence[i] == ',':
# #         count +=1
# # print(count),

# # clase hoy 15/05/2024
# # oracion:str=input("ingrese una oriacion: ")
# # contador=0
# # for indice,letra in enumerate(oracion):
# #     if letra == ",":
# #      print(f"su indice es {indice}")
# #     contador=1
# # print(f"la cantidad de comas es {contador}")


# #  escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
# # (desde 1 hasta su edad)
# # edad = int(input("Por favor, ingresa tu edad: "))

# # for n in range(1, edad+1):
# #     print("Has cumplido",n, "años")

# # crear un programa que me pida el nombre de tres personas y guarde en una variable global
# # la ultima letra de sus nombres 
# # mostrar por pantalla la variable global con las tres ultimas letras del nombre de cada persona 

# # ejemplo:
# # abel
# # antony
# # edith
# # salida lyh

# # ultimas_letras = ""

# # for n in range(3):
# #     nombre = input("Ingresa el nombre de una persona: ")
# #     ultimas_letras += nombre[-1] 
# # print("Las últimas letras de los nombres son:", ultimas_letras)


# # ejemplo del profe 

# # ultima_letra:str=""
# # for _ in range(3)
# # nombre:str=input("escribe tu nombre:")
# # last_latter:str=nombre[-1]
# # print(ultima_letra)

# # crear un programa que muestre por terminal la siguiente figura:
# # a
# # ee 
# # iii 
# # oooo
# # uuuuu
# # Definir las vocales en el orden deseado

# # print("a")
# # print("ee")
# # print("iii")
# # print("oooo")
# # print("uuuuu")
# # crear un programa que pida un numero y que muestre la tabla de multiplicas de ese numero


# condicion=True
# while condicion:
#     eval=input("desea continuar [S/N]")
#     if eval=="S":
#     print("continuas en bucle")
#     continue
# else:
#     print("se termino el programa")
#     condicion=False
#     break


# crear un programa que pida la xcantidad de notas que se debe registrar
# luego pidira las notas e imprima el promedio con while

cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: "))
notas = []
total = 0
contador = 0
while contador < cantidad_notas:
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)
    total += nota
    contador += 1
promedio = total / cantidad_notas
print(f"El promedio de las {cantidad_notas} notas ingresadas es: {promedio}")