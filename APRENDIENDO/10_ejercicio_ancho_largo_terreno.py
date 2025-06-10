# Desarrollar un programa que permita ingresar el ancho y el largo de un terreno (En metros) y
# el precio del metro cuadado de tierra. La computadora debe calcular y mostrar el precio del terreno
# y la cantidad de metros de alambre que habria que comprar para cerrcarlo en tres pasadas.

ancho = int(input("Ingresa el ancho del terreno: "))
largo = int(input("Ingresa el largo del terreno: "))
precio_m2 = float(input("Ingrese precio del terreno: "))

cant_pasadas = 3
superficie = ancho * largo 
precio_terreno = superficie * precio_m2

perimetro = 2 * ancho + 2 * largo
cant_alambre = perimetro * cant_pasadas

print("El precio del terreno es de USD",precio_terreno)
print("Cantidad de metros para",cant_pasadas,"pasadas es de",cant_alambre,"metros")
