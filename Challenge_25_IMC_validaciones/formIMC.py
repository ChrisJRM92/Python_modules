import tkinter as tk
import fnIMC

#*********FUNCIONES********
def btnCalcularIMC():
    peso = float(txtPeso.get())
    estatura = float(txtEstatura.get())
    imc = fnIMC.calcularIMC(peso, estatura)
    validarPeso = fnIMC.validarRangos(peso, "Error", 0, 150)
    validarEstatura = fnIMC.validarRangos(estatura, "Error", 30, 230)

    if(validarPeso == True and validarEstatura == True):
        print(validarPeso)
        print(validarEstatura)
        lblIMC.config(text=f"Su IMC es: {imc}")
        lblInterpretacion.config(text=f"{fnIMC.interpretarIMC(imc)}")
    else:
        lblErrorPeso.config(text=f"El peso debe ser entre 1 y 150 kg")
        lblErrorEstatura.config(text="La estatura debe ser entre 30 y 230 cm")
    
    

def limpiar():
    txtPeso.delete(0, tk.END)
    txtEstatura.delete(0, tk.END)
    lblInterpretacion.config(text="")
    lblIMC.config(text=f"Su IMC es:",fg="blue")
    lblErrorPeso.config(text="")
    lblErrorEstatura.config(text="")


#*********PARTE VISUAL*****
ventana=tk.Tk()
ventana.geometry("400x400")
ventana.title("imc")

lblIngresePeso=tk.Label(text="Ingrese su peso en kilos").pack()
txtPeso = tk.Entry()
txtPeso.pack()

lblErrorPeso=tk.Label(text="",fg="red")
lblErrorPeso.pack()

lblIngreseEstatura=tk.Label(text="Ingrese su estatura en centimetros").pack()
txtEstatura=tk.Entry()
txtEstatura.pack()

lblErrorEstatura=tk.Label(text="",fg="red")
lblErrorEstatura.pack()

btnIMC=tk.Button(text="CALCULAR IMC", command=btnCalcularIMC).pack()
btnLimpiar=tk.Button(text="Limpiar", command=limpiar).pack()

lblIMC=tk.Label(text=f"Su IMC es:",fg="blue")
lblIMC.pack()

lblInterpretacion=tk.Label(text="",fg="blue")
lblInterpretacion.pack()
ventana.mainloop()
