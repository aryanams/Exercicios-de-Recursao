# pede um número ao usuário
numero = int(input("Digite um número: "))

# função recursiva para calcular o fatorial


def fatorial(numero):
    if numero == 0:
        return 1  # caso base (0! = 1)
    else:
        return numero * fatorial(numero - 1)  # n * (n-1)!


# mostra o resultado
print(f"O fatorial de {numero} é: {fatorial(numero)}")
