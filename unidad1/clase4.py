import tkinter as tk
from tkinter import messagebox

class FreeFireGUI:
    def __init__(self, master):
        self.master = master
        master.title("Free Fire Stats v2.0")
        master.geometry("400x400")
        master.configure(bg="#2E4053")
        master.protocol("WM_DELETE_WINDOW", self.confirmar_salida)

        # Variables
        self.vida = tk.StringVar()
        self.escudo = tk.StringVar()
        self.balas = tk.StringVar()
        self.rango = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        estilo_titulo = ("Arial", 14, "bold")
        estilo_label = ("Verdana", 11)

        marco = tk.Frame(self.master, bg="#2E4053")
        marco.pack(pady=10)

        tk.Label(marco,
                 text="INGRESA LOS ATRIBUTOS",
                 font=estilo_titulo,
                 fg="#F4D03F",
                 bg="#2E4053").pack(pady=10)

        # Campo Vida (solo números)
        self.crear_campo(marco, "Vida (solo números):", self.vida, self.validar_numeros)

        # Campo Escudo (solo letras)
        self.crear_campo(marco, "Escudo (solo letras):", self.escudo, self.validar_letras)

        # Campo Balas (solo números)
        self.crear_campo(marco, "Balas (solo números):", self.balas, self.validar_numeros)

        # Campo Rango (solo letras)
        self.crear_campo(marco, "Rango (solo letras):", self.rango, self.validar_letras)

        # Botón para mostrar resultados
        tk.Button(marco,
                  text="Guardar Atributos",
                  command=self.mostrar_datos,
                  bg="#58D68D",
                  fg="white").pack(pady=10)

        # Botón de salida
        tk.Button(marco,
                  text="Salir",
                  command=self.confirmar_salida,
                  bg="#E74C3C",
                  fg="white").pack(pady=5)

    def crear_campo(self, parent, texto, variable, validacion):
        fila = tk.Frame(parent, bg="#2E4053")
        fila.pack(pady=5)
        tk.Label(fila, text=texto, font=("Verdana", 10), fg="white", bg="#2E4053").pack(side="left", padx=5)

        entrada = tk.Entry(fila, textvariable=variable, validate="key")
        entrada['validatecommand'] = (entrada.register(validacion), '%P')
        entrada.pack(side="left")

    def validar_numeros(self, texto):
        return texto.isdigit() or texto == ""

    def validar_letras(self, texto):
        return texto.isalpha() or texto == ""

    def mostrar_datos(self):
        mensaje = (
            f"Vida: {self.vida.get()}%\n"
            f"Escudo: {self.escudo.get()}\n"
            f"Balas: {self.balas.get()}\n"
            f"Rango: {self.rango.get()}"
        )
        messagebox.showinfo("Atributos Guardados", mensaje)

    def confirmar_salida(self):
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FreeFireGUI(root)
    root.mainloop()
