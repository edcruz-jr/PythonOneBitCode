# 1 - Modificando o caracter da string para $ (Exceto se esse caracter for o primeiro)
string = "fifa 23"
primeiraLetra = string[0:1] # Guardar o valor da primeira letra

print(f"Palavra selecionada: {string}")

caracterModificar = input("Digite o caracter que deseja modificar: ")
novoCaracter = input("Digite o caracter que irá ser aplicado: ")
novaPalavra = primeiraLetra + string[1:].replace(caracterModificar, novoCaracter)

print(f"Nova palavra: {novaPalavra}")

# 2 - Receber uma string com duas strings e trocar apenas os dois primeiros caracteres de cada string
string = "abc xyz"
string1 = string.split(" ")[0]
string2 = string.split(" ")[1]
modificaString1 = string2[0:2] + string1[2]
modificaString2 = string1[0:2] + string2[2]
concatenaString = modificaString1 + " " + modificaString2

print(f"String modificada: {concatenaString}")