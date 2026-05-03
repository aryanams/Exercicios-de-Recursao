# pede um número ao usuário
n = int(input("Digite um número: "))

# função recursiva para calcular Fibonacci


def fibonacci(n):
    if n < 0:
        return "Número inválido. Digite um número não negativo."  # verifica número inválido
    elif n == 0:
        return 0  # caso base
    elif n == 1:
        return 1  # caso base
    else:
        # soma dos dois termos anteriores
        return fibonacci(n - 1) + fibonacci(n - 2)


# mostra o resultado
print(f"O {n}-ésimo termo da sequência de Fibonacci é: {fibonacci(n)}")
