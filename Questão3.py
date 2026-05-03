# pede um número ao usuário
numero = int(input("Digite um número: "))

# função recursiva para contagem regressiva


def contagem_regressiva(n):
    if n < 0:
        print("Número inválido. Digite um número não negativo.")
        return

    print(n)  # imprime o número atual

    if n == 0:  # caso base
        return

    contagem_regressiva(n - 1)  # chamada recursiva


# chama a função
contagem_regressiva(numero)
