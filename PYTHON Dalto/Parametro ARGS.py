#Utilizando el parametro ARGS(*)
#Siempre debe usarse como parametro final, ya que al poseer una cantidad indefinida
# el siguiente parámetro no se tomará.
# -> Convierte al parametro en una lista con un # indefinido de elementos

#Forma optima de sumar valores (*args)
def suma(*numeros):
    resultado= sum(numeros)
    return resultado
