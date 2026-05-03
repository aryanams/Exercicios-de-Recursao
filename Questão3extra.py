# pede um número ao usuário
numero = int(input("Digite um número: "))

# função recursiva para contagem progressiva


def contagem_progressiva(n):
    if n < 0:
        print("Número inválido. Digite um número não negativo.")
        return

    if n == 0:  # caso base
        print(0)
        return

    contagem_progressiva(n - 1)  # chama antes
    print(n)  # imprime depois


# chama a função
contagem_progressiva(numero)
