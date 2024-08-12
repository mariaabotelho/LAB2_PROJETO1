def cumprimento(nome):
    return f"que a Força esteja com vc, {nome}! (Star Wars)"

print(cumprimento("Maria Antonia Botelho"))

import random
def sorteia_media():
    numeros = [random.randint(1, 100) for _ in range(3)]
    media = sum(numeros) / len(numeros)
    return media

print(f"a média dos números sorteados é: {sorteia_media()}")


