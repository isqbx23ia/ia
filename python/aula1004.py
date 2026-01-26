#LVP COND 7
def main():
    #declaração de variáveis
    ano = int(0)

    #entrada de dados
    ano = int(input())

    #processamento e saída de dados
    if (ano % 400 == 0):
        print(f'{ano} É BISSEXTO')
    elif (ano % 4 == 0 and ano % 100 != 0):
        print(f'{ano} É BISSEXTO')
    else:
        print(f'{ano} NÃO É BISSEXTO')
    
    return 0

if __name__ == "__main__":
    main()
#----------------------------------------------------    
#LVP COND 7 SIMPLIFICADA
def main():
    #declaração de variáveis
    ano = int(0)

    #entrada de dados
    ano = int(input())

    #processamento e saída de dados
    if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
        print(f'{ano} É BISSEXTO')
    else:
        print(f'{ano} NÃO É BISSEXTO')
    
    return 0

if __name__ == "__main__":
    main()
#----------------------------------------------------

#LVP COND 12
def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    #processamento e saída de dados
    if (a < b and a < c and b < c):
        print(f'{a} {b} {c}')
    else:
        if (a < b and a < c and c < b):
            print(f'{a} {c} {b}')
        else:
            if (b < c and b < a and a < c):
                print(f'{b} {a} {c}')
            else:
                if (b < c and b < a and c < a):
                    print(f'{b} {c} {a}')
                else:
                    if (c < a and c < b and a < b):
                        print(f'{c} {a} {b}')
                    else:
                        print(f'{c} {b} {a}')

    return 0

if __name__ == "__main__":
    main()

#----------------------------------------------------
#LVP COND 12
def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    #processamento e saída de dados
    if (a < b and a < c and b < c):
        print(f'{a} {b} {c}')
    else:
        if (a < b and a < c and c < b):
            print(f'{a} {c} {b}')
        else:
            if (b < c and a < c):
                print(f'{b} {a} {c}')
            else:
                if (b < c and c < a):
                    print(f'{b} {c} {a}')
                else:
                    if (a < b):
                        print(f'{c} {a} {b}')
                    else:
                        print(f'{c} {b} {a}')

    return 0

if __name__ == "__main__":
    main()
#----------------------------------------------------

#LVP COND 12
def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    #processamento e saída de dados
    if (a < b and a < c and b < c):
        print(f'{a} {b} {c}')
    elif (a < b and a < c and c < b):
        print(f'{a} {c} {b}')
    elif (b < c and a < c):
        print(f'{b} {a} {c}')
    elif (b < c and c < a):
        print(f'{b} {c} {a}')
    elif (a < b):
        print(f'{c} {a} {b}')
    else:
        print(f'{c} {b} {a}')

    return 0

if __name__ == "__main__":
    main()

#----------------------------------------------------

#LVP COND 12
def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    #processamento e saída de dados
    if (a < b and a < c):
        if (b < c):
            print(f'{a} {b} {c}')
        else:
            print(f'{a} {c} {b}')
    elif (b < c):
        if(a < c):
            print(f'{b} {a} {c}')
        else:
            print(f'{b} {c} {a}')
    elif (a < b):
        print(f'{c} {a} {b}')
    else:
        print(f'{c} {b} {a}')

    return 0

if __name__ == "__main__":
    main()

#----------------------------------------------------
#LVP COND 13
def main():
    #declaração de variáveis
    a = float(0)
    b = float(0)
    c = float(0)
    delta = float(0)
    x1 = float(0)
    x2 = float(0)

    #entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())

    #processamento e saída de dados
    if (a != 0):
        delta = b**2 - 4*a*c
        if (delta > 0):
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (-b - delta**0.5)/(2*a)
            print(f'{x1} {x2}')
        elif (delta == 0):
            x1 = -b/(2*a)
            print(f'{x1}')
        else:
            print(f'Não há raízes reais')
    return 0

if __name__ == "__main__":
    main()
       
#----------------------------------------------------

#LVP COND 18
def main():
    #declaração de variáveis
    inicio = int(0)
    fim = int(0)


    #entrada de dados
    inicio = int(input())
    fim = int(input())

    #processamento e saída de dados
    if (fim > inicio):
        print(f'{fim-inicio}')
    else:
        print(f'{24-inicio + fim}')

    return 0

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
