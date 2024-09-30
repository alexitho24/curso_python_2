# crear una clase de alumnos con los atributos que usted crea por conveninte 
# luego instancia a 4 alumnos
class Alumno:
    def __init__(self, nombre, edad, grado, promedio):
        self.nombre = nombre      
        self.edad = edad          
        self.grado = grado        
        self.promedio = promedio   

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Grado: {self.grado}")
        print(f"Promedio: {self.promedio:.2f}\n")


# Instanciando 4 alumnos
alumno1 = Alumno("Juan Pérez", 16, "10°", 8.5)
alumno2 = Alumno("María Gómez", 15, "9°", 9.0)
alumno3 = Alumno("Carlos López", 17, "11°", 7.8)
alumno4 = Alumno("Ana Torres", 16, "10°", 9.5)

# Mostrando la información de los alumnos
alumno1.mostrar_informacion()
alumno2.mostrar_informacion()
alumno3.mostrar_informacion()
alumno4.mostrar_informacion()
