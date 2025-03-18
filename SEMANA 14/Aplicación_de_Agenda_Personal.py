import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import re


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.eventos_file = "eventos.json"

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        for col in ("Fecha", "Hora", "Descripción"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.frame_lista.grid_rowconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(0, weight=1)

        # Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada, width=30)
        self.descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(padx=10, pady=10, fill=tk.X)

        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

        self.cargar_eventos()

    def validar_hora(self, hora):
        return re.match(r"^(\d{2}):(\d{2})$", hora)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get().strip()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
            return

        if not self.validar_hora(hora):
            messagebox.showwarning("Formato Incorrecto", "La hora debe tener el formato HH:MM.")
            return

        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        self.guardar_eventos()

        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Eliminar Evento", "¿Está seguro de eliminar el evento?")
            if confirmacion:
                self.tree.delete(seleccionado)
                self.guardar_eventos()
        else:
            messagebox.showwarning("Nada Seleccionado", "Seleccione un evento para eliminar.")

    def guardar_eventos(self):
        eventos = []
        for item in self.tree.get_children():
            eventos.append(self.tree.item(item)['values'])
        with open(self.eventos_file, "w") as f:
            json.dump(eventos, f, indent=4)

    def cargar_eventos(self):
        try:
            with open(self.eventos_file, "r") as f:
                eventos = json.load(f)
                for evento in eventos:
                    self.tree.insert("", tk.END, values=evento)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
