class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios
        self.usuarios = {}  # Diccionario con ID de usuario como clave

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido correctamente.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado correctamente.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return
        libro = self.libros_disponibles[isbn]
        self.usuarios[id_usuario].libros_prestados.append(libro)
        del self.libros_disponibles[isbn]
        print(f"Libro '{libro.titulo}' prestado a '{self.usuarios[id_usuario].nombre}'.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        usuario = self.usuarios[id_usuario]
        libro_devuelto = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_devuelto = libro
                break
        if libro_devuelto:
            usuario.libros_prestados.remove(libro_devuelto)
            self.libros_disponibles[isbn] = libro_devuelto
            print(f"Libro '{libro_devuelto.titulo}' devuelto por '{usuario.nombre}'.")
        else:
            print(f"El libro con ISBN {isbn} no fue prestado a este usuario.")

    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros_disponibles.values() if titulo.lower() in libro.titulo.lower()]
        return resultados

    def buscar_libro_por_autor(self, autor):
        resultados = [libro for libro in self.libros_disponibles.values() if autor.lower() in libro.autor.lower()]
        return resultados

    def buscar_libro_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros_disponibles.values() if categoria.lower() in libro.categoria.lower()]
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print(f"El usuario '{usuario.nombre}' no tiene libros prestados.")
        else:
            print(f"Libros prestados a '{usuario.nombre}':")
            for libro in usuario.libros_prestados:
                print(libro)


# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9788437604947")
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "9780451524935")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("001", "9788437604947")
biblioteca.prestar_libro("002", "9780451524935")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")
biblioteca.listar_libros_prestados("002")

# Devolver libros
biblioteca.devolver_libro("001", "9788437604947")
biblioteca.devolver_libro("002", "9780451524935")

# Buscar libros
print("\nBúsqueda por título '1984':")
for libro in biblioteca.buscar_libro_por_titulo("1984"):
    print(libro)

print("\nBúsqueda por autor 'Gabriel García Márquez':")
for libro in biblioteca.buscar_libro_por_autor("Gabriel García Márquez"):
    print(libro)

print("\nBúsqueda por categoría 'Ciencia Ficción':")
for libro in biblioteca.buscar_libro_por_categoria("Ciencia Ficción"):
    print(libro)

# Dar de baja usuario
biblioteca.dar_de_baja_usuario("001")
