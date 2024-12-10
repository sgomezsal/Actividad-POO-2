import tkinter as tk
from tkinter import messagebox

class ComparadorNumeros:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparar Números")
        self.centrar_ventana(300, 200)
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

        tk.Label(frame, text="Número A:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_a = tk.Entry(frame)
        self.entry_a.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Número B:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_b = tk.Entry(frame)
        self.entry_b.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(frame, text="Comparar", command=self.comparar_numeros).grid(row=2, column=0, columnspan=2, pady=10)

    def comparar_numeros(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())

            if a > b:
                resultado = "A es mayor que B"
            elif a == b:
                resultado = "A es igual a B"
            else:
                resultado = "A es menor que B"
            
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ComparadorNumeros(root)
    root.mainloop()
