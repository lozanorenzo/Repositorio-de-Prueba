#FOR IN
animales= ["gato", "perro","loro","cocodrilo"]
numeros=[5,20,30,40]

for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}" )

for numero in numeros:
    print(f"Ahora el número es: {numero}")    
    
#Iterando dos listas al mismo tiempo
#Para ello usaremos ZIP

for animal,numero in zip(animales,numeros):
    print(f"Recorriendo lista 1: {animal}")
    print(f"Recorriendo lista 2: {numero}")


#RANGE() itera desde el valor inicial hasta uno antes
for num in range(1,101):
    print(num)

#ENUMERATE() nos permite recorrer una lista retornándonos su valor e índice en forma de Tuplas

#for num in enumerate(numeros):
  #  print(num)
    
#for(i=0,1<10,i++)