n = int(input("Digite o número de linhas da grade: "))
m = int(input("Digite o número de colunas da grade: "))


def contar_caminhos_bloqueados(linha, coluna, n, m, bloqueadas):
    # saiu da grade
    if linha >= n or coluna >= m:
        return 0

    # caiu em casa bloqueada
    if (linha, coluna) in bloqueadas:
        return 0

    # chegou no destino
    if linha == n - 1 and coluna == m - 1:
        return 1

    # pode ir para baixo ou para direita
    return contar_caminhos_bloqueados(linha + 1, coluna, n, m, bloqueadas) + contar_caminhos_bloqueados(linha, coluna + 1, n, m, bloqueadas)


# exemplo: bloqueando a casa da linha 1, coluna 0
bloqueadas = {(1, 0)}

resultado = contar_caminhos_bloqueados(0, 0, n, m, bloqueadas)

print(f"O número de caminhos possíveis é: {resultado}")
