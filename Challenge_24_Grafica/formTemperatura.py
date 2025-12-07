import tkinter as tk 
import fnTemperatura

#########funciones
def btnConvertirF():
    centrigrados=float(txtCentigrados.get())
    farenheit = fnTemperatura.convertirFarenheit(centrigrados)
    lblResultado.config(text=f"{centrigrados}ºC son: {farenheit}F")

#########parte visual
ventana=tk.Tk()
ventana.geometry("300x300")
ventana.title("CONVERTIDOR TEMPERATURA")

lblIngreseCentigrados=tk.Label(text="Ingrese la temperatura en Grados Centigrados")
lblIngreseCentigrados.pack()

txtCentigrados=tk.Entry()
txtCentigrados.pack()

btnConvertir=tk.Button(text="CONVERTIR A FARENHEIT", command=btnConvertirF)
btnConvertir.pack()

lblResultado=tk.Label(text="...")
lblResultado.pack()

ventana.mainloop()