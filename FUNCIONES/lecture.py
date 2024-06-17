# return devuelve valores que podre hacer uso 
# crear una funcion que retorne el numero 10 y muestre por terminal si es par
# siempre que el valor 
def diez():
    return 10 
if diez()%2==0:
    print("es par")
else:
    print("es impar")
# print solo muestra por terminal 

# return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato o un tipo de dato estruccturado

# cear una funcion que me mustre el producto de dos numeros
def producto(a,b):
    return a*b

# crear una funcion que me retorne una lista de tres numeros
def lista_numeros():
    return [3,2,6]

# print usaremos cada vez que muestra funcion retornr un mensaje

#crear una funcion que por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre
def mensaje(nombre):
    print(f"hola, {nombre}, bienvenido al chongo") 
# mensaje ("jose")

#crear una funcion que reciba por parametro una lista de numeros y me devuelva el numero menor, 
# mostrar por terminal el valor retornado por la funcion 
lista=[4,3,6,74,5]
def min(1):
    minimo=1[0]
    for n in 1:
        if n < minimo:
            minimo=n
        return minimo
    print(min(lista))   

# crear una funcion que resiba como parametro en nombre y la edad de una persona mi funcion debera retornar un
# diccionario con los datos, luego mostrar por terminal el valor de retorno en mi funcion
def crear_persona(nombre, edad):
    persona = {"nombre": nombre, "edad": edad}
    return persona
def mostrar_valor_retorno():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    datos_persona = crear_persona(nombre, edad)
    print("Datos de la persona:")
    print(datos_persona)
mostrar_valor_retorno()