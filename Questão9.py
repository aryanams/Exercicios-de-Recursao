# função recursiva para gerar versões da string
def gerar_versoes(texto):
    print(texto)  # mostra a string atual

    # caso base: quando restar só uma letra, para
    if len(texto) == 1:
        return

    # passo recursivo: remove o primeiro caractere
    gerar_versoes(texto[1:])


# pede uma string ao usuário
texto = input("Digite uma string para gerar as versões: ")

# chama a função
gerar_versoes(texto)
