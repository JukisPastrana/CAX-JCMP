print("Bienvenidos a la tienda de Juca!")
print("Ingrese su nombre: ")
nombre=input()
print("Hola, bienvenido a la tienda de JuCa")
print("Articulos en venta: ")
print("Papas")
print("Refresco")
print("Servilletas")
print("Chelas")
print("Hielos")
print("Clamato")
print("Chamoy")
print("Agua")
print("Bacardi")
print("Vasos")


while True:
  a=input("Ingrese el articulo que quiera comprar: ")
  if(a=="Papas"):
    print("Las papas cuestan $15")
    costo= 15
  if(a=="Refresco"):
    print("El Refresco cuesta $13")
    costo=13
  if(a=="Servilletas"):
    print("Las Servilletas cuestan $20")
    costo=20
  if(a=="Chelas"):
    print("Las Chelas cuestan $40")
    costo=40
  if(a=="Hielos"):
    print("Los Hielos cuestan $56")
    costo=56
  if(a=="Clamato"):
    print("El Clamato cuesta $38")
    costo=38
  if(a=="Chamoy"):
    print("El Chamoy cuesta $19")
    costo=19
  if(a=="Agua"):
    print("El Agua cuesta $10")
    costo=10
  if(a=="Bacardi"):
    print("El Bacardi cuesta $199")
    costo=199
  if(a=="Vasos"):
    print("Los vasos cuestan $35")
    costo=35

  a=input("Ingrese el otro articulo que quiera comprar: ")
  if(a=="Papas"):
    print("Las papas cuestan $15")
    costo2= 15
  if(a=="Refresco"):
    print("El Refresco cuesta $13")
    costo2=13
  if(a=="Servilletas"):
    print("Las Servilletas cuestan $20")
    costo2=20
  if(a=="Chelas"):
    print("Las Chelas cuestan $40")
    costo2=40
  if(a=="Hielos"):
    print("Los Hielos cuestan $56")
    costo2=56
  if(a=="Clamato"):
    print("El Clamato cuesta $38")
    costo2=38
  if(a=="Chamoy"):
    print("El Chamoy cuesta $19")
    costo2=19
  if(a=="Agua"):
    print("El Agua cuesta $10")
    costo2=10
  if(a=="Bacardi"):
    print("El Bacardi cuesta $199")
    costo2=199
  if(a=="Vasos"):
    print("Los vasos cuestan $35")
    costo2=35
  print("Total: ", (costo+costo2))