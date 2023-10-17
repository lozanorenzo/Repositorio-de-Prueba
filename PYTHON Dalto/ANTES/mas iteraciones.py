
frutas = ["banana","manzana", "pera"]
cadena="Hola Dalto"
numeros=[2,4,6,8]

#Evitando que se coma una manzana con la secuencia CONTINUE
for fruta in frutas:
    if fruta=="manzana":
        continue
    print(f"me voy a comer una {fruta}")

#Evitando que el ciclo siga ejecutándose BREAK
for fruta in frutas:
    if fruta=="manzana":
        break
    print(f"me voy a comer una {fruta}")

#Iterando una cadena de texto (letra por letra)
for letra in cadena:
    print(letra)
    
#Duplicando todos los elementos de una lista e imprimiendolos en lista.

numeros_duplicados=[num*2 for num in numeros]
print(numeros_duplicados)