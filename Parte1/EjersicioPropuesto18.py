import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion_fuente = retencion_fuente

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (1 - self.retencion_fuente / 100)

    def mostrar_informacion(self):
        salario_bruto = self.calcular_salario_bruto()
        salario_neto = self.calcular_salario_neto()
        return (f"Código: {self.codigo}\n"
                f"Nombres: {self.nombres}\n"
                f"Salario Bruto: ${salario_bruto:,.2f}\n"
                f"Salario Neto: ${salario_neto:,.2f}")

class AplicacionEmpleado:
    def __init__(self, root):
        self.root = root
        self.root.title("Información del Empleado")
        self.centrar_ventana(450, 350)
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

        tk.Label(frame, text="Código:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_codigo = tk.Entry(frame)
        self.entry_codigo.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nombres = tk.Entry(frame)
        self.entry_nombres.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Horas Trabajadas:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_horas_trabajadas = tk.Entry(frame)
        self.entry_horas_trabajadas.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame, text="Valor por Hora:").grid(row=3, column=0, padx=10, pady=5)
        self.entry_valor_hora = tk.Entry(frame)
        self.entry_valor_hora.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame, text="Retención (%)").grid(row=4, column=0, padx=10, pady=5)
        self.entry_retencion_fuente = tk.Entry(frame)
        self.entry_retencion_fuente.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Información", command=self.calcular_informacion_empleado).grid(row=5, column=0, columnspan=2, pady=10)

    def calcular_informacion_empleado(self):
        try:
            codigo = self.entry_codigo.get()
            nombres = self.entry_nombres.get()
            horas_trabajadas = int(self.entry_horas_trabajadas.get())
            valor_hora = float(self.entry_valor_hora.get())
            retencion_fuente = float(self.entry_retencion_fuente.get())

            empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente)
            resultado = empleado.mostrar_informacion()
            messagebox.showinfo("Información del Empleado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionEmpleado(root)
    root.mainloop()
