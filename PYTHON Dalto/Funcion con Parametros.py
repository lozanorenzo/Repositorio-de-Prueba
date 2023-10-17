#Parámetro : Son variables que se crean para usarse dentro de un fx
def saludar(nombre,sexo):
    sexo=sexo.lower()
    if sexo=="mujer":
        print(f"Hola {nombre} mi reina como estas")
    elif sexo=="varon":
        print(f"Hola {nombre} mi rey,como estas")
    else:
        print(f"Hola {nombre} amor como estas")    
        
        
saludar("Camila","mujer")
saludar("Renzo","varon")
saludar("Fran","no binario")    

#Creando una función que NO RETORNE valores
def crear_contraseña_ramdom(num):
    chars="abcdefghij"
    num_entero=str(num)
    pd=int(num_entero[0])
    c1 = pd-2
    c2 = pd
    c3 = pd-5
    
    contrasenia= f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    
    return contrasenia

mostrar=crear_contraseña_ramdom(9)

print(f"Tu nueva contraseña es: {mostrar}")