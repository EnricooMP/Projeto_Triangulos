while True:
    try:
        l1 = float(input("\nLado 1: "))
        l2 = float(input("Lado 2: "))
        l3 = float(input("Lado 3: "))
    except ValueError:
        print("Erro: Digite apenas números")
        continue # O continue é para voltar ao início do while se der erro

    if (l1 + l2 > l3 ) and (l1 + l3 > l2) and (l2 + l3 > l1): # o "and" é usado para que tudo dentro dos "()" seja validado.

        if (l1 == l2 == l3):
            print("\n--- Triangulo equilátero ---")
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print("\n--- Triangulo isósceles ---")
        else:
            print("\n--- Triangulo escaleno ---")
    else:
        print("Os valores informados não foram um triangulo")

    pergunta = input("\nDeseja fazer outro cáculo? (s/n): ").lower()
    if pergunta != 's':
        print("Até logo!")
        break



    
