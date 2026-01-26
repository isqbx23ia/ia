def main():
    #declaração de variáveis
    nome = str("")
    nota1 = float(0.0)
    nota2 = float(0.0)
    nota3 = float(0.0)
    nota4 = float(0.0)
    media = float(0.0)

    #entrada de dados
    nome = str(input())
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())

    #processamento de dados
    media = (nota1 + nota2 + nota3 + nota4)/4
    
    #saida
    if (media >= 60):
        print(f'Aluno {nome} foi aprovado com média {media}')
    elif (media >= 20):
        print(f'Aluno {nome} está de prova final com média {media}')
    else:
        print(f'Aluno {nome} foi reprovado com média {media}')
    return 0

if __name__ == "__main__":
    main()
    -----------------------------------------------------------------------
    def main():
    SLF = int(0) #Salário
    CMS = int(0) #Comissão
    Venda = int(0) #Vendas
    SFV = int(0) #Salário Final Do Vendedor

    #Entradas de dados
    SLF = int(input())
    CMS = int(input())
    Venda = int(input())
    
    #Processamento
    SFV = (SLF + CMS) + Venda * (5%)