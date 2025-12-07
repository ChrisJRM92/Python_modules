from datetime import datetime

def determinarResultadosIMC(imc):
    if(imc >= 0 and imc <=16):
        return "Delgadez severa"
    elif(imc >= 16 and imc <= 17):
        return "Delgadez moderada"
    elif(imc >= 17 and imc<=18.5):
        return "Delgadez leve"
    elif(imc >= 18.5 and imc <= 25):
        return "Peso normal"
    elif(imc >= 25 and imc <=30):
        return "Sobrepeso"
    elif(imc >= 30 and imc <= 35):
        return "Obesidad grado 1"
    elif(imc >= 35 and imc <= 40):
        return "Obesidad grado 2"
    elif(imc >= 40):
        return ("Obesidad grado 3")
    else:
        return ("IMC Fuera de rango")
    
def encontrarMayor(valor1, valor2, valor3):
    mayorActual = valor1
    if valor2 > mayorActual:
        mayorActual = valor2
    if valor3 > mayorActual:
        mayorActual = valor3
    return mayorActual
    
def encontrarMenor(valor1, valor2, valor3, valor4):
    menorActual = valor1
    if(valor2 < menorActual):
        menorActual = valor2
    if(valor3 < menorActual):
        menorActual = valor3
    if(valor4 < menorActual):
        menorActual = valor4
    return menorActual

def calcularEdad(anioNacimiento):
    anioActual = datetime.now().year
    if(anioNacimiento >0 and anioNacimiento <= anioActual):
        return anioActual-anioNacimiento
    else:
        return -1
def calcularCuota(monto, interesAnual, numeroMeses):
    interesMensual = (interesAnual / 12) / 100
    cuotaMensual = (monto * interesMensual) / (1 - (1 + interesMensual)**(-numeroMeses))
    return cuotaMensual


