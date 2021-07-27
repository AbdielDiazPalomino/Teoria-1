#Acá sacamos una clase llamada Estudiante que la podemos importar 
#a otro programa

class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

    def desactivar(self):
        self.esta_activo = False

estudiante1= Estudiante("Marcos", 35, "Python")

#acá le decimos si el estudiante está activo y como le pusimos True
#va a decir True
print(estudiante1.esta_activo)

#Pero luego ejecutamos la función desactivar y
#ahora va a decir False si lo imprimimos
estudiante1.desactivar()

print(estudiante1.esta_activo)