# pede uma string ao usuário
texto = input("Digite uma string para inverter: ")

# função recursiva para inverter a string
def inverter_string(texto):
    if len(texto) == 0:
        return texto  # caso base (string vazia)
    else:
        # pega a última letra + inverte o resto
        return texto[-1] + inverter_string(texto[:-1])

# mostra o resultado
print(f"A string invertida é: {inverter_string(texto)}")