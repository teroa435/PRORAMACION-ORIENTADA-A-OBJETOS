import tkinter as tk
from tkinter import ttk, messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")
        self.style.configure("Completed.TLabel", foreground="#888", font=('Arial', 10, 'overstrike'))

        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de nueva tarea
        self.task_entry = ttk.Entry(self.main_frame, font=('Arial', 12))
        self.task_entry.pack(fill=tk.X, pady=5)
        self.task_entry.bind("<Return>", self.add_task)
        self.task_entry.focus_set()

        # Botones
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=5)

        self.add_button = ttk.Button(self.button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = ttk.Button(self.button_frame, text="Marcar Completada", command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.task_list = tk.Listbox(
            self.main_frame,
            font=('Arial', 12),
            selectbackground="#a6a6a6",
            selectmode=tk.SINGLE,
            height=15
        )
        self.task_list.pack(fill=tk.BOTH, expand=True, pady=5)
        self.task_list.bind("<Double-Button-1>", self.mark_completed)  # Doble clic para marcar

        # Estado de las tareas
        self.tasks = []

    def add_task(self, event=None):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def mark_completed(self, event=None):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()

    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.task_list.insert(tk.END, task["text"])
                self.task_list.itemconfig(tk.END, {'fg': '#888888', 'selectforeground': '#888888'})
            else:
                self.task_list.insert(tk.END, task["text"])


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
