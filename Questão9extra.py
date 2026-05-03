# função recursiva para gerar todas as combinações removendo 1 caractere
def gerar_todas_remocoes(texto):
    print(texto)  # mostra a string atual

    # caso base: quando tiver só 1 letra, para
    if len(texto) == 1:
        return

    # percorre cada posição da string
    for i in range(len(texto)):
        # remove o caractere da posição i
        nova_string = texto[:i] + texto[i + 1:]

        # chama a função novamente com a nova string
        gerar_todas_remocoes(nova_string)


# pede uma string ao usuário
texto = input("Digite uma string: ")

# chama a função
gerar_todas_remocoes(texto)
