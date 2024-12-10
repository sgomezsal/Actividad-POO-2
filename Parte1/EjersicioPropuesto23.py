import tkinter as tk
from tkinter import messagebox
import math

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_soluciones(self):
        discriminante = self.b ** 2 - 4 * self.a * self.c

        if discriminante > 0:
            x1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return x1, x2
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return x,
        else:
            parte_real = -self.b / (2 * self.a)
            parte_imaginaria = math.sqrt(-discriminante) / (2 * self.a)
            return (parte_real + parte_imaginaria * 1j, parte_real - parte_imaginaria * 1j)

    def mostrar_soluciones(self):
        soluciones = self.calcular_soluciones()
        if len(soluciones) == 2:
            return f"Las soluciones son: {soluciones[0]:.2f} y {soluciones[1]:.2f}"
        elif len(soluciones) == 1:
            return f"La única solución es: {soluciones[0]:.2f}"
        else:
            return f"Las soluciones complejas son: {soluciones[0]} y {soluciones[1]}"

class AplicacionEcuacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Ecuación de Segundo Grado")
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

        tk.Label(frame, text="Coeficiente a:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_a = tk.Entry(frame)
        self.entry_a.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Coeficiente b:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_b = tk.Entry(frame)
        self.entry_b.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Coeficiente c:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_c = tk.Entry(frame)
        self.entry_c.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Soluciones", command=self.calcular_soluciones).grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_soluciones(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())

            if a == 0:
                raise ValueError("El coeficiente 'a' no puede ser 0 para una ecuación de segundo grado.")

            ecuacion = EcuacionSegundoGrado(a, b, c)
            resultado = ecuacion.mostrar_soluciones()
            messagebox.showinfo("Resultado", resultado)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionEcuacion(root)
    root.mainloop()
