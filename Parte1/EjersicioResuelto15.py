import tkinter as tk
from tkinter import messagebox

class CalculadoraEsfera:
    def __init__(self, root):
        self.root = root
        self.root.title("Encontrar Esfera Diferente")
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

        tk.Label(frame, text="Peso Esfera A:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_peso_a = tk.Entry(frame)
        self.entry_peso_a.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Peso Esfera B:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_peso_b = tk.Entry(frame)
        self.entry_peso_b.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Peso Esfera C:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_peso_c = tk.Entry(frame)
        self.entry_peso_c.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame, text="Peso Esfera D:").grid(row=3, column=0, padx=10, pady=5)
        self.entry_peso_d = tk.Entry(frame)
        self.entry_peso_d.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Diferente", command=self.encontrar_esfera_diferente).grid(row=4, column=0, columnspan=2, pady=10)

    def encontrar_esfera_diferente(self):
        try:
            peso_a = float(self.entry_peso_a.get())
            peso_b = float(self.entry_peso_b.get())
            peso_c = float(self.entry_peso_c.get())
            peso_d = float(self.entry_peso_d.get())

            if peso_a == peso_b == peso_c:
                diferente = "D"
                diferencia = peso_d - peso_a
            elif peso_a == peso_b == peso_d:
                diferente = "C"
                diferencia = peso_c - peso_a
            elif peso_a == peso_c == peso_d:
                diferente = "B"
                diferencia = peso_b - peso_a
            else:
                diferente = "A"
                diferencia = peso_a - peso_b

            peso_texto = "mayor" if diferencia > 0 else "menor"
            resultado = f"La esfera {diferente} es la diferente y es de {peso_texto} peso."
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraEsfera(root)
    root.mainloop()
