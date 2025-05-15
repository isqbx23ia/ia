def main():
    #declaração de variáveis
    idade = int(0)
    soma = int(0)
    flag = str("") #VC

    #atribuição de valores
    soma = 0 #variável acumuladora

    #entrada de dados
    flag = input("Deseja informar uma idade <S/N>: ") #IVC
    while (flag.upper() == "S"): #CP
        idade = int(input("Digite a idade: "))
        soma += idade
        flag = input("Deseja informar outra idade <S/N>:")  #AVC
    print(f'{soma}')

    return 0

if __name__ == "__main__":
    main()
#-----------------------------------------------------------

def main():
    #declaração de variáveis
    idade = int(0)
    soma = int(0)

    #atribuição de valores
    soma = 0 #variável acumuladora

    #entrada de dados
    idade = int(input("Digite a idade (-1 para sair): ")) #IVC
    while (idade >= 0): #CP
        soma += idade
        idade = int(input("Digite outra idade (-1 para sair): ")) #AVC
    print(f'{soma}')
    return 0

if __name__ == "__main__":
    main()

#-----------------------------------------------------------

'''
Faça um programa que leia a idade e o sexo de diversas pessoas. 
A condição de parada será quando for informada uma idade menor que zero.
Ao final o programa deverá apresentar a soma da idade dos homens 
e a média da idade das mulheres
'''

def main():
    #declaração de variáveis
    idade = int(0)
    sexo = str("")
    somam = int(0)
    somaf = int(0)
    contf = int(0)

    #atribuição de valores
    somam = 0 #variável acumuladora
    somaf = 0 #variável acumuladora
    contf = 0 #variável acumuladora

    #entrada de dados
    idade = int(input("Digite a idade (-1 para sair): ")) #IVC
    while (idade >= 0): #CP
        sexo = input("Digite o sexo <M/F>: ")
        if (sexo.upper() == "F"):
            somaf += idade
            contf += 1
        elif (sexo.upper() == "M"):
            somam += idade
        idade = int(input("Digite outra idade (-1 para sair): ")) #AVC
    print(f'\nSoma da idade dos homens = {somam}')
    print(f'Média da idade das mulheres = {somaf/contf}')
    return 0

if __name__ == "__main__":
    main()


