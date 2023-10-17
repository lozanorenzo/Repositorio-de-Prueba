#ENUMERATE() nos permite recorrer una lista retornándonos su valor e índice en forma de Tuplas
numeros=[56,16,14,72]

for num in enumerate(numeros):
  indice=num[0]
  valor=num[1]
  print(f"El índice es: {indice} y su valor es: {valor} ")