n = int(input("Digite o número de linhas da grade: "))
m = int(input("Digite o número de colunas da grade: "))


def contar_caminhos(n, m):
    # Caso base: se chegamos ao destino, há um caminho válido
    if n == 1 and m == 1:
        return 1
    # Se estamos fora dos limites da grade, não há caminhos válidos
    if n < 1 or m < 1:
        return 0
    # Passo recursivo: mover para a direita ou para baixo
    return contar_caminhos(n - 1, m) + contar_caminhos(n, m - 1)


print(
    f"O número de caminhos possíveis em uma grade de {n} x {m} é: {contar_caminhos(n, m)}")
