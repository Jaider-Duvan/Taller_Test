def verificar_numero_positivo():
    # Solicita al usuario un número entero positivo y lo retorna.
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo: "))
            if numero > 0:
                return numero  
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Ingresa un número entero válido.")

def numero_armstrong(num):
    # Convertimos el número a string y calculamos la cantidad de dígitos
    num_str = str(num)
    num_digitos = len(num_str)

    # Calculamos la suma de los dígitos elevados a la potencia del número de dígitos
    suma = sum(int(digito) ** num_digitos for digito in num_str)

    # Comparamos la suma con el número original
    return num == suma

def main():
    print("Verificador de Números de Armstrong")
    numero = verificar_numero_positivo()
    if numero_armstrong(numero):
        print(f"¡El número {numero} es un número de Armstrong!")
    else:
        print(f"El número {numero} no es un número de Armstrong.")


if __name__ == "__main__":
    main()