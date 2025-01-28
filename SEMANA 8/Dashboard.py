import os
import subprocess
from datetime import datetime
from colorama import Fore, Style, init

# Inicializa colorama para colores multiplataforma
init(autoreset=True)

def mostrar_codigo(ruta_script):
    """Muestra el contenido de un script."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n{Fore.CYAN}--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"{Fore.RED}El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"{Fore.RED}Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script en una terminal separada."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        elif os.name == 'posix':  # Unix-based systems
            terminal = 'xterm' if subprocess.call(['which', 'xterm'], stdout=subprocess.DEVNULL) == 0 else 'open'
            subprocess.Popen([terminal, '-hold', '-e', 'python3', ruta_script])
        else:
            print(f"{Fore.YELLOW}Sistema operativo no compatible para ejecutar scripts automáticamente.")
    except Exception as e:
        print(f"{Fore.RED}Ocurrió un error al ejecutar el código: {e}")

def registrar_historial(ruta_script):
    """Registra en un archivo log la ejecución de un script."""
    with open('historial_ejecuciones.log', 'a') as log:
        log.write(f"{datetime.now()} - Ejecutado: {ruta_script}\n")

def mostrar_menu():
    """Muestra el menú principal del dashboard."""
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    print(f"{Fore.GREEN}\nBienvenido al Dashboard de Gestión de Proyectos")
    while True:
        print(f"\n{Style.BRIGHT}Menu Principal")
        for key, unidad in unidades.items():
            print(f"{key} - {unidad}")
        print("0 - Salir")

        eleccion_unidad = input(f"{Fore.YELLOW}Elige una unidad o '0' para salir: {Style.RESET_ALL}")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """Muestra el submenú con las subcarpetas de la unidad seleccionada."""
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(f"\n{Fore.BLUE}Submenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input(f"{Fore.YELLOW}Elige una subcarpeta o '0' para regresar: {Style.RESET_ALL}")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print(f"{Fore.RED}Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print(f"{Fore.RED}Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts disponibles en la subcarpeta seleccionada."""
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n{Fore.MAGENTA}Scripts disponibles")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input(f"{Fore.YELLOW}Elige un script, '0' para regresar o '9' para ir al menú principal: {Style.RESET_ALL}")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input(f"{Fore.GREEN}¿Desea ejecutar el script? (1: Sí, 0: No): {Style.RESET_ALL}")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                            registrar_historial(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print(f"{Fore.RED}Opción no válida. Regresando al menú de scripts.")
                        input(f"{Fore.YELLOW}\nPresiona Enter para volver al menú de scripts.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print(f"{Fore.RED}Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
