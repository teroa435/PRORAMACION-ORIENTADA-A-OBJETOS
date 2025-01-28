import threading
import time

# Función que ejecutará cada hilo
def tarea(nombre, tiempo):
    print(f"Hilo {nombre} iniciando")
    time.sleep(tiempo)
    print(f"Hilo {nombre} finalizando")

# Creación de hilos
t1 = threading.Thread(target=tarea, args=("A", 2))
t2 = threading.Thread(target=tarea, args=("B", 4))
t3 = threading.Thread(target=tarea, args=("C", 1))

# Inicio de hilos
t1.start()
t2.start()
t3.start()

# Esperar a que terminen todos los hilos
t1.join()
t2.join()
t3.join()

print("Todos los hilos han finalizado")

# Beneficios de los hilos:
# 1. Permiten la ejecución concurrente de tareas sin bloquear el flujo principal.
# 2. Mejoran el rendimiento en tareas de entrada/salida como lectura de archivos o solicitudes de red.
# 3. Optimizan el tiempo de respuesta en aplicaciones interactivas.
