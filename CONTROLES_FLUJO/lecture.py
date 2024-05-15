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
    
#         #contador += 1

# print(f"la cantidad de letras a que tengo es {contador}
# sentence = input("Escribe una oración: ")
# count = 0
# for i in range(len(sentence)):
#     if sentence[i] == ',':
#         count +=1
# print(count),

#2
# oracion:str=input("ingrese una oriacion: ")
# contador=0
# for indice,letra in enumerate(oracion):
#     if letra == ",":
#      print(f"su indice es {indice}")
#     contador=1
# print(f"la cantidad de comas es {contador}")


#  escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad)
edad = int(input("Por favor, ingresa tu edad: "))

for n in range(1, edad+1):
    print("Has cumplido",n, "años")