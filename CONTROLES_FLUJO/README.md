

 almacenar el if en un variable 
``` python  -->
# primer ejemplo if estructurado
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")
# segundo ejemplo if almacenado en variable
edad:int=int(input("escribe tu edad: "))
rewspuesta:str="eres mayor" if edad>=18 else "eres menor" 
print(respuesta)

> para FOR

for n in range(1,11):
    prin(n)

crear un programa que me imprima las 5 bocales 

vocales= str="aeiou"
for n in range(0,5):
    print(vocales[n])

crear un programa que me muestre los 8 primeros numeros pares

for i in range(1, 17):
    if n % 2 == 0:
        print(n)

crear un programa que me pida al usuario escribir una oracion y mostrar por terminal la cantidad de vocales a que tiene esa oracion 
OJO SOLO LA "a" MINUSCULA

oracion = input("Escribe una oración: ")
contador = 0

for letra in oracion:
    if letra == 'a':
        contador += 1

print(contador)
 
 mismo ejercicio con rangue.
 
oracion = input("Escribe una oración: ")
contador = 0
for n in range(0,len(oracion)):
    if oracion [n]== 'a':
        contador=contador+1
    
        #contador += 1

print(f"la cantidad de letras a que es {contador}")


#crear un programa que me cuente  la cantidad de comas y me muestre sus indices.
#ojo: tierne que pedir al usuario.
sentence = input("Escribe una oración: ")
count = 0
for n in range(len(sentence)):
    if sentence[n] == ',':
        count += 1
print(count)


# Solicitar al usuario que ingrese una cadena de texto
texto = input("Por favor, ingresa una cadena de texto: ")

# Inicializar una lista para almacenar los índices de las comas
indices_comas = []

# Contador para la cantidad de comas
cantidad_comas = 0

# Recorrer la cadena de texto para encontrar las comas y sus índices
for i in range(len(texto)):
    if texto[i] == ',':
        cantidad_comas += 1
        indices_comas.append(i)

# Mostrar la cantidad de comas y sus índices
print("La cantidad de comas en el texto es:", cantidad_comas)
print("Los índices de las comas son:", indices_comas)

el extend 
este es para poder agregar multiples elementos a una lista 
#lo del profe
oracion:str=input("ingrese una oriacion: ")
contador=0
for indice,letra in enumerate(oracion):
    print(f"su indice es {indice}")
    contador=1
print(f"la ccantidad de comas es {contador}")
# el enumerate es mas rapido y almacena menos en documentos grandes y medianos
# 