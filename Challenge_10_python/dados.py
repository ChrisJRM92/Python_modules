import random
print("******Prueba tu suerte*******")
print("Reglas: Si el valor lanzado es igual a 6 ganas el juego")
input("Presiona enter para lanzar el dado...")
valorDado = random.randint(1,6)
print(f"Tu valor es: {valorDado}")

if valorDado == 6:
    print("Ganaste felcitaciones!!")
    print("Estas de suerte")

