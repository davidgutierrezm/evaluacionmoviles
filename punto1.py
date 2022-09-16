n= int(input("Digite la cantidad de datos que desea: "))

if n > 0:
    positivos=0
    negativos=0
    nulos=0
    
    for i in range (n):
        dato = int(input("Ingrese un número: ")) 
        
        if dato > 0:
            positivos +=1
        
        elif dato < 0:
            negativos +=1
        
        else:
            nulos +=1
            
    print ("la cantidad de números pósitivos fue: ",positivos,
           "\n la cantidad de números negativos fue: ",negativos,
           "\n la cantidad de números nulos fue: ",nulos)

else:
    print ("El número ingresado no es correcto. Intentalo nuevamente")