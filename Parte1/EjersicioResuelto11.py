import tkinter as tk
from tkinter import messagebox

class MayorDeTres:
    def __init__(self, root):
        self.root = root
        self.root.title("Mayor de Tres Números")
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

        tk.Label(frame, text="Número 1:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_n1 = tk.Entry(frame)
        self.entry_n1.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Número 2:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_n2 = tk.Entry(frame)
        self.entry_n2.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Número 3:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_n3 = tk.Entry(frame)
        self.entry_n3.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Mayor", command=self.mayor_de_tres).grid(row=3, column=0, columnspan=2, pady=10)

    def mayor_de_tres(self):
        try:
            n1 = float(self.entry_n1.get())
            n2 = float(self.entry_n2.get())
            n3 = float(self.entry_n3.get())

            if n1 > n2 and n1 > n3:
                mayor = n1
            elif n2 > n3:
                mayor = n2
            else:
                mayor = n3

            resultado = f"El valor mayor entre {n1}, {n2}, y {n3} es: {mayor}"
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MayorDeTres(root)
    root.mainloop()
