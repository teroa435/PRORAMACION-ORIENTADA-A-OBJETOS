# Programación Tradicional

def ingresar_temperaturas():
    """Solicita al usuario las temperaturas diarias de la semana y las almacena en una lista."""
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de una lista de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

# Ejecución usando programación tradicional
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")
