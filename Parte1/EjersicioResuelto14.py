import tkinter as tk
from tkinter import messagebox

class CalculadoraSalarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salarios")
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

        tk.Label(frame, text="Ventas Depto. 1:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_vd1 = tk.Entry(frame)
        self.entry_vd1.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Ventas Depto. 2:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_vd2 = tk.Entry(frame)
        self.entry_vd2.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Ventas Depto. 3:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_vd3 = tk.Entry(frame)
        self.entry_vd3.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame, text="Salario Base:").grid(row=3, column=0, padx=10, pady=5)
        self.entry_salario_base = tk.Entry(frame)
        self.entry_salario_base.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Salarios", command=self.calcular_salarios).grid(row=4, column=0, columnspan=2, pady=10)

    def calcular_salarios(self):
        try:
            vd1 = float(self.entry_vd1.get())
            vd2 = float(self.entry_vd2.get())
            vd3 = float(self.entry_vd3.get())
            salario_base = float(self.entry_salario_base.get())

            total_ventas = vd1 + vd2 + vd3
            porcentaje_ventas = 0.33 * total_ventas

            salar1 = salario_base + 0.2 * salario_base if vd1 > porcentaje_ventas else salario_base
            salar2 = salario_base + 0.2 * salario_base if vd2 > porcentaje_ventas else salario_base
            salar3 = salario_base + 0.2 * salario_base if vd3 > porcentaje_ventas else salario_base

            resultado = (
                f"Salario vendedores Depto. 1: ${salar1:,.2f}\n"
                f"Salario vendedores Depto. 2: ${salar2:,.2f}\n"
                f"Salario vendedores Depto. 3: ${salar3:,.2f}"
            )
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraSalarios(root)
    root.mainloop()
