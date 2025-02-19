import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(int(id), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            open(self.archivo, 'w').close()  # Crear un archivo vacío si no existe
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """Añade un producto al inventario y lo guarda en el archivo."""
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' añadido exitosamente.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto y guarda los cambios."""
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print(f"Producto ID {id} actualizado exitosamente.")
                return
        print(f"Error: Producto con ID {id} no encontrado.")

    def eliminar_producto(self, id):
        """Elimina un producto del inventario y guarda los cambios."""
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print(f"Producto ID {id} eliminado exitosamente.")
                return
        print(f"Error: Producto con ID {id} no encontrado.")

    def listar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Listar Productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == '2':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == '3':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == '4':
            inventario.listar_productos()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()