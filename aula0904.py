#LVP COND 11
def main():
    #declaração de variáveis
    a = float(0)
    b = float(0)
    c = float(0)
    maior = float(0)
    maior2 = float(0)
    
    #entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())
    
    #processamento
    if (a > b and a > c):
        maior = a
        if (b > c):
            maior2 = b
        else:
            maior2 = c
    else:
        if (b > a and b > c):
            maior = b
            if (a > c):
                maior2 = a
            else:
                maior2 = c
        else:
            if (c > a and c > b):
                maior = c
                if (a > b):
                    maior2 = a
                else:
                    maior2 = b
    #saida de dados
    print(f'{maior+maior2}')
    
    return 0
    
if __name__ == "__main__":
    main()
    
#----------------------------------------------------    

def main():
    #declaração de variáveis
    a = float(0)
    b = float(0)
    c = float(0)
    maior = float(0)
    maior2 = float(0)
    
    #entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())
    
    #processamento
    if (a > b and a > c):
        maior = a
        if (b > c):
            maior2 = b
        else:
            maior2 = c
    else:
        if (b > c):
            maior = b
            if (a > c):
                maior2 = a
            else:
                maior2 = c
        else:
            maior = c
            if (a > b):
                maior2 = a
            else:
                maior2 = b
    
    #saida de dados
    print(f'{maior+maior2}')
    
    return 0
    
if __name__ == "__main__":
    main()

#----------------------------------------------------
def main():
    #declaração de variáveis
    a = float(0)
    b = float(0)
    c = float(0)
    maior = float(0)
    maior2 = float(0)
    
    #entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())
    
    #processamento
    if (a > b and a > c):
        maior = a
        if (b > c):
            maior2 = b
        else:
            maior2 = c
    elif (b > c):
        maior = b
        if (a > c):
            maior2 = a
        else:
            maior2 = c
    else:
        maior = c
        if (a > b):
            maior2 = a
        else:
            maior2 = b
    
    #saida de dados
    print(f'{maior+maior2}')
    
    return 0
    
if __name__ == "__main__":
    main()

#----------------------------------------------------

def main():
    #declaração de variáveis
    a = float(0)
    b = float(0)
    c = float(0)
    maior = float(0)
    maior2 = float(0)
    
    #entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())
    
    #processamento e saída de dados
    if (a < b and a < c):
        print(f'{b+c}')
    elif (b < c):
        print(f'{a+c}')
    else:
        print(f'{a+b}')
    
    return 0
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
