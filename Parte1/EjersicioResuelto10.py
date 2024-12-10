import tkinter as tk
from tkinter import messagebox


class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago(self):
        pago = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            pago += 0.03 * self.patrimonio
        return pago

    def mostrar_informacion(self):
        return f"El estudiante con número de inscripción {self.numero_inscripcion} y nombre {self.nombres} debe pagar: ${self.calcular_pago():,.0f}"


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pago de Estudiantes")
        self.centrar_ventana(400, 250)
        self.crear_widgets()

    def centrar_ventana(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Número de Inscripción:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_inscripcion = tk.Entry(frame)
        self.entry_inscripcion.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(frame)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_patrimonio = tk.Entry(frame)
        self.entry_patrimonio.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame, text="Estrato:").grid(row=3, column=0, padx=10, pady=5)
        self.entry_estrato = tk.Entry(frame)
        self.entry_estrato.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Pago", command=self.agregar_estudiante).grid(row=4, column=0, columnspan=2, pady=10)

    def agregar_estudiante(self):
        try:
            numero_inscripcion = self.entry_inscripcion.get()
            nombres = self.entry_nombre.get()
            patrimonio = float(self.entry_patrimonio.get())
            estrato = int(self.entry_estrato.get())

            estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)
            resultado = estudiante.mostrar_informacion()
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en los campos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
