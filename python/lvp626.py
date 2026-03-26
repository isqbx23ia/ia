'''Faça um programa em Python que leia o salário atual de um funcionário
 e calcule o valor do novo salário 
 de acordo com as faixas salariais a seguir:

Salario atual < R$1000,00 - 20% de aumento

R$1000,00 <= Salario atual <= R$5000,00 - 10% de aumento

Salario atual > R$5000,00 - 5% de aumento

Modelo de saída de dados:

SALARIO ATUAL=99.99 SALARIO NOVO=99.99'''

def main():
    
    #Declaração de váriaveis:

    sa = float()
    aument = float()
    sn = float()

    #Entrada de dados:
    sa = float(input())
    if sa < 1000:
         sn = (sa *  20/100)
         aument = sa + sn
    if sa >= 1000 and sa <= 5000:
        sn = (sa * 10/100)
        aument = sa + sn
    if sa >= 5000:
        sn = (sa * 5/100)
        aument = sa + sn

    print(f"SALARIO ATUAL={sa:.2f} SALARIO NOVO={aument:.2f}")  



    
    return 0
if __name__=="__main__":
    main()