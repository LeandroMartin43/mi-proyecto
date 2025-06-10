#Desarrollar un algoritmo que permita ingresar un monto en dolares(entero). La computadora debe mostrar como pagar ese monto con la menor cantidad de billetes posibles.

monto = int(input("Ingrese el monto: "))

cant_100 = monto // 100
monto = monto % 100
print("La cantidad de billetes de 100:",cant_100)
cant_50 = monto // 50
monto = monto % 50
print("La cantidad de billetes de 50:",cant_50)
cant_20 = monto // 20
monto = monto % 20
print("La cantidad de billetes de 20:",cant_20)
cant_10 = monto // 10
monto = monto % 10
print("La cantidad de billetes de 10:",cant_10)
cant_5 = monto // 5
monto = monto % 5
print("La cantidad de billetes de 5:",cant_5)
cant_2 = monto // 2
monto = monto % 2
print("La cantidad de billetes de 2:",cant_2)
print("La cantidad de billetes de 1:",monto)