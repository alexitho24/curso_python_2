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

