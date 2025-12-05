import random

print("\033c")
print("*******Piedra, papel y tijera********")
print("Selecciona una opcion...")
print("Piedras: 1")
print("Papel:   2")
print("Tijera:  3")
seleccion = int(input("Opcion: "))
if(seleccion == 1):
    print("Elejiste Piedra")
elif(seleccion == 2):
    print("Elejiste Papel")
elif(seleccion == 3):
    print("Elejiste tijera")
else:
    print("Opcion invalida")

seleccionPc = random.randint(1, 3)

if(seleccionPc == 1):
    print("La pc eligio Piedra")
elif(seleccionPc == 2):
    print("La pc eligio Papel")
elif(seleccionPc == 3):
    print("La pc eligio Tijera")
else:
    print("No lo se rick, la pc debio haber elegido un numero cuantico")

if seleccion == 1 and seleccionPc == 1:
    print("Empate")
elif seleccion == 1 and seleccionPc == 2:
    print("La IA conquistara el mundo, haz perdido ante silicio muerto he inherte")
elif seleccion == 1 and seleccionPc == 3:
    print("Suerte de principiante, sometiste a la IA, Felicidades!!")

elif seleccion == 2 and seleccionPc == 1:
    print("Suerte de principiante, sometiste a la IA, Felicidades!!")
elif seleccion == 2 and seleccionPc == 2:
    print("Empate")
elif seleccion == 2 and seleccionPc == 3:
    print("La IA corta tus esperanzas, haz perdido ante silicio muerto he inherte")

elif seleccion == 3 and seleccionPc == 1:
    print("La IA corta tus esperanzas, haz perdido ante silicio muerto he inherte")
elif seleccion == 3 and seleccionPc == 2:
    print("Suerte de principiante, sometiste a la IA, Felicidades!!")
elif seleccion == 3 and seleccionPc == 3:
    print("Empate")
