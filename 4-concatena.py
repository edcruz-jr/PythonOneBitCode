name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planInclude = input("Está incluso no serviço mensal:\n")

print("### Dados do jogo###")
print("====================")
# Alternativa 1
# print("Nome do jogo: ", name)
# print("Ano de Lançamento: ", yearLaunch)
# print("Preço do jogo: ", gamePrice)
# print("Está incluído no jogo: ", planInclude)

# Alternativa 2
# print("Nome do jogo: ", name, "\nAno de lançamento: ", yearLaunch, "\nPreço do jogo: ", gamePrice, "\nEstá incluso no plano: ", planInclude)

# Alternativa 3
print(f"Nome do jogo: {name} \nAno de lançamento: {yearLaunch} \nPreço do jogo: {gamePrice} \nEstá incluso no plano: {planInclude}")