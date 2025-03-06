import threading

# Variable global compartida
contador_global = 0

# Crear un objeto Lock (mutex)
mutex = threading.Lock()

# Función que incrementa el contador global de forma segura utilizando un mutex
def incrementar():
    global contador_global
    # Adquirir el mutex
    mutex.acquire()
    try:
        # Sección crítica: Incrementar el contador
        contador_global += 1
    finally:
        # Liberar el mutex
        mutex.release()

# Función que ejecuta la tarea de incrementar el contador un número determinado de veces
def tarea():
    for _ in range(100000):
        incrementar()

# Crear dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

# Imprimir el valor final del contador global
print("El valor final del contador global es:", contador_global)
