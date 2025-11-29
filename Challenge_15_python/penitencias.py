import random
penitencia_1="Tienes que cantar"
penitencia_2="Tienes que bailar"
penitencia_3="Tienes que contar un chiste"
penitencia_4="Tienes que hacer muecas"
penitencia_5="Tienes que contar una adivinanza"
penitencia_6="Tienes que crear una rest api para consumir data desde el front con spring boot y reglas de seguridad"
print("-----Bienvenidos al juego de penitencias----")
print("Por cada numero que obtengas al lanzar el dado tendras que relizar la penitnecia asignada")
input("Presiona enter para lanzar el dado...")
numeroDado = random.randint(1,6)
print(f"Tu numero es: {numeroDado}")
if numeroDado == 1:
    print(penitencia_1)
elif numeroDado == 2:
    print(penitencia_2)
elif numeroDado == 3:
    print(penitencia_3)
elif numeroDado == 4:
    print(penitencia_4)
elif numeroDado == 5:
    print(penitencia_5)
else:
    print(penitencia_6)