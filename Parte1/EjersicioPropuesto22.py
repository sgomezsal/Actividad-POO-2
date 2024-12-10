import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

    def mostrar_informacion(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            return f"Nombre: {self.nombre}\nSalario mensual: ${salario_mensual:,.2f}"
        else:
            return f"Nombre: {self.nombre}"

class AplicacionSalario:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salario Mensual")
        self.centrar_ventana(400, 300)
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

        tk.Label(frame, text="Nombre del Empleado:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(frame)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Salario por Hora:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_salario_por_hora = tk.Entry(frame)
        self.entry_salario_por_hora.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Horas Trabajadas:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_horas_trabajadas = tk.Entry(frame)
        self.entry_horas_trabajadas.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Salario", command=self.calcular_salario).grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_salario(self):
        try:
            nombre = self.entry_nombre.get()
            salario_por_hora = float(self.entry_salario_por_hora.get())
            horas_trabajadas = int(self.entry_horas_trabajadas.get())

            empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
            resultado = empleado.mostrar_informacion()
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSalario(root)
    root.mainloop()
