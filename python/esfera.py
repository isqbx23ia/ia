def main():

    area = int()
    pi = 3.14
    vol = int()
    raio = int()

    #entrada de dados
    raio = int(input())


    area = 4 * pi * (raio**2)
    vol = 4/3 * pi * (raio**3)
    print(f'{raio:.2f} {area:.2f} {vol:.2f}')
    






    return 0
if __name__=="__main__":
 main()


 '''Faça um programa em Python 3 que leia o raio de uma esfera calcule a área e o volume desta esfera e imprima os valores calculados.

Modelo de saída de dados:

RAIO=99.99 AREA=99.99 VOLUME=99.99'''