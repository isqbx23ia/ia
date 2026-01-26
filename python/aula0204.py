def main():
    #declaração de variáveis

    #entrada de dados

    #processamento

    #saída de dados

    return 0

if __name__ == "__main__":
    main()
#---------------------------------------------------	

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    aux = int(0)

    #entrada de dados
    a = int(input())
    b = int(input())

    #processamento
    aux = a 
    a = b
    b = aux

    #saída de dados
    print(f'{a} e {b}')

    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------

def main():
    #declaração de variáveis
    n = int(0)
    c = int(0)
    d = int(0)
    u = int(0)
    novo = int(0)
    

    #entrada de dados
    n = int(input())

    #processamento
    c = n // 100
    resto = n % 100
    d = resto // 10
    u = resto % 10
    
    novo = u * 10**2 + d * 10**1 + c * 10**0
    #novo = u * 100 + d * 10 + c
    
    #saída de dados
    print(f'{novo}')

    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------	

def main():
    #declaração de variáveis
    vh = float(0.0)
    horas = int(0)
    ir = float(0.0)
    inss = float(0.0)
    sindicado = float(0.0)
    salario = float(0.0)
    liquido = float(0.0)

    #entrada de dados
    vh = float(input())
    horas = int(input())

    #processamento
    salario = vh * horas
    ir = salario * 11/100
    inss = salario * 8/100
    sindicato = salario * 5/100
    liquido = salario - (ir + inss + sindicato)
    

    #saída de dados
    print(f'+ Salário Bruto : R$ {salario:.2f}')
    print(f'- IR (11%) : R$ {ir:.2f}')
    print(f'- INSS (8%) : R$ {inss:.2f}')
    print(f'- Sindicato ( 5%) : R$ {sindicato:.2f}')
    print(f'= Salário Líquido : R$ {liquido:.2f}')    
    return 0

if __name__ == "__main__":
    main()