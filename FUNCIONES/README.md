# FUNCIONES
## concepto
Matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos` y produce un valor denominado `resultado` .
>[!NOTE]
> Todos los lenguajes de programacion tiene funciones incorporadas (`funciones internas`), y funciones creadas por el usuario (`funciones externas`).
 
En programacion una funcion es un subprograma, es una estructura que nos permite agrupar codigo y sus principales objetivos son:
- `NO REPETIR` fracmentos de codigo
- `REUTILIZAR` el codigo en distintos ecenarios 
## Estructura de una funcion 
una funcion viene `difinida` por un `nombre`, sus `parmetros` y su valor de `retorno`.
una ves creada la funcion ´podremos solicitar su ejecucion `invocando`la funcion por su `nombre`.
## Difinir una funcion en python 
ara definir una funcion en python primero utilizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros` con `()`si es una funcion sin parametros, `(a)` si es una funcion con parametros, si se tuviera mas de un parametro iran separados por `,`, finalizaremos la linea con `:`,  en la siguiente linea sin olvidar el identado, comenzara el `cuerpo`  de la funcion (micro programa ) que puede contener 1 o mas sentencias, finalmente devera `retornar` un resultado con la palabra reservada `return`.
> [!TIP]
> como retorno tambien se puede utilizar la funcion `funcion interna`, `print()`, para depuracion de codigo no es recomendable usarlo en produccion.
**EJEMLO:**
``` python 
def saludo ():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"{saludo}, {saludo_dos}"
    #print(f"{saludo}, {saludo_dos}")
print(saludo())
#saludo()
```
## invocar una funcion 
para invocar, (o llamar, ejecutar) una funcion solo tendremos que escribir el nombre ` nombre ` de la funcion seguido por `()` parentesis 
```python
def saludo():
    print("hola")
#invocando la funcion 
saludo()
```
## Retornar un valor 
las funcones pueden retornar (o devolver) un valor.
```python
def uno():
    return 1
uno()
```
>[!WARING]
> No confundir `print` con `return`. el valor retornado por `return` nos permite usarlo fuera de su contexto. y `print()` solo mostrara el literal por terminal.
**ejemplo**
*en el archivo `lecture.py`
## Retornando multiples valores 
el secreto es hacerlo mediante un tipo de dato estructurado 
```python
def varios():
    return 2,3,4
varios()
#retorna (2,3,4)
def lista():
    return ["hola", 45 ]
# retorna ["hola",45]
def dicc():
    return {"nombre":"jose","edad":45}
#retorna {#"nombre":"jose":"edad":45}
```
## parametros y argumentos 
si una funcion no dispusiera de valores de entrada estaria limitada en su actuacion. Es por ello que los `parametros` no permiten variar los datos que consume una funcion para obtener distintos resultados.
**ejemplo**
*crear una funcion que recibe un valor numerico y devuelve su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion 
    sqrt(4)
```
cuando llamamos a una funcion con `argumentos`, los valores de estos argumentos se copian en los correspondiente `parametros` dentro de la funcion.
```python 
# creamos la funcion
def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)
```
### Argumentos nominales
en esta aproximacion los argumentos no son copiados en un orden especifico sino que **se asigana por nombre a cada parametro**. Ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros en la difinicion de la funcion. para utilizarlo, basta con realizar una asignacion  de cada argumento en la propia llamada a la funcion.
**ejemplo**
```python
def buil_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia},
    con {num_core} cores y con una 
    fecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales
    build_cpu(num_core=4,familia="intel",frecuencia=2.7)
