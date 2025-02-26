import tkinter as tk
from tkinter import messagebox

class FreeFireGUI:
    def __init__(self, master):
        self.master = master
        master.title("Free Fire Stats v2.0")
        master.geometry("400x300")
        master.configure(bg="#2E4053")
        
        # Configurar protocolo de cierre
        master.protocol("WM_DELETE_WINDOW", self.confirmar_salida)
        
        # Atributos del juego
        self.stats = {
            "Vida": tk.StringVar(value="❤️ 100%"),
            "Escudo": tk.StringVar(value="🛡️ Nivel 3"),
            "Balas": tk.StringVar(value="🔸 250"),
            "Rango": tk.StringVar(value="⭐ Oro II")
        }
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Estilos
        estilo_titulo = ("Arial", 14, "bold")
        estilo_stats = ("Verdana", 12)
        
        # Marco principal
        marco = tk.Frame(self.master, bg="#2E4053")
        marco.pack(pady=20)
        
        # Título
        tk.Label(marco, 
                text="EATRIBUTOS FREE FIRE",
                font=estilo_titulo,
                fg="#F4D03F",
                bg="#2E4053").pack(pady=10)
        
        # Mostrar stats
        for stat, valor in self.stats.items():
            fila = tk.Frame(marco, bg="#2E4053")
            fila.pack(pady=5)
            
            tk.Label(fila, 
                    text=f"{stat}:",
                    font=estilo_stats,
                    fg="white",
                    bg="#2E4053").pack(side="left", padx=10)
            
            tk.Label(fila, 
                    textvariable=valor,
                    font=estilo_stats,
                    fg="#58D68D",
                    bg="#2E4053").pack(side="left")
        
        # Botón de salida
        tk.Button(self.master, 
                 text="Salir",
                 command=self.confirmar_salida,
                 bg="#E74C3C",
                 fg="white").pack(pady=20)
    
    def confirmar_salida(self):
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FreeFireGUI(root)
    root.mainloop()
