import tkinter as tk
from tkinter import messagebox
import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_semiperimetro(self):
        return self.calcular_perimetro() / 2

    def calcular_area(self):
        s = self.calcular_semiperimetro()
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def mostrar_propiedades(self):
        perimetro = self.calcular_perimetro()
        semiperimetro = self.calcular_semiperimetro()
        area = self.calcular_area()
        return (f"Lados: {self.lado1}, {self.lado2}, {self.lado3}\n"
                f"Perímetro: {perimetro:.2f}\n"
                f"Semiperímetro: {semiperimetro:.2f}\n"
                f"Área: {area:.2f}")

class AplicacionTriangulo:
    def __init__(self, root):
        self.root = root
        self.root.title("Propiedades del Triángulo")
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

        tk.Label(frame, text="Lado 1:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_lado1 = tk.Entry(frame)
        self.entry_lado1.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Lado 2:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_lado2 = tk.Entry(frame)
        self.entry_lado2.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Lado 3:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_lado3 = tk.Entry(frame)
        self.entry_lado3.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Propiedades", command=self.calcular_propiedades_triangulo).grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_propiedades_triangulo(self):
        try:
            lado1 = float(self.entry_lado1.get())
            lado2 = float(self.entry_lado2.get())
            lado3 = float(self.entry_lado3.get())

            if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
                raise ValueError("Los lados no forman un triángulo válido.")

            triangulo = Triangulo(lado1, lado2, lado3)
            resultado = triangulo.mostrar_propiedades()
            messagebox.showinfo("Propiedades del Triángulo", resultado)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTriangulo(root)
    root.mainloop()
