import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Función para agregar datos a la lista
def agregar_dato():
    dato = campo_texto.get()  # Obtener el texto del campo de entrada
    if dato:  # Verificar que el campo no esté vacío
        lista_datos.insert(tk.END, dato)  # Agregar el dato a la lista
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un dato antes de agregar.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Borrar todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño de la ventana

# Crear y colocar los componentes en la ventana

# Etiqueta (Label)
etiqueta = tk.Label(ventana, text="Ingresa un dato:")
etiqueta.pack(pady=10)

# Campo de texto (Entry)
campo_texto = tk.Entry(ventana, width=30)
campo_texto.pack(pady=10)

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos (Listbox)
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
