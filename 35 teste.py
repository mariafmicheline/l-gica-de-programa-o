def contar_numeros():
    numeros = []  # Lista para armazenar os números inseridos
    while True:
        try:
            entrada = int(input("Digite um número (0 para sair): "))
            if entrada == 0:
                break  # Se o número digitado for 0, sair do loop
            numeros.append(entrada)  # Adicionar o número à lista
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    quantidade_numeros = len(numeros)  # Contar quantos números foram inseridos
    print(f"Foram digitados {quantidade_numeros} número(s) diferente(s) de zero.")