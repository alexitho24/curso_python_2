## crear un a funcion que resiva por argumento n numeros y retorne una lista con los numeros pares 

def numeros_pares(*args):
    lista_pares = []
    for num in args:
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares

# Ejemplo de uso
numeros = numeros_pares(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numeros)  

# crear tres funciones para los siguientes casos
# calcular el numero menor 
# calcular el numero mayor 
# calcular la suma de todos los numeros 
# se le pasara por argumento n numeros 


def numero_menor(*numeros):
    return min(numeros)

def numero_mayor(*numeros):
    return max(numeros)

def suma_numeros(*numeros):
    return sum(numeros)

# Ejemplo de uso
print(numero_menor(5, 10, 3, 8))  
print(numero_mayor(5, 10, 3, 8)) 
print(suma_numeros(5, 10, 3, 8)) 

# ejemplo 2 
def numero_menor(*numeros):
    menor = numeros[0]
    for num in numeros:
        if num < menor:
            menor = num
    return menor

def numero_mayor(*numeros):
    mayor = numeros[0]
    for num in numeros:
        if num > mayor:
            mayor = num
    return mayor

def suma_numeros(*numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma

# Ejemplo de uso
print(numero_menor(5, 10, 3, 8)) 
print(numero_mayor(5, 10, 3, 8)) 
print(suma_numeros(5, 10, 3, 8)) 

