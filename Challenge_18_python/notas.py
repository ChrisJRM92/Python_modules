print("\033c")
print("*********Notas*********")
nota1 = float(input("Ingresa una nota del 1 - 10: "))
faltas = 0;
if(nota1 >= 1 and nota1 <= 10):
    print("Nota valida...")
    faltas = int(input("Cuantas veces haz faltadop a las clases: "))
    if(faltas < 3 and nota1 >= 8):
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Solo se permiten notas entre 1 - 10")
