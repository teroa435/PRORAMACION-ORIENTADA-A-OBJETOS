import random
import time


class Memoria:
    def __init__(self, tamanio):
        """Inicializa la memoria con bloques libres"""
        self.tamanio = tamanio
        self.memoria = [None] * tamanio  # None = bloque libre

    def asignar(self, proceso, tamanio_requerido):
        """Asigna bloques contiguos a un proceso usando estrategia First-Fit"""
        for i in range(self.tamanio - tamanio_requerido + 1):
            # Verifica si hay bloques contiguos libres
            if all(self.memoria[i + j] is None for j in range(tamanio_requerido)):
                # Asigna los bloques al proceso
                for j in range(tamanio_requerido):
                    self.memoria[i + j] = proceso
                print(
                    f"✅ Proceso {proceso} asignó {tamanio_requerido} bloques (posiciones {i}-{i + tamanio_requerido - 1})")
                return True
        print(f"❌ Proceso {proceso} no pudo asignar {tamanio_requerido} bloques (no hay espacio contiguo)")
        return False

    def liberar(self, proceso):
        """Libera todos los bloques ocupados por un proceso"""
        for i in range(self.tamanio):
            if self.memoria[i] == proceso:
                self.memoria[i] = None
        print(f"🔄 Proceso {proceso} liberó sus bloques de memoria")

    def mostrar_memoria(self):
        """Muestra el estado actual de la memoria con formato visual"""
        print("\n📊 Estado de la Memoria:")
        print("┌" + "─┬" * (self.tamanio - 1) + "─┐")
        print("│" + "│".join(f"{' ' if b is None else b[-1]}" for b in self.memoria) + "│")
        print("└" + "─┴" * (self.tamanio - 1) + "─┘")
        print("Leyenda: A-E = Procesos, ' ' = Libre\n")


def proceso(nombre, memoria):
    """Simula el comportamiento de un proceso"""
    tamanio_requerido = random.randint(1, 5)
    print(f"\n🔄 {nombre} solicita {tamanio_requerido} bloques...")

    if memoria.asignar(nombre, tamanio_requerido):
        # Simula tiempo de ejecución del proceso
        tiempo_ejecucion = random.uniform(0.5, 2.0)
        time.sleep(tiempo_ejecucion)

        # Libera la memoria al finalizar
        memoria.liberar(nombre)

    # Tiempo entre procesos
    time.sleep(random.uniform(0.5, 1.5))


def simulacion_memoria():
    """Ejecuta la simulación completa"""
    print("🚀 INICIANDO SIMULACIÓN DE MEMORIA")
    print("---------------------------------")

    # Configuración inicial
    memoria = Memoria(10)  # Memoria de 10 bloques
    procesos = ['Proceso-A', 'Proceso-B', 'Proceso-C', 'Proceso-D', 'Proceso-E']

    # Ejecuta 5 procesos aleatorios
    for i in range(5):
        proceso_actual = random.choice(procesos)
        proceso(proceso_actual, memoria)
        memoria.mostrar_memoria()

    print("\n🔚 FIN DE LA SIMULACIÓN")


if __name__ == "__main__":
    simulacion_memoria()