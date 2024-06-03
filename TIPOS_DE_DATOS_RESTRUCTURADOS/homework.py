# yo como dueño de mi mascota 
# deseo ver una lista de mis mascotas
# para tener un resumen o control de ellos. 

# YO COMO DUEÑO DE MI MASCOTA
# DESEO VER UNA LISTA DE MIS MASCOTAS
# PARA TENER UN RESUMEN O CONTROL DE ELLOS

# YO COMO DUEÑO DE MI MASCOTA 
# DESEO ACTUALIZAR LA EDAD DE MI MASCOTA
# PARA TENER UNA LISTA CORRECTA DE MI MASCOTA 

# YO COMO DUEÑO 
# Crear una lista de alumnos
lista_alumnos = [
    {
    "nombre": "Ruth",
    "apellido": "Castillo",
    "edad": 18
    },{
    "nombre": "Flor", 
    "apellido": "Lucana", 
    "edad": 18
    },{
    "nombre": "Rocío", 
    "apellido": "Lobo", 
    "edad": 20
    },{
    "nombre": "Lucy", 
    "apellido": "Rivera", 
    "edad": 18
    },{
    "nombre": "Abel", 
    "apellido": "Rojas", 
    "edad": 27
    }
]

# Insertar los datos de Anthony al final de la lista
lista_alumnos.append({"nombre": "Anthony", "apellido": "Smith", "edad": 24})

# Eliminar los datos de Abel si existen en la lista
lista_alumnos.remove({
    "nombre":"Abel",
    "apellido":"Rojas",
    "edad":27
})
print(lista_alumnos)


#tareas
# crear una lista con 4 diccionarios donde tendran los datos de sus mascotas ( nombre, edad, sexo, raza)
# tareas 
# mostrar la lista con los 4 diccionarios
# editar el 3er registro y cambiarle la edad sin modificar la lista original
# mostrar la lista original y luego la lista con el 3er registro modificado.

# Crear una lista con 4 diccionarios de mascotas
mascotas = [
    {"nombre": "Luna", "edad": 3, "sexo": "hembra", "raza": "Labrador"},
    {"nombre": "Max", "edad": 5, "sexo": "macho", "raza": "Golden Retriever"},
    {"nombre": "Bella", "edad": 2, "sexo": "hembra", "raza": "Poodle"},
    {"nombre": "Rocky", "edad": 4, "sexo": "macho", "raza": "Bulldog"}
]

# Mostrar la lista con los 4 diccionarios
print("Lista original:")
for mascota in mascotas:
    print(mascota)

# Editar el 3er registro y cambiarle la edad sin modificar la lista original
mascotas[2]["edad"] = 3

# Mostrar la lista original y luego la lista con el 3er registro modificado
print("\nLista original:")
for mascota in mascotas:
    print(mascota)

# Mostrar la lista con el 3er registro modificado
print("\nLista con el 3er registro modificado:")
for mascota in mascotas:
    print(mascota)

# un empresario de alquiler de autos desea guardar en una base de datos la informacion de sus vehiculos, 
# proceso que desea automatizar con un sistema infromatico, las acciones que puede realizar el empresario 
# son ver las lista de autos que tiene, podra tambien actualizar la lista y agregar un nuevo vehiculo
# casos de uso
# programacion


## caso de uso
# Ver lista de autos: El empresario podrá visualizar
# la lista de autos que tiene disponibles para alquilar.

## programacion 

# Lista de autos (simulando la base de datos)
autos = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "año": 2020, "precio_alquiler": 50},
    {"id": 2, "marca": "Honda", "modelo": "Civic", "año": 2021, "precio_alquiler": 55},
    {"id": 3, "marca": "Ford", "modelo": "Focus", "año": 2022, "precio_alquiler": 75}
]

def ver_lista_autos():
    # verifica si hay autos en la lista 
    if len(autos) == 0:
        print("No hay autos disponibles.")
    else:
        #imprime la lista de autos disponibles
        print("Lista de autos disponibles:")
        for auto in autos:
            print(f"ID: {auto['id']}, Marca: {auto['marca']}, Modelo: {auto['modelo']},
                   Año: {auto['año']}, Precio de alquiler: {auto['precio_alquiler']}")

ver_lista_autos()
