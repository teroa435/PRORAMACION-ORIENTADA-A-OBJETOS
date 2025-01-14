class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.__velocidad_maxima = velocidad_maxima  # Atributo privado

    # Método público para obtener la velocidad máxima
    def obtener_velocidad_maxima(self):
        return self.__velocidad_maxima

    # Método de clase base
    def detalles(self):
        return f"{self.marca} {self.modelo} con velocidad máxima de {self.__velocidad_maxima} km/h"
class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, num_puertas):
        super().__init__(marca, modelo, velocidad_maxima)  # Llamada al constructor de la clase base
        self.num_puertas = num_puertas

    # Sobrescribir el método 'detalles' para el coche
    def detalles(self):
        return f"{super().detalles()} y {self.num_puertas} puertas"

    # Método para modificar la velocidad máxima, demostrando encapsulación
    def cambiar_velocidad_maxima(self, nueva_velocidad):
        if nueva_velocidad > 0:
            self.__velocidad_maxima = nueva_velocidad
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_motor):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_motor = tipo_motor

    # Sobrescribir el método 'detalles' para la motocicleta
    def detalles(self):
        return f"{super().detalles()} con motor {self.tipo_motor}"
# Crear instancias de las clases
vehiculo = Vehiculo("Toyota", "Corolla", 180)
coche = Coche("Ford", "Fiesta", 200, 5)
motocicleta = Motocicleta("Yamaha", "YZF-R1", 300, "4 tiempos")

# Mostrar detalles de los vehículos
print(vehiculo.detalles())
print(coche.detalles())
print(motocicleta.detalles())

# Modificar la velocidad máxima de un coche y mostrar los detalles nuevamente
coche.cambiar_velocidad_maxima(220)
print(coche.detalles())
