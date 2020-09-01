import random
numero_secreto = random.randint(1, 100)

print("""
Minijuego: ¡Adivina el Número Secreto!

Pensaré un número del 1 al 100. Tienes 10 vidas para adivinar mi número secreto.
Te iré guiando, pero estoy seguro que no lo lograrás ᕦ(ò_óˇ)ᕤ

¡Suerte!

""")


def run():
    vidas = 10
   

    while vidas > 0:
        intento = int(input("¿Cuál crees que es mi número secreto?: "))

        if numero_secreto == intento:
            print("""¿¡Qué!? Un simple simio como tú pudo averiguar mi número secreto ToT
        
            Felicidades ('-_-)""")
            break

        if intento < numero_secreto:
            print("""
            """)
            print("Pff. Mi número secreto es mayor (~˘▾˘)~")
            vidas = vidas - 1
            print("Te quedan " + str(vidas) + " vidas")
            print("""
            """)
        elif numero_secreto < intento:
            print("""
            """)            
            print("Mi número secreto es menor jaja (~˘▾˘)~")
            vidas = vidas - 1
            print("Te quedan " + str(vidas) + " vidas")
            print("""
            """)

    if vidas == 0:
        print("JAJAJA perdiste. SOY EL MEJOR ᕦ(ò_óˇ)ᕤ")


if __name__ == "__main__":
    run()