# mapa com as conexões das salas
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
        visitadas = []  # lista para controlar salas já visitadas

    if sala_atual not in visitadas:
        print(sala_atual)  # mostra a sala atual
        visitadas.append(sala_atual)  # marca como visitada

        # percorre as salas conectadas
        for sala_conectada in mapa[sala_atual]:
            visitar_salas(sala_conectada, mapa, visitadas)


# inicia a visita a partir da sala A
visitar_salas('A', mapa_salas)
