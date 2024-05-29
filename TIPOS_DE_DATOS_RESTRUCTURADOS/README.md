# tipos de datos estructurados (TDA- tipos de datos abstractos)
!-- ```python
#lista - sus valores o elemtos se pueden actualizar, eliminar.
lista=["abel",20,5.2,.5,False,["texto",.2]]
#tupla - sus valores o elementos no pueden ser modificados o eliminados.
tupla=("abel",20,5.2,,False,[])

#diccionarios o objetos 
#loa diccionarios almacenan los datos con clave :valor
diccionario={"nombre":"antonio", "edad":15 "sexo":False}
```
- {!TIP}
- **OBSERVACION** Que los tipos de datos estruccturados pueden almacenar en su interior otros tipos de datos estructurados.

```python
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":20,
        "amigos":["no tiene"]
    },{
        "nombre":"ruth",
        "edad":13
        "amigos":["flor", "rosio"]
    },{
        "nombre":"rony",
        "edad":23
        "amigos"["no tiene"]
    }

]
```
## metodos 
### 1. convertir texto a lista 
```python
texto="hola"
list(texto)
#["h","o","l","a"]

# METODO SPLIT - trocea textos mediante un limitador ejemplo 
texto="hola como estan mascotas"
texto.split(",")


# join es el metodo que utilizamos para unir elemtos de una sola lista 

texto_largo="este es un texto largo chiquitas y chiquitos"
nuevo_texto=texto_largo.split(" ")
print(" ".join(nuevo_texto))

```
### 2. agregar elementos a una lista 
```python
#metodo append - es el metodo que me permite agregar elementos al final de una lista 
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]

# metodo insert - es el metodo que me permite agregar elemtos en cualquier ubicacion de mi lista 

lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"anthony")
```

### 3. eliminar elemento de una lista 
```python
# metodo pop - es el metodo que elimina el ultimo elemto de una lista es el contrario de append.
``` 

lista_nombres=["edith","ruth","luz"]
lista_nombres.pop()

# primera manera - metodo remove - este metodo elimina el por el nombre  el elemento que coincida dentro de mi lista 

```python

lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")

# segunda opcion - metodo pop - al pasarle por pametro un indice este lo elima de la lista.


lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)
```

# buscar un elemento en una lista 
```python 
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

pertenecia="edith" in lista-nombres -->


# crear una lista de 5 alumnos cada alumno almacenaremos su nombre apellido y edad 

# insertar al final de la lista los datos de antoni 

# eliminar de la lista si existe los datos de abel

# buscar y mostrar la posicion del alumno 4 de la lista 

los nombres de los alumnos seran 
antoni
abel
ruth
lizbeth
luz
```python
# Crear una lista 
alumnos = [
    {"nombre": "Antoni", "apellido": "Gomez", "edad": 25},
    {"nombre": "Abel", "apellido": "Perez", "edad": 23},
    {"nombre": "Ruth", "apellido": "Martinez", "edad": 22},
    {"nombre": "Lizbeth", "apellido": "Garcia", "edad": 24},
    {"nombre": "Luz", "apellido": "Lopez", "edad": 21}
]

alumnos.append({"nombre": "Antoni", "apellido": "Nunez", "edad": 26})

alumnos = [alumno for alumno in alumnos if alumno["nombre"] != "Abel"]

posicion_alumno_4 = None
for i, alumno in enumerate(alumnos):
    if i == 3:  
        posicion_alumno_4 = i
        break

print("Lista de alumnos actualizada:")
for alumno in alumnos:
    print(alumno)

print("La posición del alumno 4 en la lista es:", posicion_alumno_4)












### 5, comparacion de listas
podemos hacer uso de los operadores de comparacion para comparar listas 
**ejm:** 

compra=[1,2,3,]>[1,2,4]
# 1 no por que son iguales en ambas listas
# 2 no por que son iguales en ambas listas 
# 3 evalua que es menor a 4 
# entonces la primera lista es menor que la segunda lista 
print(compra)
# salida:
```
### 6. cuidado con las copias
### 7. fe de erratas (actualizar listas )
lista=[2,3,4,5,6]
copia_lista=lista[0]=2
print(copia_lista)
#[2,3,4,5,6]
# modificando lista con diccionario 
alumnos=[
    { 
        "nombre":"abel"
        "edad":15
    },
    {
        "nombre":"anthony"
        "edad":29
    }
]
alumnos[0]["edad"]=30
print(alumnos)
# crear un programa que reciba una lista desordenada y muestre por terminal la lista ordenada y la lista previa a ser ordenada.
lista=[4,76,1,3,6,8,2]
lista.sort()
print(lista)

#tareas
# crear una lista con 4 diccionarios donde tendran los datos de sus mascotas ( nombre, edad, sexo, raza)
# tareas 
# mostrar la lista con los 4 diccionarios
# editar el 3er registro y cambiarle la edad sin modificar la lista original
# mostrar la lista original y luego la lista con el 3er registro modificado.