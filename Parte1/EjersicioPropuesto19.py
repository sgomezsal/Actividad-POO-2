import tkinter as tk
from tkinter import messagebox
import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (self.lado * math.sqrt(3)) / 2

    def calcular_area(self):
        altura = self.calcular_altura()
        return (self.lado * altura) / 2

    def mostrar_propiedades(self):
        perimetro = self.calcular_perimetro()
        altura = self.calcular_altura()
        area = self.calcular_area()
        return (f"Lado: {self.lado}\n"
                f"Perímetro: {perimetro:.2f}\n"
                f"Altura: {altura:.2f}\n"
                f"Área: {area:.2f}")

class AplicacionTriangulo:
    def __init__(self, root):
        self.root = root
        self.root.title("Propiedades del Triángulo Equilátero")
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

        tk.Label(frame, text="Lado del Triángulo:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_lado = tk.Entry(frame)
        self.entry_lado.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Propiedades", command=self.calcular_propiedades_triangulo).grid(row=1, column=0, columnspan=2, pady=10)

    def calcular_propiedades_triangulo(self):
        try:
            lado = float(self.entry_lado.get())
            triangulo = TrianguloEquilatero(lado)
            resultado = triangulo.mostrar_propiedades()
            messagebox.showinfo("Propiedades del Triángulo", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un valor válido para el lado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTriangulo(root)
    root.mainloop()
