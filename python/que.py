'''Faça um programa em Python 3 que leia três números reais, que representam os coeficientes de uma equação do segundo grau

do tipo ax² + bx + c = 0.

Calcule e imprima: delta e as raízes desta equação.

Modelo de saída de dados:

DELTA = 99.99
X1 = 99.99
X2 = 99.99'''




def main():
#Declaração de variáveis
 a = float(0) 
 b = float(0)
 c = float(0)
 delta = float
 X1 = float
 X2 = float
 

#Entrada de dados
 a = float(input())
 b = float(input())
 c = float(input())
 
 #Processamento
 delta = (b**2 - 4 * a * c)
 X1 = ( -b + delta**0.5) / (2 * a)
 X2 = ( -b - delta**0.5) / (2 * a)
 
 #Saída de dados
 print(f"DELTA = {delta:.2f}")
 print(f"X1 = {X1:.2f}")
 print(f"X2 = {X2:.2f}")
 
 return 0

if __name__=="__main__":
    main()
