1 # Pedir al usuario que ingrese su edad
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si la edad ingresada es mayor o igual a 18
if edad >= 18:
    print("Eres mayor de edad causita.")
else:
    print("Eres menor de edad, mocos@.")


2 # Almacenar la contraseña en una variable
contrasena_guardada = "tu_papi"

# Pedir al usuario que ingrese la contraseña
contrasena_usuario = input("Por favor, ingresa la contraseña: ")

# Verificar si la contraseña introducida coincide con la guardada (sin distinguir mayúsculas y minúsculas)
if contrasena_usuario.lower() == contrasena_guardada.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")  