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
    print("Elejiste Tijera")
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

#Difinir ganador
if (seleccion == seleccionPc):
    print("Empates")
if (seleccion == 1 and seleccionPc == 3) or (seleccion == 2 and seleccionPc == 1) or (seleccion == 3 and seleccionPc == 2):
    print("Exito, haz ganado!!!")
if(seleccionPc == 1 and seleccion == 3) or (seleccionPc == 2 and seleccion == 1) or (seleccionPc == 3 and seleccion == 2):
    print("El silicio inherte te ha derrotado")