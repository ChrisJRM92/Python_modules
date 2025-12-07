import random

def generarFortuna():
    numeroRandom = random.randint(1, 5)
    if(numeroRandom == 1):
        print("Frase motivacional 1")
    elif(numeroRandom == 2):
        print("Frase motivacional 2")
    elif(numeroRandom == 3):
        print("Frase motivacional 3")
    elif(numeroRandom == 4):
        print("Frase motivacional 4")
    elif(numeroRandom == 5):
        print("Frase motivacional 5")
    else:
        print("Virgen santisima ingresa un numero valido por favor...")