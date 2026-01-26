def main():
    #declaração de variáveis

    #entrada de dados

    #processamento

    #saída de dados

    return 0

if __name__ == "__main__":
    main()
#---------------------------------------------------	
#LVP INTRO 21
import math

def main():
    #declaração de variáveis
    area = float(0.0)
    latas18 = float(0.0)
    latas3 = float(0.0)
    litros = float(0.0)
    
    #entrada de dados
    area = float(input())
    #processamento
    litros = area/6
    latas18 = math.ceil(litros/18)
    latas3 = math.ceil(litros/3.6)

    #saída de dados
    print(f'Você utilizará {latas18} de 18L. Valor = {latas18*80:.2f}')
    print(f'Você utilizará {latas3} de 3.6L. Valor = {latas3*25:.2f}')
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------
#LVP CONDICIONAIS 1
def main():
    #declaração de variáveis
    n = int(0)

    #entrada de dados
    n = int(input())

    #processamento e saída de dados
    if (n % 2 == 0):
        print(f'{n} é PAR')
    else:
        print(f'{n} é ÍMPAR')
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------	
#LVP CONDICIONAIS 2
def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())

    #processamento e saída de dados
    if (a > b):
        print(f'{a} + {b} = {a+b}')
    else:
        print(f'{a} x {b} = {a*b}')
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------	
#LVP CONDICIONAIS 3
def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())

    #processamento e saída de dados
    if (a > b):
        print(f'{a} - {b} = {a-b}')
    else:
        print(f'{b} - {a} = {b-a}')

    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------	

