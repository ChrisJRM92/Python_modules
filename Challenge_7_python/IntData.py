nombreUsuario =input("Ingrese su nombre: ")
edadUsuario = input("Ingrese su edad: ")
nombreAmigo = input("Ingrese nombre de un amigo: ")
edadAmigo = input("Ingrese edad de u amigo: ")

sumaEdades = int(edadUsuario)+int(edadAmigo)
restaEdades = int(edadUsuario)-int(edadAmigo)
print(f"La suma de las edades de {nombreUsuario} y {nombreAmigo} es {sumaEdades}")
print(f"La diferencia de las edades entre {nombreUsuario} y {nombreAmigo} es {restaEdades}")
