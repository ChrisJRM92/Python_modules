import random
print("******Bienvenido******")
print("Lanzaras 2 dados y la suma de ambos valores debe ser mayor a 8 para ganar el juego")
input("Presiona enter para continuar...")
input("Presiona enter para lanzar el primer dado...")
valorDado1 = random.randint(1,6)
print(f"El valor del primer dado es: {valorDado1}")
input("Presiona enter para lanzar el segundo dado...")
valorDado2 = random.randint(1,6)
print(f"El valor del segundo dado es: {valorDado2}")
sumaDados = valorDado1+valorDado2
print(f"Ha obtenido {valorDado1} y {valorDado2}, total {sumaDados}")
if sumaDados >= 8:
    print("Te salvaste!!")

