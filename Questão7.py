# mapa com as conexões entre as salas
mapa_salas = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

# função recursiva para visitar as salas


def visitar_salas(sala_atual, mapa, visitadas=None):
    if visitadas is None:
        visitadas = []  # lista para guardar salas já visitadas

    if sala_atual not in visitadas:
        visitadas.append(sala_atual)  # adiciona a sala atual

        # percorre as salas conectadas
        for sala_conectada in mapa[sala_atual]:
            visitar_salas(sala_conectada, mapa, visitadas)

    return visitadas  # retorna a ordem das salas visitadas


# chama a função começando da sala A
resultado = visitar_salas('A', mapa_salas)

# mostra o resultado
print(resultado)
