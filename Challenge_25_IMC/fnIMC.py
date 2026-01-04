#***********FUNCION calcularIMC*******

def calcularIMC(peso, altura):
    alturaMetros = altura/100
    imc = peso/(alturaMetros*alturaMetros)
    return round(imc, 4)




#***********FUNCION interpretarIMC*******

def interpretarIMC(imc):
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


#Recibe un parámetro
#   imc: float, el valor del imc de la persona
#RETORNA un mensaje del estado de la persona en base al valor
#recibido con la tabla de ejercicios anteriores, por ejemplo
#Obesidad Grado 3, Peso Normal, etc
#IMPORTANTE: colocar bien los extremos de los rangos 

