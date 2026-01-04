import tkinter as tk
import utilitariosImagen


def encenderPC():
    img = utilitariosImagen.obtenerImagen("compuPrendida.PNG")
    lblImagen.config(image=img)
    lblImagen.image = img
    btnEncender.config(state="disabled")
    btnApagar.config(state="normal")

def apagarPC():
    img = utilitariosImagen.obtenerImagen("compuApagada.PNG")
    lblImagen.config(image=img)
    lblImagen.image = img
    btnApagar.config(state="disabled")
    btnEncender.config(state="normal")

ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("Mi formulario")

imgApagar = utilitariosImagen.obtenerImagen("compuApagada.PNG")
lblImagen = tk.Label(image=imgApagar)
lblImagen.pack()

btnEncender = tk.Button(text="Encender PC", command=encenderPC, state="normal")
btnEncender.pack()

btnApagar = tk.Button(text="Apagar PC", command=apagarPC, state="disabled")
btnApagar.pack()

ventana.mainloop()

