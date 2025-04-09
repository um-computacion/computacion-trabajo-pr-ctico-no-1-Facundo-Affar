def decimal_a_romano(numero):
    if not (1 <= numero <= 3999):
        raise ValueError("El número debe estar entre 1 y 3999")

    valores_romanos = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
    resultado = ''
    for valor, simbolo in valores_romanos:
        while numero >= valor:
            resultado += simbolo
            numero -= valor

    return resultado  


if __name__ == "__main__":
    try:
        numero = int(input("Introduce un número entre 1 y 3999: "))
        romano = decimal_a_romano(numero)
        print(f"Tu número decimal se convirtió a romano y se escribe así: {romano}")
    except ValueError as e:
        print(f"Error: {e}")