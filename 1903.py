'''
Algoritmo media
var
n1, n2, n3, n4, media: real // declaração de variáveis
início // começo do algoritmo
leia (n1, n2, n3, n4); // entrada de dados
media <- (n1 + n2 + n3 + n4)/4; //processamento
escreva (media); // saída de dados
fim. // fim do algoritmo'''

def main():
    #declaração de variáveis
    n1 = float(0.0)
    n2 = float(0.0)
    n3 = float(0.0)
    n4 = float(0.0)
    media = float(0.0)
    
    #entrada de dados
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    #processamento
    media = (n1 + n2 + n3 + n4)/4

    #saída de dados
    print(f'{media:.2f}')
    return 0

if __name__ == "__main__":
    main()
	
#---------------------------------------------------	
#PRIMEIRA LVP
def main():
    #declaração de variáveis
    x = float(0)
    y = float(0)
    soma = float(0)
    
    #entrada de dados
    x = float(input())
    y = float(input())
    
    #processamento
    soma = x + y
    
    #saída de dados
    print(f'{soma}')
    
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------------
#PRIMEIRA LVP
def main():
    #declaração de variáveis
    x = float(0)
    y = float(0)
    soma = float(0)

    #entrada de dados
    x = float(input())
    y = float(input())

    #processamento 
    soma = x * y 

    #saída de dados
    print(f'{soma}')

    return 0 

if __name__ == "__main__":
    main()