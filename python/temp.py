def main():
    #Declaração de váriaveis:
    far = float()
    cel = float()

    #Entrada de dados:
    far = float(input())
    

    #Processamento de dados:

    cel = (far -32 ) / 9
    cel *= 5
    print(f'FAHRENHEIT={far:.2f} CELSIUS={cel:.2f}')


    return 0
if __name__=="__main__":
 main()











'''Faça um programa em Python 3 que leia uma temperatura fornecida em graus Fahrenheit e converta esta temperatura em graus Celsius. Imprima os valores das temperaturas.

Modelo de saída de dados:

FAHRENHEIT=99.99 CELSIUS=99.99


Celsius5=FAHRENHEIT−329

'''