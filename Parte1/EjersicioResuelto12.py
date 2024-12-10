import tkinter as tk
from tkinter import messagebox

class CalculadoraSalario:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salario")
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

        tk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(frame)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Horas Trabajadas:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_horas = tk.Entry(frame)
        self.entry_horas.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Valor por Hora:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_valor_hora = tk.Entry(frame)
        self.entry_valor_hora.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Salario", command=self.calcular_salario).grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_salario(self):
        try:
            nombre = self.entry_nombre.get()
            horas_trabajadas = int(self.entry_horas.get())
            valor_hora = float(self.entry_valor_hora.get())

            if horas_trabajadas > 40:
                horas_extras = horas_trabajadas - 40
                if horas_extras > 8:
                    extras_triples = horas_extras - 8
                    salario = 40 * valor_hora + 16 * valor_hora + extras_triples * 3 * valor_hora
                else:
                    salario = 40 * valor_hora + horas_extras * 2 * valor_hora
            else:
                salario = horas_trabajadas * valor_hora

            resultado = f"El trabajador {nombre} devengó: ${salario:,.2f}"
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraSalario(root)
    root.mainloop()
