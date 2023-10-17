numero_de_alvaro=int(input("Álvaro - Me salió: "))
numero_de_barbara=int(input("Bárbara - A mi me tocó: "))

if 1<=numero_de_alvaro & numero_de_barbara<=6 :
    if numero_de_alvaro>numero_de_barbara :
        print("Felicidades Álvaro, ganaste")
    elif numero_de_barbara>numero_de_alvaro:
        print("Felicidades Bárbara, ganaste")
    else:
        ("EMPATARON")
elif (numero_de_barbara>6 or numero_de_barbara<1 ) & (numero_de_alvaro>6 or numero_de_alvaro<1 ) :
    print("Ambos están mintiendo")
elif numero_de_barbara>6 or numero_de_barbara<1 :
    print("Bárbara no mientas")
    
elif numero_de_alvaro>6 or numero_de_alvaro<1 :
    print("Álvaro no mientas")
