# METODOS EN PYTHON
## NUMERO
PYTHON
len(12345678)
# devuelve 1 cantidad de digitos
# 7

int=int(input("variable: "))
# INPUT almacena la informacion de una variable ya sea numero, texto, etc.
# pero siempre se define si es int=int() o srt=int()



## TEXTO
PYTHON
len("hola gusano")
# devuelve la cantidad de caracteres
# el espacio cuernta tambien como un caracter
# 11

str=str(input("variable: "))
# INPUT almacena la informacion de una variable ya sea numero, texto, etc.
# pero siempre se define si es str=str() o srt=int()

str.join(iterable)
# une todos los elementos de una iteracion con un especifico str
print("y".join(["a","b","c"])) # a y b y c


## LISTAS
PYTHON
len(["h","o","l","a";"m";"a";"s";"c";"o";"t";"a"])
# devuelve cantidad de elemntos ("elemento" es lo que esta dentro de array)
# el espacio cuenta tanmbien comoun caracter
#11

tienda=["manzana","banana","fresa","orange";"apple"]
tienda.clear()
#elimina todos los elementos de la lista

tienda=["manzana","banana","fresa","orange";"aple"]
tienda.copy()
# devuelve una copia de la lista especificada

numeros=[1,1,2,3,3,3,3,3,3]
numeros.count(3) # 6
# devuelve la cantidad de veces de un numero que esta dentro de una lista

numeros=[1,2,3,4,5,6,7]
numeros.index(3)
# Buscar un elemento en una lista .index (se usa para informacion grande)

lista_nombres=["liz","ruth","luz"]
lista_nombres.insert(0:"rocio") #["rocio","liz","ruth","luz"]
# agrega elementos en la ubicacion que asignes

tienda=["manzana","banana","fresa","orange"]
tienda.append("atun")
# añade elemtos al final de la lista

lista_nombres=["liz","ruth","luz"]
lista_nombres.pop() #["luz","ruth"]
#elimina el ultimo elemnto de una lista

lista_nombres=["liz","ruth","luz"]
lista_nombres.remove("ruth")
# elimina un elemento de una lista segun le asigne

## TUPLAS
PYTHON



## DICCIONARIOS
PYTHON
moto={
"marca":"torito",
"color":"verde",
"precio/alquiler":30
}

variable=motors.get("color")
print(variable) # "verde"
# ".get" devuelve el valor del elemento con la clave especificada

motors.update("color":"negro")
print(motors)
# ".update" inserta los elemntos especificados en el diccionario (deben ser objetos iterables con pares clave-valor)

motors.copy()
print(motors)
# ".copy" devuelve copsssia del diccionario especificado
