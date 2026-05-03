# lê os números digitados pelo usuário (separados por vírgula)
vetor = list(
    map(int, input("Digite números separados por vírgula: ").split(',')))

# função recursiva para somar os elementos do vetor


def soma(vetor):
    if len(vetor) == 0:
        return 0  # caso base (vetor vazio)
    else:
        return vetor[0] + soma(vetor[1:])  # soma o primeiro + resto


# mostra o resultado
print(f"A soma dos números é: {soma(vetor)}")
