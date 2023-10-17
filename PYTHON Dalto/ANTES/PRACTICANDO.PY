#Si en promedio una persona dice una palabra cada dos egundos
frase=input("Escriba una frase: ")


#PREMISA A
#Necesito separar el string ingresado en palabras
separando_por_espacios=frase.split( )

#Contando el número de palabras -> uso len() para contar el # de elementos de una lista
numero_de_palabras=len(separando_por_espacios)

#Calculando el tiempo en decir las palabras
tiempo_necesario=(numero_de_palabras/2)

print(f"Usted dijo {numero_de_palabras} palabras en {tiempo_necesario} segundo(s)")

#PREMISA B
if tiempo_necesario>60:
    print("Para falco no te pedí un testamento")
    
#PREMISA C
tiempo_de_dalto=(numero_de_palabras*0.7/2)
print(f"Dalto lo diría en: {tiempo_de_dalto} segundo(s)")

