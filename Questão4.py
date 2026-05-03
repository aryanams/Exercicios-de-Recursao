# pede a base e o expoente
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# função recursiva para calcular potência
def potencia(base, expoente):
    if expoente == 0:
        return 1  # caso base (qualquer número elevado a 0 é 1)
    else:
        return base * potencia(base, expoente - 1)  # chamada recursiva

# mostra o resultado
print(f"{base} elevado a {expoente} é: {potencia(base, expoente)}")