contador=0
producto=[]
opcionesProducto=[]
print("***Menú***")
print("1. Registrar producto")
print("2. Mostrar producto")
print("3. Salir")

productos=[]
while(contador !=3):
    
    producto={}
    contador= int(input("Digite la opción: "))
    if (contador==1):
        producto['nombre']=input("Ingrese el nombre del producto: ")
        producto['Codigo']=input("Ingrese el código del producto: ")
        producto['precio']=int(input("Ingrese el precio: $"))
        productos.append(producto)
        print("Agregando producto: ")
    
    elif (contador==2):
        print("Mostrar producto")
        print(productos)
    elif (contador==3):
        print("salir")
        break
