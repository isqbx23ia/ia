#Código Eficaz mas pouco eficiente
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
        print(f"aprovado com média = {media}")

    if (media < 60 and media >= 20):
        print(f"prova final com média = {media}")

    if (media < 20):
        print(f"reprovado com média = {media}")

    return 0

if __name__ == "__main__":
    main()
	
#---------------------------------------------------------
#Código Eficaz e mais Eficiente que anterior
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
        print(f"aprovado com média = {media}")
    else:
        if (media < 60 and media >= 20):
            print(f"prova final com média = {media}")
        else:
            if (media < 20):
                print(f"reprovado com média = {media}")
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------------
#Código Eficaz e mais Eficiente que anterior
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
        print(f"aprovado com média = {media}")
    else:
        if (media >= 20):
            print(f"prova final com média = {media}")
        else:
            print(f"reprovado com média = {media}")
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------------
#Código Eficaz e tão Eficiente quanto o anterior, porém, simplificado pelo elif
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
        print(f"aprovado com média = {media}")
    elif (media >= 20):
        print(f"prova final com média = {media}")
    else:
        print(f"reprovado com média = {media}")
    return 0

if __name__ == "__main__":
    main()
    
#---------------------------------------------------------

def main():
    #declaração de variáveis
    idade = int(0)
    
    #entrada de dados
    idade = int(input())
    
    #saida
    if (idade <= 10):
        print(f"Categoria: Infantil")
    else:
        if (idade <= 15):
            print(f'Categoria: Juvenil')
        else:
            if (idade <= 20):
                print(f'Categoria: Júnior')
            else:
                if (idade < 30):
                    print(f'Categoria: Profissional')
                else:
                    print(f'Categoria: Sênior')
    return 0

if __name__ == "__main__":
    main()

#---------------------------------------------------------

def main():
    #declaração de variáveis
    idade = int(0)
    
    #entrada de dados
    idade = int(input())
    
    #saida
    if (idade <= 10):
        print(f"Categoria: Infantil")
    elif (idade <= 15):
        print(f'Categoria: Juvenil')
    elif (idade <= 20):
        print(f'Categoria: Júnior')
    elif (idade < 30):
        print(f'Categoria: Profissional')
    else:
        print(f'Categoria: Sênior')
    return 0

if __name__ == "__main__":
    main()

