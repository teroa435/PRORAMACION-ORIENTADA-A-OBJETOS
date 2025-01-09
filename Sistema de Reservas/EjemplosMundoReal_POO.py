class Habitacion:
    """
    Clase que representa una habitación en el hotel.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # Ejemplo: 'simple', 'doble', 'suite'
        self.precio = precio
        self.esta_disponible = True  # Por defecto, las habitaciones están disponibles

    def reservar(self):
        """
        Marca la habitación como no disponible.
        """
        if self.esta_disponible:
            self.esta_disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"Habitación {self.numero} no está disponible.")

    def liberar(self):
        """
        Marca la habitación como disponible.
        """
        self.esta_disponible = True
        print(f"Habitación {self.numero} ahora está disponible.")

class Cliente:
    """
    Clase que representa un cliente del hotel.
    """
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Cliente: {self.nombre}, ID: {self.id_cliente}"

class SistemaReservas:
    """
    Clase que gestiona el sistema de reservas.
    """
    def __init__(self):
        self.habitaciones = []
        self.reservas = {}

    def agregar_habitacion(self, habitacion):
        """
        Agrega una nueva habitación al sistema.
        """
        self.habitaciones.append(habitacion)

    def listar_habitaciones_disponibles(self):
        """
        Lista todas las habitaciones disponibles.
        """
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.esta_disponible:
                print(f"- Habitación {habitacion.numero}, Tipo: {habitacion.tipo}, Precio: ${habitacion.precio}")

    def hacer_reserva(self, cliente, numero_habitacion):
        """
        Realiza una reserva para un cliente.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.esta_disponible:
                    habitacion.reservar()
                    self.reservas[cliente.id_cliente] = numero_habitacion
                    print(f"Reserva hecha para {cliente}.")
                    return
                else:
                    print("La habitación no está disponible.")
                    return
        print("Habitación no encontrada.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear el sistema
    sistema = SistemaReservas()

    # Agregar habitaciones
    sistema.agregar_habitacion(Habitacion(101, "simple", 50))
    sistema.agregar_habitacion(Habitacion(102, "doble", 75))
    sistema.agregar_habitacion(Habitacion(201, "suite", 120))

    # Listar habitaciones disponibles
    sistema.listar_habitaciones_disponibles()

    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", 1)

    # Hacer una reserva
    sistema.hacer_reserva(cliente1, 101)

    # Listar habitaciones disponibles nuevamente
    sistema.listar_habitaciones_disponibles()