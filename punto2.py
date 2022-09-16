print("**Salpicones Davilexis Bienvenido**")

frutas=[]

for i in range(10):
    fruta={}
    fruta['nombre']=input(f'Ingrese el nombre de la fruta: ')
    fruta['color']=input(f'Ingrese el color de la fruta: ')
    fruta['precio']=input(f'Ingrese el precio de la fruta: ')
    frutas.append(fruta)
    
print(frutas)