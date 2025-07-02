gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol Desenvolvido pela EA Sports
É possível jogar online
"""

# string[inicio:fim] - índice começa na posição 0 | índice final na posição -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:7])

# 3 - Busque toda string da 3 até a última posição
print(gameName[2:])

# string[inicio:fim:passo] - índice começa na posição 0 | índice final na posição -1 | passo determina o incremento que por padrão é 1

# 4 - Busque toda string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda string nos índices ímpares
print(gameName[1::2])

# 6 - Inverter uma string (de trás para frente)
print(gameName[::-1])