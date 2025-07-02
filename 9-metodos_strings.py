gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol, Desenvolvido pela EA Sports,
É possível jogar online
"""

print(gameName.upper()) # Retornar a string em maiúsculo
print(gameName.lower()) # Retornar a string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maiúsculo
print(gameName.center(10, "-")) # Retorna a string centralizada
print(gameName.find("a")) # Retorna a posição de um determinado caractere
print(gameDescription.count("f")) # Conta caracteres
print(gameDescription.replace("Fifa", "PES")) # Altera um elemento por outro
print(gameDescription.split(","))
