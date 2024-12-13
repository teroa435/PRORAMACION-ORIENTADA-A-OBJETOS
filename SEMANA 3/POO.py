# Programación Orientada a Objetos (POO)

class Clima:
    """Clase que representa la información diaria del clima."""
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        """Agrega una temperatura a la lista de temperaturas."""
        self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        """Calcula el promedio de las temperaturas almacenadas."""
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Ejecución usando programación orientada a objetos
clima = Clima()
for i in range(7):
    temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    clima.ingresar_temperatura(temperatura)

promedio_poo = clima.calcular_promedio()
print(f"El promedio semanal de las temperaturas es: {promedio_poo:.2f}")
