class FileManager:
    def __init__(self, filename):
        """
        Constructor que inicializa el objeto con el nombre del archivo
        y abre el archivo en modo escritura.
        """
        self.filename = filename
        self.file = open(filename, 'w')
        print(f"Archivo {self.filename} abierto correctamente.")

    def write_data(self, data):
        """
        Método para escribir datos en el archivo.
        """
        self.file.write(data + '\n')
        print(f"Datos escritos en {self.filename}.")

    def __del__(self):
        """
        Destructor que cierra el archivo cuando el objeto se destruye.
        """
        self.file.close()
        print(f"Archivo {self.filename} cerrado correctamente.")


# Uso de la clase
if __name__ == "__main__":
    manager = FileManager("example.txt")
    manager.write_data("Hola, mundo!")
    manager.write_data("Python es genial!")

    # Eliminamos manualmente el objeto para llamar al destructor
    del manager

    # Confirmación de finalización del programa
    print("Programa finalizado.")
