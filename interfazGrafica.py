import tkinter as tk
from tkinter import ttk

def calcularSumaDados():
    dado1 = 0
    dado2 = 0
    try:
        dado1 = int(input_dado1.get())
        if dado1 < 1 or dado1 > 6:
            raise ValueError("El valor debe estar entre 1 y 6")
        etiqueta_error_dado1.config(text="")
    except ValueError:
        etiqueta_error_dado1.config(text="Introduce un número entre 1 y 6")
    
    try:
        dado2 = int(input_dado2.get())
        if dado2 < 1 or dado2 > 6:
            raise ValueError("El valor debe estar entre 1 y 6")
        etiqueta_error_dado2.config(text="")
    except ValueError:
        etiqueta_error_dado2.config(text="Introduce un número entre 1 y 6")
    
    if 1 <= dado1 <= 6 and 1 <= dado2 <= 6:
        suma = dado1 + dado2
        etiqueta_resultado.config(text=f"La suma de los dados es: {suma}")
    else:
        etiqueta_resultado.config(text="")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Suma de Dados")
ventana.config(width=600, height=200)

# Etiquetas y entradas para los valores de los dados
etiqueta_dado1 = ttk.Label(text="Introduce el valor del dado 1 (1-6):")
etiqueta_dado1.place(x=10, y=10)
input_dado1 = ttk.Entry()
input_dado1.place(x=200, y=10, width=50)
etiqueta_error_dado1 = ttk.Label(text="", foreground="red")
etiqueta_error_dado1.place(x=270, y=10)

etiqueta_dado2 = ttk.Label(text="Introduce el valor del dado 2 (1-6):")
etiqueta_dado2.place(x=10, y=50)
input_dado2 = ttk.Entry()
input_dado2.place(x=200, y=50, width=50)
etiqueta_error_dado2 = ttk.Label(text="", foreground="red")
etiqueta_error_dado2.place(x=270, y=50)

# Botón para calcular la suma
boton_calcular = ttk.Button(text="Calcular Suma", command=calcularSumaDados)
boton_calcular.place(x=100, y=90)

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(text="")
etiqueta_resultado.place(x=10, y=130)

ventana.mainloop()
