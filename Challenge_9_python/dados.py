import random
print("******Prueba tu suerte*******")
print("Reglas: Si el valor lanzado es mayor a 3 ganas el juego")
input("Presiona enter para lanzar el dado...")
valorDado = random.randint(1,6)
print(f"Tu valor es: {valorDado}")

if valorDado > 3:
    print("Ganaste felcitaciones!!")
    print("Estas de suerte")

