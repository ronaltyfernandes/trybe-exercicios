# o mode=w diz o tipo de operação que vamos fazer, no caso write
caracters_file = open("melhores-equipes-formula1.txt", mode='w')

# o \n faz a quebra de linha no texto, vital para a leitura e utilização dos dados
caracters_file.write("mercedes petronas\n")
caracters_file.write("maclaren\n")
caracters_file.write("redBull racing\n")

# se escrevermos dentro do print especificando qual o arquivo
# nos vamos dar a saida dentro do arquivo, logo escrevendo nele
print('alfa Romeu', file=caracters_file)

mais_equipes = ["Hass\n", "aston Martin\n"]

caracters_file.writelines(mais_equipes)

# sempre precisamos fechar o arquivo
# uma vez que se não for fechado uma serie de erro vai ocorrer
caracters_file.close()