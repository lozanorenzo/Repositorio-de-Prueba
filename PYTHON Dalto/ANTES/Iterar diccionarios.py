
diccionario={
    "nombre" : "Lucas",
    "apellido" : "Dalto",
    "subs" : 1000000
}

#Recorriendo el diccionario para obtener las claves
for key in diccionario:
    print(key)

#Recorriendo el diccionario con items() para obtener las claves y los valores
for datos in diccionario.items() :
    print(datos)