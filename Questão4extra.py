# pede a base e o expoente
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# função recursiva para calcular potência


def potencia(base, expoente):
    if expoente < 0:
        return 1 / potencia(base, -expoente)  # trata expoente negativo
    elif expoente == 0:
        return 1  # caso base (qualquer número^0 = 1)
    else:
        return base * potencia(base, expoente - 1)  # recursão


# mostra o resultado
print(f"{base} elevado a {expoente} é: {potencia(base, expoente)}")
