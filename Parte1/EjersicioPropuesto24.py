import tkinter as tk
from tkinter import messagebox

class Esferas:
    def __init__(self, peso_a, peso_b, peso_c):
        self.peso_a = peso_a
        self.peso_b = peso_b
        self.peso_c = peso_c

    def determinar_mayor(self):
        if self.peso_a > self.peso_b and self.peso_a > self.peso_c:
            mayor = "A"
            peso = self.peso_a
        elif self.peso_b > self.peso_c:
            mayor = "B"
            peso = self.peso_b
        else:
            mayor = "C"
            peso = self.peso_c
        return mayor, peso

    def mostrar_mayor(self):
        mayor, peso = self.determinar_mayor()
        return f"La esfera de mayor peso es {mayor} con un peso de {peso:.2f}"

class AplicacionEsferas:
    def __init__(self, root):
        self.root = root
        self.root.title("Determinar Esfera de Mayor Peso")
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

        tk.Label(frame, text="Peso Esfera A:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_peso_a = tk.Entry(frame)
        self.entry_peso_a.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Peso Esfera B:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_peso_b = tk.Entry(frame)
        self.entry_peso_b.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Peso Esfera C:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_peso_c = tk.Entry(frame)
        self.entry_peso_c.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(frame, text="Determinar Mayor", command=self.calcular_mayor).grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_mayor(self):
        try:
            peso_a = float(self.entry_peso_a.get())
            peso_b = float(self.entry_peso_b.get())
            peso_c = float(self.entry_peso_c.get())

            esferas = Esferas(peso_a, peso_b, peso_c)
            resultado = esferas.mostrar_mayor()
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionEsferas(root)
    root.mainloop()
