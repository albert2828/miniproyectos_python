# Madlibs (o historias locas) es un juego sobre completar una frase 
# (desconocida al jugador) con información que se pide

def main():
    print(40*"=")
    print(" ¡Bienvenido al juego! \nIntroduce con el teclado lo siguiente")
    print(40*"=")

    verbo1 = input("Un verbo (por ejemplo 'escribir'): ")
    verbo2 = input("Un verbo (por ejemplo 'jugar'): ")
    adjetivo = input("Un sustantivo (por ejemplo 'divertido'): ")

    madlib = f"Hoy quería {verbo1} una historia, pero en lugar de eso, "
    madlib += f"me puse a {verbo2}. Al final, fue muy {adjetivo}."

    print(madlib)
    print("¡Gracias por jugar! Vuelve pronto.")

if __name__=='__main__':
    main()