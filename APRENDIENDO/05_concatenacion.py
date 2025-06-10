#nombre_de_usuario = input("Ingresa tu nombre: ")
#print("Hola",nombre_de_usuario,"!!!")

#Por default en Python la separacion de la "," es de un espacio
#Para modificar esto deberian ingresar " sep="" "y lo que pongamos entre comillas sera lo q se imprime

#EJEMPLO
#nombre_de_usuario = input("Ingresa tu nombre: ")
#print("Hola",nombre_de_usuario,"!!!",sep="")

edad_de_usuario = int(input("Ingresa tu edad: "))
saludo = "Tenes " + str(edad_de_usuario) + " años" #Cuando usemos el operador + todos van a tener q ser tratados como cadenas
print(saludo)
