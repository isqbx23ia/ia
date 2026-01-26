def main():
    #declaração de variáveis

    #entrada de dados

    #processamento



    return 0

if __name__ == "__main__":
    main()
#---------------------------------------------	

'''
LVP R 8: Faça um Algoritmo que leia 5 valores inteiros e escreva no final a soma dos valores lidos.
'''
def main():
    #declaração de variáveis
    i = int(0) #variável de controle
    n = int(0)
    soma = int(0) #variável acumuladora

    #inicialização da variável de controle
    i = 0 
    
    #entrada de dados
    while (i < 5): #condição de parada
        n = int(input())
        soma = soma + n #soma += n #processamento
        i = i + 1 #i += 1 atualização da variável de controle

    #saída de informação
    print(f'{soma}')
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------

'''
LVP R 9: Faça um Algoritmo que leia 5 valores inteiros e escreva no final a média dos valores lidos.
'''
def main():
    #declaração de variáveis
    i = int(0) #variável de controle
    n = int(0)
    soma = int(0) #variável acumuladora

    #inicialização da variável de controle
    i = 0 
    
    #entrada de dados
    while (i < 5): #condição de parada
        n = int(input())
        soma = soma + n #soma += n #processamento
        i = i + 1 #i += 1 atualização da variável de controle

    #saída de informação
    print(f'{soma/i}')
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------

'''
LVP R 10: Faça um Algoritmo que leia 5 valores e escreva no final a soma dos valores positivos e a
média dos negativos. 
'''
def main():
    #declaração de variáveis
    i = int(0) #variável de controle
    n = int(0)
    somap = int(0) #variável acumuladora
    soman = int(0) #variável acumuladora
    contn = int(0) #variável acumuladora

    #inicialização da variável de controle
    i = 0 
    somap = 0
    soman = 0
    contn = 0

    #entrada de dados
    while (i < 5): #condição de parada
        n = int(input())
        if (n >= 0):
            somap = somap + n #varíavel acumuladora
        else:
            soman = soman + n #varíavel acumuladora
            contn = contn + 1 #varíavel contadora
        i = i + 1 #i += 1 atualização da variável de controle

    #saída de informação
    print(f'{somap}')
    if (contn > 0):
        print(f'{soman/contn}')
    else:
        print("Não foram informados números negativos")
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------

'''
LVP C 15: Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo e qual tipo de triângulo é. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.
'''
def main():
    #declaração de variáveis
    a = float(0.0)
    b = float(0.0)
    c = float(0.0)

    #entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())

    #processamento
    if (a + b > c and a + c > b and b + c > a):
        if (a == b and b == c):
            print(f'EQUILÁTERO')
        elif (a == b or b == c or a == c):
            print(f'ISÓSCELES')
        else:
            print(f'ESCALENO')
    else:
        print(f'NÃO É TRIÂNGULO')
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------

'''
LVP C 17: Ler 3 valores inteiros: a, b e c (considere que não serão informados valores iguais). Utilizando o algoritmo de troca de valores entre variáveis, vistos na LVP INTRODUÇÃO 18: TROCAR VALORES, realocar os valores das variáveis, fazendo com que o menor valor esteja na variável a, o segundo menor valor na variável b e o maior valor na variável c.

A saída do programa deve ser, obrigatoriamente, com a linha, abaixo:

print(f'{a} {b} {c}')
'''
def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)
    aux = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    #processamento
    if (a < b and a < c):
        if (c < b):
            aux = b
            b = c
            c = aux
    elif (b < c):
        aux = a
        a = b
        b = aux
        if (c < b):
            aux = b
            b = c
            c = aux     
    else:
        aux = a
        a = c
        c = aux   
        if (c < b):
            aux = b
            b = c
            c = aux                    
    #saida
    print(f'{a} {b} {c}')

    return 0

if __name__ == "__main__":
    main()
