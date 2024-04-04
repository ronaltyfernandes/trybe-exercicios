def maior_numero(num1, num2):
    #returna o maior numero entre dois
    if num1>num2:
        return num1
    return num2
  

def media(lista): 
    #returna a media de uma lista
    sum = 0
    for num in lista:
        sum += num
    return sum/len(lista)


def quadrado_asterico(num):
    #returna um quadrado de arteriscos baseado no numero
    index = 1
    while index<num:
        print(num* '*')
        index+=1
    
         
    
def mais_letras(lista):
    #returna o a palavra com mais letras da lista    
    maior_palavra = ''
    for palavra in lista:
        if len(palavra)> len(maior_palavra):
            maior_palavra = palavra
    return maior_palavra


def menor_numero(numbers):
    #returna o menor numero da lista
    smaller = numbers[0]
    for number in numbers:
        if number < smaller:
            smaller = number
    return smaller
    

def maior_numero_lista(lista):
    #returna o maior numero da lista
    return max(lista)

def piramidePalavra(word):
    armazena_palavra = word
    while len(armazena_palavra) > 0:
        print(armazena_palavra)
        armazena_palavra = armazena_palavra[:-1]
