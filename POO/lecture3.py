# crear una clase de alumnos con los atributos que usted crea por conveninte 
# luego instancia a 4 alumnos
class Alumno:
    def _init_(self, nombre, dni, edad, email, programa_estudio="APSTI" ):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        self.email=email
        self.programa_estudio=programa_estudio
    # metodos
    def escribir(self):
        print("estoy escribiendo")
    def tarea(self,nombre_docente):
        print ("haciendo la tarea de:", nombre_docente)
    def terminar_tarea(self):
        print ("terminando tarea anterior")
maricielo=Alumno("MARICIELO",75869321,14,"yo@gmail")
maricielo.tarea("alicia")
maricielo.terminar_tarea()
maricielo.tarea ("alvarez")


maricielo=Alumno("MARICIELO",75869321,14,"yo@gmail")
print(maricielo.programa_estudio)
mercedes=Alumno("meche",74859632,15,"tu@gmail.com", "Enfermeria")
prin(mercedes.programa_estudio)
       

