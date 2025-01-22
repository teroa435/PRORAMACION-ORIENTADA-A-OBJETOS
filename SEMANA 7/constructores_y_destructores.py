class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("¡Hola! Soy", self.nombre, "y tengo", self.edad, "años.")

    def __del__(self):
        print(self.nombre, "ha sido eliminado.")

# Creando objetos
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)

# El destructor se llama automáticamente cuando el objeto ya no es necesario
# Por ejemplo, cuando sale del alcance:
del persona1

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.saludo = "Hola"  # Atributo adicional
        print(self.saludo, "Soy", self.nombre, "y tengo", self.edad, "años.")

    def __del__(self):
        print(self.nombre, "se despide.")

    def presentarse(self):
        print("Mi nombre es", self.nombre)
