
n1=int(input("Digite un numero: "))
n2=int(input("Digite otro numero: "))
print("----------")
print("Opcion 1: Sumar")
print("Opcion 2: Restar")
print("Opcion 3: Dividir")
print("Opcion 4: Multiplicar")
suma=n1+n2
resta=n1-n2
division=n1/n2
multi=n1*n2
print("----------")
respuesta=int(input("Digite una opcion: "))

if respuesta==1:
    print(suma)
elif respuesta==2:
    print(resta)
elif respuesta==3:
    print(division)
elif respuesta==4:
    print(multi)
else:
    print("Opción Invalida")