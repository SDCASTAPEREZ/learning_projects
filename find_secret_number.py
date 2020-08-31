def run():
    print("""
    Hola.
    En este reto tienes que adivinar el número secreo (entre 0 y 9), para lograrlo tienes 3 intentos.
    Mucha suerte :D
    """)
    
    intentos = 0

    while intentos < 3:
        numero_prueba = input("Digita un número: ")
        intentos += 1

        if numero_prueba == "6":
            print("Felicidades adivinaste, el número secreto es 6")
            break

        if intentos == 3:
            print("Perdiste ToT F")


if __name__ == "__main__":
    run()