print("Bienvenidos a la tienda de JuCa")
cajero=input("Ingrese nombre del cajero: ")

art1=input("Ingrese articulo 1: ")
precio1=int(input("Ingrese precio: "))

art2=input("Ingrese articulo 2: ")
precio2=int(input("Ingrese precio: "))

art3=input("Ingrese articulo 3: ")
precio3=int(input("Ingrese precio: "))

art4=input("Ingrese articulo 4: ")
precio4=int(input("Ingrese precio: "))

art5=input("Ingrese articulo 5: ")
precio5=int(input("Ingrese precio: "))

print("##########TICKET##########")
subtotal=(precio1+precio2+precio3+precio4+precio5)

print("El subtotal es: ", subtotal)

total=(subtotal*1.16)
print("El total es: ",total)