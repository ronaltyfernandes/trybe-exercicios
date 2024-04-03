def maior_numero(num1, num2): 
    if num1>num2:
        return num1
    return num2
  

def media(lista): 
    sum = 0
    for num in lista:
        sum += num
    return sum/len(lista)


def quadrado_asterico(num):
    index = 1
    while index<num:
        print(num* '*')
        index+=1
    
         
    
def mais_letras(lista):
    maior_palavra = ''
    for palavra in lista:
        if len(palavra)> len(maior_palavra):
            maior_palavra = palavra
    return maior_palavra


def menor_numero(numbers):
    smaller = numbers[0]
    for number in numbers:
        if number < smaller:
            smaller = number
    return smaller
    

def maior_numero_lista(lista):
    return max(lista)
