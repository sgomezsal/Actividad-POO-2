import tkinter as tk
from tkinter import messagebox


class CalculadoraDescuento:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Valor a Pagar")
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

        tk.Label(frame, text="Valor de Compra:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_valor_compra = tk.Entry(frame)
        self.entry_valor_compra.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Color de la Bolita:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_color_bolita = tk.Entry(frame)
        self.entry_color_bolita.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(frame, text="Calcular Valor", command=self.calcular_valor_pago).grid(row=2, column=0, columnspan=2, pady=10)

    def calcular_valor_pago(self):
        try:
            valor_compra = float(self.entry_valor_compra.get())
            color_bolita = self.entry_color_bolita.get()

            descuentos = {
                "BLANCO": 0,
                "VERDE": 10,
                "AMARILLO": 25,
                "AZUL": 50,
                "ROJO": 100
            }
            descuento = descuentos.get(color_bolita.upper(), 0)
            valor_a_pagar = valor_compra - (valor_compra * descuento / 100)

            resultado = f"El cliente debe pagar: ${valor_a_pagar:,.2f}"
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraDescuento(root)
    root.mainloop()
