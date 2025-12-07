print("\033c")
print("**********Edades*********")
nombre = input("Cual es tu nombre: ")
edad = int(input("Cual es tu edad: "))

if(edad>0 and edad <=12):
    print("Eres un niño")
elif(edad >= 13 and edad <= 17):
    print("Eres adolecente")
elif(edad >= 18 and edad <= 30):
    print("Eres audlto joven")
elif(edad >= 31 and edad <=60):
    print("Eres adulto")
elif(edad >= 61 and edad>= 120):
    print("Eres adulto mayor")
else:
    print("No eres humano....Sospechoso -_-")