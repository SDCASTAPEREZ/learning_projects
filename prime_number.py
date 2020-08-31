def run():
    numero = int(input("Te diremos si un número es o no es primo. Dígita el número natural que quieras: "))
    contador = 0
    
    for i in range (1, numero + 1):
        if i == 1:
            continue
        if i == numero:
            continue
        residuo = numero % i
        print(str(numero) + " dividido " + str(i) + " deja como residuo " + str(residuo))
        
        if residuo == 0:
            contador = contador + 1     

    
    if contador == 0:
        print("Es un número primo, esto quiere decir que sólo es divisible por 1 y " + str(numero))
    else:
        print("No es número primo")


if __name__ == '__main__':
    run()