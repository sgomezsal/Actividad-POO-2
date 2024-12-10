import tkinter as tk
from tkinter import messagebox
import math

class Figura:
    def calcular_area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.base**2 + self.altura**2)
        return self.base + self.altura + hipotenusa


class Rombo(Figura):
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        return 4 * self.lado


class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

class CalculadoraFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Figuras Geométricas")
        self.centrar_ventana(500, 500)
        self.crear_widgets()

    def centrar_ventana(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def crear_widgets(self):
        self.figura_seleccionada = tk.StringVar(value="Círculo")

        frame_seleccion = tk.Frame(self.root)
        frame_seleccion.pack(pady=10)

        tk.Label(frame_seleccion, text="Selecciona una figura:").grid(row=0, column=0, columnspan=2)
        figuras = ["Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo", "Rombo", "Trapecio"]
        for i, figura in enumerate(figuras):
            tk.Radiobutton(frame_seleccion, text=figura, variable=self.figura_seleccionada, value=figura,
                           command=self.actualizar_campos).grid(row=i + 1, column=0, columnspan=2)

        self.frame_inputs = tk.Frame(self.root)
        self.frame_inputs.pack(pady=10)

        self.entry_param1_label = tk.Label(self.frame_inputs, text="")
        self.entry_param1 = tk.Entry(self.frame_inputs)

        self.entry_param2_label = tk.Label(self.frame_inputs, text="")
        self.entry_param2 = tk.Entry(self.frame_inputs)

        self.entry_param3_label = tk.Label(self.frame_inputs, text="")
        self.entry_param3 = tk.Entry(self.frame_inputs)

        btn_calcular = tk.Button(self.root, text="Calcular", command=self.calcular_figura)
        btn_calcular.pack(pady=20)

        self.actualizar_campos()

    def calcular_figura(self):
        figura = self.figura_seleccionada.get()
        try:
            if figura == "Círculo":
                radio = float(self.entry_param1.get())
                figura_obj = Circulo(radio)
            elif figura == "Rectángulo":
                base = float(self.entry_param1.get())
                altura = float(self.entry_param2.get())
                figura_obj = Rectangulo(base, altura)
            elif figura == "Cuadrado":
                lado = float(self.entry_param1.get())
                figura_obj = Cuadrado(lado)
            elif figura == "Triángulo Rectángulo":
                base = float(self.entry_param1.get())
                altura = float(self.entry_param2.get())
                figura_obj = TrianguloRectangulo(base, altura)
            elif figura == "Rombo":
                diagonal_mayor = float(self.entry_param1.get())
                diagonal_menor = float(self.entry_param2.get())
                lado = float(self.entry_param3.get())
                figura_obj = Rombo(diagonal_mayor, diagonal_menor, lado)
            elif figura == "Trapecio":
                base_mayor = float(self.entry_param1.get())
                base_menor = float(self.entry_param2.get())
                altura = float(self.entry_param3.get())
                lado1 = 5  # Lado predeterminado
                lado2 = 7  # Lado predeterminado
                figura_obj = Trapecio(base_mayor, base_menor, altura, lado1, lado2)
            else:
                raise ValueError("Selecciona una figura válida.")

            resultado = (f"Área: {figura_obj.calcular_area():.2f}\n"
                         f"Perímetro: {figura_obj.calcular_perimetro():.2f}")
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def actualizar_campos(self):
        figura = self.figura_seleccionada.get()
        for widget in self.frame_inputs.winfo_children():
            widget.grid_forget()
        if figura in ["Círculo", "Cuadrado"]:
            self.entry_param1_label.config(text="Radio:" if figura == "Círculo" else "Lado:")
            self.entry_param1_label.grid(row=0, column=0)
            self.entry_param1.grid(row=0, column=1)
        elif figura in ["Rectángulo", "Triángulo Rectángulo"]:
            self.entry_param1_label.config(text="Base:")
            self.entry_param2_label.config(text="Altura:")
            self.entry_param1_label.grid(row=0, column=0)
            self.entry_param1.grid(row=0, column=1)
            self.entry_param2_label.grid(row=1, column=0)
            self.entry_param2.grid(row=1, column=1)
        elif figura == "Rombo":
            self.entry_param1_label.config(text="Diagonal Mayor:")
            self.entry_param2_label.config(text="Diagonal Menor:")
            self.entry_param3_label.config(text="Lado:")
            self.entry_param1_label.grid(row=0, column=0)
            self.entry_param1.grid(row=0, column=1)
            self.entry_param2_label.grid(row=1, column=0)
            self.entry_param2.grid(row=1, column=1)
            self.entry_param3_label.grid(row=2, column=0)
            self.entry_param3.grid(row=2, column=1)
        elif figura == "Trapecio":
            self.entry_param1_label.config(text="Base Mayor:")
            self.entry_param2_label.config(text="Base Menor:")
            self.entry_param3_label.config(text="Altura:")
            self.entry_param1_label.grid(row=0, column=0)
            self.entry_param1.grid(row=0, column=1)
            self.entry_param2_label.grid(row=1, column=0)
            self.entry_param2.grid(row=1, column=1)
            self.entry_param3_label.grid(row=2, column=0)
            self.entry_param3.grid(row=2, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraFiguras(root)
    root.mainloop()