```
### Argumentos posicionales
los argumentos son copiados en un orden especifico, en este caso debemos conocer o recordad cual es el orden de los parametros 
**ejmplo**
```python
def buil_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia},
    con {num_core} cores y con una 
    fecuencia de {frecuencia}
    """)
# haciendo uso de argumentos posicionales
buil_cpu("intel",4,2.7)
```
## Parametros por defecto
es posible espesificar **valor por defecto** en los parametros de una funcion, en el caso de que no se proporcione un valor al argumento en la llamada a la funcion, el parametro correspondiente tomara el valor definido por defecto.
**ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):
    alumnos("ruth","castillo")
    alumnos("anthony","crucez","desaprobado")
```
## Desempaquetado/Empaquetado de argumentos (tarea)
El desempaquetado y empaquetado de argumentos en Python se refiere a la capacidad de pasar múltiples argumentos a una función de manera flexible.
 
# Empaquetado de argumentos:
 
- Empaquetado de argumentos posicionales: Permite pasar un número variable de argumentos posicionales a una función utilizando el operador  * . Por ejemplo:
 
python
 Copiar
def sumar(*args):
    total = sum(args)
    return total

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)  # Output: 15
 
- Empaquetado de argumentos de palabras clave: Permite pasar un número variable de argumentos de palabras clave a una función utilizando el operador  ** . Por ejemplo:
 
python
 Copiar
def imprimir_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

imprimir_info(nombre="Alice", edad=30, ciudad="Madrid")
Output:
nombre: Alice
edad: 30
ciudad: Madrid
 
# Desempaquetado de argumentos:
 
- Desempaquetado de argumentos posicionales: Permite pasar una secuencia de elementos como argumentos posicionales a una función utilizando el operador  * . Por ejemplo:
 
python
 Copiar
numeros = [1, 2, 3, 4, 5]
resultado = sum(*numeros)
print(resultado)  # Output: 15
 
- Desempaquetado de argumentos de palabras clave: Permite pasar un diccionario como argumentos de palabras clave a una función utilizando el operador  ** . Por ejemplo:
 
python
 Copiar
datos = {"nombre": "Bob", "edad": 25, "ciudad": "Barcelona"}
imprimir_info(**datos)
# Output:
# nombre: Bob
# edad: 25
# ciudad: Barcelona
 
 
El empaquetado y desempaquetado de argumentos en Python proporciona flexibilidad al trabajar con funciones que requieren un número variable de argumentos.


## funciones interna de python(tarea)
Las funciones internas de Python son funciones incorporadas en el lenguaje que están disponibles para su uso sin necesidad de importar ningún módulo adicional. Algunas de las funciones internas más comunes en Python son:
 
1.  print() : Utilizada para imprimir mensajes en la consola.
2.  len() : Devuelve la longitud de un objeto, como una lista o una cadena.
3.  type() : Devuelve el tipo de un objeto.
4.  input() : Permite al usuario ingresar datos desde la consola.
5.  range() : Genera una secuencia de números.
6.  sum() : Calcula la suma de los elementos en una lista.
7.  min() : Devuelve el valor mínimo en una lista.
8.  max() : Devuelve el valor máximo en una lista.
9.  abs() : Devuelve el valor absoluto de un número.
10.  round() : Redondea un número al entero más cercano.
 
Estas son solo algunas de las muchas funciones internas disponibles en Python para realizar diversas operaciones.

## tipos de funciones 
### funciones anonimas (funciones lambda)
una funcion que no tiene nombre
`lambada:"hola`
Funciones Anónimas
Las funciones anónimas en Python, también conocidas como funciones lambda, son funciones sin nombre definidas utilizando la palabra clave lambda. Aquí tienes un resumen sobre las funciones anónimas en Python:
Características Principales
Las funciones anónimas son funciones pequeñas y temporales.
Se utilizan para realizar operaciones simples y rápidas.
No requieren la declaración formal de una función utilizando def.
Sintaxis Básica
La sintaxis básica para definir una función anónima en Python es la siguiente:

lambda arguments: expression

Ejemplo de Uso
Definir una función anónima que suma dos números
sumar = lambda x, y: x + y
print(sumar(3, 4))  # Output: 7
### funciones closure
una funcion que dentro tiene otra funcion 
`def saludo(nombre):
print (f"bienbenido {nombre}")`

### funciones callback
funciones que reciben por parametro otra funcion
`int(input("ingrese un numero: "))`

### programacion funcional
la programacion funcional no requiere que sepas como se
desarrolla y ejecuta el procesamiento de la informacion 
**ejemplo**
```python 
lista=[5,7,8,4,1]
def num_minimo(1):
    minimo=1[0]
    for n in l:
        if n < minimo:
            minimo=n
        return minimo
# programacion funcional 
min(lista)
```

#### averiguar sobre map(), filter(), reduce()

## map
 la función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...). La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla. Es posible utilizar map junto con una función lambda. En lo personal considero esta la mejor opción
```python
  
## filter
Cómo su nombre lo indica, esta función nos permite realizar un filtro sobre los elementos de la colección. La estructura de la función es la siguiente. La función a aplicar será aplicada a cada uno de los elementos de la colección. Esta función siempre deberá retornar un valor booleano.

## reduce
reduce nos permitirá reducir los elementos de la colección. Podemos ver a esta función como un acumulador