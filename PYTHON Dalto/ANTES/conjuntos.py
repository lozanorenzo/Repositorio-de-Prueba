
#Teoría de Conjuntos
a={3}
b={1,3,5}

#Los conjuntos se pueden comparar mediante
resultado1=a.issuperset(b)
resultado2=b.issubset(a)
#DATO EXTRA para saber también si un conjunto está dentro de otro podemos usar los operadores lógicos
print(a<b)

#ISDISJOINT permite verificar si los conjuntos no comparten elementos
resultado3=a.isdisjoint(b)




