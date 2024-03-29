from random import randint
from time import sleep

def main(x):

    print(23*"=")
    print(" ¡Bienvenido al juego! ")
    print(23*"=")
    sleep(3)
    print("EL juego es sencillo")
    print(f"Tienes que adivinar un número entre 1 y {x}")
    sleep(3)

    numero = randint(1, x)

    eleccion = 0
    count = 0
    stop = x//4

    while eleccion != numero and count<=stop:
        count += 1
        eleccion = int(input(f"Escribe un número entre 1 y {x}: "))
        
        if eleccion < numero:
            print("El número que escogiste es muy pequeño. ¡Prueba de nuevo!")
        elif eleccion > numero:
            print("EL número que escogiste es muy grande. ¡Prueba de nuevo!")
    
    if eleccion==numero:
        print(f"¡Felicidades! Lograste adivinar el número {numero}" )
        print(f"Lograste hacerlo en {count} ocasiones")
    else:
        print("Lo sentimos. Tardaste mucho en adivinar")


if __name__ == '__main__':
    main(20)