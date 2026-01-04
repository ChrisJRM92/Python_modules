import tkinter as tk
import fnIMC

#*********FUNCIONES********
def btnCalcularIMC():
    peso = float(txtPeso.get())
    estatura = float(txtEstatura.get())
    imc = fnIMC.calcularIMC(peso, estatura)
    lblIMC.config(text=f"Su IMC es: {imc}")
    lblInterpretacion.config(text=f"{fnIMC.interpretarIMC(imc)}") 



#*********PARTE VISUAL*****
ventana=tk.Tk()
ventana.geometry("400x400")
ventana.title("imc")

lblIngresePeso=tk.Label(text="Ingrese su peso en kilos").pack()
txtPeso = tk.Entry()
txtPeso.pack()

lblErrorPeso=tk.Label(text="",fg="red").pack()

lblIngreseEstatura=tk.Label(text="Ingrese su estatura en centimetros").pack()
txtEstatura=tk.Entry()
txtEstatura.pack()

lblErrorEstatura=tk.Label(text="",fg="red").pack()

btnIMC=tk.Button(text="CALCULAR IMC", command=btnCalcularIMC).pack()

lblIMC=tk.Label(text=f"Su IMC es:",fg="blue")
lblIMC.pack()

lblInterpretacion=tk.Label(text="",fg="blue")
lblInterpretacion.pack()
ventana.mainloop()
