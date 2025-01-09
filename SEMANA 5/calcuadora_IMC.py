# calculadora_imc.py
# Este programa calcula el Índice de Masa Corporal (IMC) de una persona e indica su clasificación según la OMS.

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) a partir del peso y la altura.

    :param peso: Peso en kilogramos (float).
    :param altura: Altura en metros (float).
    :return: El IMC calculado (float).
    """
    if peso <= 0 or altura <= 0:
        return "Peso y altura deben ser valores positivos."
    return peso / (altura ** 2)


def clasificar_imc(imc):
    """
    Clasifica el IMC según las categorías de la OMS.

    :param imc: Índice de Masa Corporal (float).
    :return: Clasificación del IMC (str).
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main():
    """
    Función principal para ejecutar el programa.
    """
    print("Calculadora de Índice de Masa Corporal (IMC)")
    try:
        # Solicitar al usuario el peso y la altura
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))

        # Calcular el IMC
        imc = calcular_imc(peso, altura)

        # Manejar casos de error
        if isinstance(imc, str):  # Verifica si hay un mensaje de error
            print(imc)
        else:
            # Mostrar el resultado y la clasificación
            clasificacion = clasificar_imc(imc)
            print(f"Su IMC es: {imc:.2f}")
            print(f"Clasificación: {clasificacion}")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos para el peso y la altura.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
