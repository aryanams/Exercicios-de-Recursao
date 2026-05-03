# mapa com as conexões dos usuários
rede_social = {
    'Renato': ['Ana', 'Bruno'],
    'Ana': ['Carla'],
    'Bruno': ['Diego'],
    'Carla': [],
    'Diego': []
}

# função recursiva para percorrer a rede e contar usuários


def percorrer_rede(usuario, rede, visitados=None):
    if visitados is None:
        visitados = []  # lista de usuários visitados

    if usuario in visitados:
        return 0  # já visitado, não conta

    print(usuario)  # mostra o usuário
    visitados.append(usuario)  # marca como visitado

    total = 1  # conta o usuário atual

    # percorre os colegas
    for colega in rede[usuario]:
        total += percorrer_rede(colega, rede, visitados)

    return total  # retorna o total


# chama a função
total_usuarios = percorrer_rede('Renato', rede_social)

print("Total de usuários únicos alcançados:", total_usuarios)
