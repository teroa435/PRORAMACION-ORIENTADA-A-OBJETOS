import tkinter as tk
from tkinter import ttk, messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        # Configurar atajos de teclado
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.root.bind('<Return>', lambda e: self.add_task())
        self.root.bind('<Delete>', lambda e: self.delete_task())
        self.root.bind('d', lambda e: self.delete_task())
        self.root.bind('c', lambda e: self.complete_task())

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de tarea
        ttk.Label(main_frame, text="Nueva Tarea:").pack(anchor=tk.W)
        self.task_entry = ttk.Entry(main_frame, width=50)
        self.task_entry.pack(fill=tk.X, pady=(0, 10))
        self.task_entry.focus()

        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))

        self.add_button = ttk.Button(
            button_frame,
            text="Añadir (Enter)",
            command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT, padx=(0, 5))

        self.complete_button = ttk.Button(
            button_frame,
            text="Completar (C)",
            command=self.complete_task
        )
        self.complete_button.pack(side=tk.LEFT, padx=(0, 5))

        self.delete_button = ttk.Button(
            button_frame,
            text="Eliminar (D/Delete)",
            command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT)

        # Lista de tareas
        ttk.Label(main_frame, text="Lista de Tareas:").pack(anchor=tk.W)
        self.task_listbox = tk.Listbox(
            main_frame,
            height=15,
            selectmode=tk.SINGLE,
            activestyle='none'
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.task_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Pie de página con instrucciones
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(fill=tk.X, pady=(10, 0))

        ttk.Label(
            footer_frame,
            text="Atajos: Enter=Añadir, C=Completar, D/Eliminar=Eliminar, Esc=Salir",
            font=('Helvetica', 8)
        ).pack(side=tk.LEFT)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task_text = self.task_listbox.get(index)

            # Verificar si ya está marcada como completada
            if not task_text.startswith("✓ "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✓ {task_text}")
                self.task_listbox.itemconfig(index, {'fg': 'gray'})
            else:
                messagebox.showinfo("Información", "La tarea ya está completada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()