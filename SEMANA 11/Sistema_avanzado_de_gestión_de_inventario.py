import json
import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado con éxito.")
        else:
            print("Error: El ID del producto no existe.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado con éxito.")
        else:
            print("Error: El ID del producto no existe.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if producto.get_nombre() == nombre]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def guardar_inventario(inventario, archivo="inventario.json"):
    with open(archivo, 'w') as f:
        productos_dict = {id: {"nombre": producto.get_nombre(), "cantidad": producto.get_cantidad(), "precio": producto.get_precio()} for id, producto in inventario.productos.items()}
        json.dump(productos_dict, f)
    print("Inventario guardado con éxito.")


def cargar_inventario(archivo="inventario.json"):
    inventario = Inventario()
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            productos_dict = json.load(f)
            for id, datos in productos_dict.items():
                producto = Producto(id, datos["nombre"], datos["cantidad"], datos["precio"])
                inventario.añadir_producto(producto)
        print("Inventario cargado con éxito.")
    else:
        print("No se encontró el archivo de inventario. Se creará uno nuevo al guardar.")
    return inventario


def menu():
    inventario = cargar_inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == "5":
            inventario.mostrar_todos_los_productos()
        elif opcion == "6":
            guardar_inventario(inventario)
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
