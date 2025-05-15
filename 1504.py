import turtle
def main():
    #declaração de variáveis
    i = int(0)
    ang = float(0.0)
    lados = int(0)
    t = int(0)

    #atribuição de valores
    i = 0 #inicialização da variavel de controle (vc)
    lados = 1000
    t = 1000/lados
    ang = 360/lados

    #criando a tartaruga e a tela
    g = turtle.Turtle()
    w = turtle.Screen()
    g.speed(1000)
    g.shape("turtle")

    #processamento e saída
    while (i < lados): #condição de parada
        g.forward(t)
        g.left(ang)
        i = i + 1  #atualização da variavel de controle (vc)

    #mantendo a janela aberta até o clique do mouse
    w.exitonclick()

    return 0

if __name__ == "__main__":
    main()

#----------------------------------------------------------------	

def main():
    #declaração de variáveis
    i = int(0)

    #atribuição de valores
    i = 0 #inicialização da variavel de controle (vc)

    while (i < 0): #condição de parada
        print(i)
        i -= 1 #i = i + 1 #atualização da variavel de controle (vc)

    return 0

if __name__ == "__main__":
    main()

#----------------------------------------------------------------

def main():
    #declaração de variáveis
    i = int(0)
    x = int(0)
    soma = int(0)

    #atribuição de valores
    soma = 0
    i = 0 #inicialização da variavel de controle (vc)
    while (i < 5): #condição de parada
        x = int(input())
        soma += x
        i += 1 #i = i + 1 #atualização da variavel de controle (vc)
    print(soma/i)

    return 0

if __name__ == "__main__":
    main()

#----------------------------------------------------------------

def main():
    #declaração de variáveis
    i = int(0)
    x = int(0)
    soma = int(0)

    #atribuição de valores
    soma = 0
    i = 0 #inicialização da variavel de controle (vc)
    while (i < 5): #condição de parada
        x = int(input())
        soma += x
        i += 1 #i = i + 1 #atualização da variavel de controle (vc)
    print(soma/i)
    soma = 0
    for i in range(0,5,1):
        x = int(input())
        soma += x
    print(soma/(i+1))

    return 0

if __name__ == "__main__":
    main()

#----------------------------------------------------------------