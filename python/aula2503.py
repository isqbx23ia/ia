#LVP 5
def main():
    #declaração de variáveis
    anos = int 
    meses = int(0)
    dias = int(0)
    idade_em_dias = int(0)
    
    #entrada de dados
    anos = int(input())
    meses = int(input())
    dias = int(input())
    
    #processamento 
    idade_em_dias = anos * 365 + meses * 30 + dias
    
    #saída de dados
    print(f'Idade em dias: {idade_em_dias}')
    return 0
    
if __name__ == "__main__":
    main()
	
#---------------------------------------------------------
#Faça um programa que receba a idade em dias e informe a idade em anos, meses e dias
def main():
    #declaração de variáveis
    anos = int 
    meses = int(0)
    dias = int(0)
    resto = int(0)
    idade_em_dias = int(0)
    
    #entrada de dados
    idade_em_dias = int(input())
    
    #processamento
    anos = idade_em_dias // 365
    resto = idade_em_dias % 365
    meses = resto // 30
    dias = resto % 30
    
    #saída de dados
    print(f'{anos}, {meses} e {dias}')
    return 0
    
if __name__ == "__main__":
    main()

#---------------------------------------------------------

#LVP 6
def main():
    #declaração de variáveis
    total = int(0)
    vb = int(0) #votos em branco
    vn = int(0) #votos nulos
    vv = int(0) #votos válidos
    pb = float(0.0) #percentual votos em branco
    pn = float(0.0) #percentual em branco
    pv = float(0.0) #percentual votos em branco
    
    #entrada de dados
    total = int(input())
    vb = int(input()) #votos em branco
    vn = int(input()) #votos nulos
    vv = int(input()) #votos válidos
    
    #processamento 
    pb = vb * 100 / total
    pn = vn * 100 / total
    pv = vv * 100 / total
    #saída de dados
    print(f'BRANCOS={pb:.2f} %')
    print(f'NULOS={pn:.2f} %')
    print(f'VÁLIDOS={pv:.2f} %')
    return 0
    
if __name__ == "__main__":
    main()

#---------------------------------------------------------

	