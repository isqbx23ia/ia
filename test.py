'''Questão:

Solicite conjuntos de 3 números, (a, b e c) até que o usuário insira um número menor do que 1 para o primeiro valor (a). Ao final exiba o MDC desses números.'''

def main():
    #Declaração
    num1 = int(0)
    num2 = int(0)
    num3 = int(0)
    
    #Entrada de dados
    num1 = int(input())

    #Processamento 
    while num1 > 0:
        num2 = int(input())
        num3 = int(input())        

        if (num1 < num2 and num1 < num3):
            menor = num1
        elif (num2 < num3):
            menor = num2
        else:
            menor = num3

        for i in range(1,menor+1):
            if (num1 % i == 0 and num2 % i == 0 and num3 % i == 0):
                mdc = i

        print(f'MDC({num1}, {num2}, {num3})={mdc} ')
        num1 = int(input())
    
if __name__ == "__main__":
    main()