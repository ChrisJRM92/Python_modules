import tkinter as tk
def saludar():
    nombre = txtNombre.get()
    lblMensaje.config(text=f"Hola mundo mi nombre es {nombre}")
ventana = tk.Tk()
ventana.title("Bienvenido")
ventana.geometry("600x300")

lblTitle = tk.Label(text="Ingrese su nombre:").pack()
txtNombre = tk.Entry()
txtNombre.pack()
lblMensaje = tk.Label(text="")
lblMensaje.pack()
btnOk = tk.Button(text="Ok", command=saludar)
btnOk.pack()



ventana.mainloop()