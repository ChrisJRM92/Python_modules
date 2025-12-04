import random

print("\033c")

print("******* Bienvenidos al juego dle dia*******")
print("Regla: El jugador que saque la mayor puntuacion gana")

jugador1 = input("Ingrese el nombre del jugador 1: ")
jugador2 = input("Ingrese el nombre del jugador 2: ")

input("Jugadpor 1: Presiona enter para lanzar el dado...")
dadoJuhador1 = float(random.randint(1,6))
input("Jugadpor 2: Presiona enter para lanzar el dado...")
dadoJuhador2 = float(random.randint(1,6))

print(f"{jugador1} sacaste {dadoJuhador1}")
print(f"{jugador2} sacaste {dadoJuhador2}")

input("Presiona enter para continuar...")

if(dadoJuhador1 > dadoJuhador2):
    print(f"El ganador es: {jugador1}")
elif(jugador2 > jugador1):
    print(f"El ganador es: {jugador2}")
else:
    print("Empate..!! :D")
