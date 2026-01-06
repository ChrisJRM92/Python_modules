def buscarEstudiante(cedula, listaEstudiante):
    for est in listaEstudiante:
        partesEstudiantes = est.split("#")
        if partesEstudiantes[0] == cedula:
            return partesEstudiantes
    return None

def calcularTotal(n1,n2, n3, faltas):
    n4 = 0
    if faltas == 0:
        n4 = 10
    elif faltas >=1 and faltas < 4:
        n4 = 9
    elif faltas >= 4 and faltas <= 5:
        n4 = 8
    elif faltas > 5:
        n4 = 7
    else:
        n4 = 0
    return (n1+n2+n3+n4)/4


def calcularPromedioCurso(estudiantes):
    totalSuma = 0

    for estudiante in estudiantes:
        partes = estudiante.split("#")
        notaTotal = float(partes[7])
        totalSuma += notaTotal

    promedio = totalSuma / len(estudiantes)
    return round(promedio, 4)

