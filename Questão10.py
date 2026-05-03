# mapa com as conexões dos usuários
rede_social = {
    'Renato': ['Ana', 'Bruno'],
    'Ana': ['Carla'],
    'Bruno': ['Diego'],
    'Carla': [],
    'Diego': []
}

# função recursiva para percorrer a rede de conexões


def percorrer_rede(usuario, rede, visitados=None):
    if visitados is None:
        visitados = []  # lista para controlar usuários já visitados

    if usuario not in visitados:
        print(usuario)  # mostra o usuário atual
        visitados.append(usuario)  # marca como visitado

        # percorre os usuários indicados
        for colega in rede[usuario]:
            percorrer_rede(colega, rede, visitados)


# inicia a busca a partir de Renato
percorrer_rede('Renato', rede_social)
