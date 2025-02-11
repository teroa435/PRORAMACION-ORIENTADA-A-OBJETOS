class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_producto_id(self):
        return self.producto_id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not any(p.get_producto_id() == producto.get_producto_id() for p in self.productos):
            self.productos.append(producto)
            print(f"Producto {producto.get_nombre()} añadido correctamente.")
        else:
            print("Error: El ID del producto ya existe.")

    def eliminar_producto(self, producto_id):
        producto = next((p for p in self.productos if p.get_producto_id() == producto_id), None)
        if producto:
            self.productos.remove(producto)
            print(f"Producto {producto.get_nombre()} eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        producto = next((p for p in self.productos if p.get_producto_id() == producto_id), None)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print(f"Producto {producto.get_nombre()} actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(f"ID: {p.get_producto_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for p in self.productos:
                print(f"ID: {p.get_producto_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
        else:
            print("No hay productos en el inventario.")


def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")


def ejecutar_menu():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                producto_id = int(input("Introduce el ID del producto: "))
                nombre = input("Introduce el nombre del producto: ")
                cantidad = int(input("Introduce la cantidad: "))
                precio = float(input("Introduce el precio: "))
                producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Por favor, introduce datos válidos.")

        elif opcion == "2":
            try:
                producto_id = int(input("Introduce el ID del producto a eliminar: "))
                inventario.eliminar_producto(producto_id)
            except ValueError:
                print("Por favor, introduce un ID válido.")

        elif opcion == "3":
            try:
                producto_id = int(input("Introduce el ID del producto a actualizar: "))
                nueva_cantidad = input("Introduce la nueva cantidad (deja en blanco si no deseas cambiarla): ")
                nuevo_precio = input("Introduce el nuevo precio (deja en blanco si no deseas cambiarlo): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Por favor, introduce datos válidos.")

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor selecciona una opción del 1 al 6.")


# Llamar a la función para ejecutar el menú
if __name__ == "__main__":
    ejecutar_menu()
