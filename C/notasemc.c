/*bjetivo:
Escrever um programa que receba as notas de um aluno, calcule a média aritmética simples e exiba uma mensagem personalizada com base no resultado.

Requisitos do Programa:

    Entrada de Dados: O programa deve solicitar ao utilizador que insira duas notas (valores reais, ex: 8.2).

    Cálculo: O programa deve calcular a média entre essas duas notas.

    Saída de Dados: * Exibir o valor da média final com duas casas decimais.

    Lógica de Decisão (Estrutura Condicional):

        Se a média for maior ou igual a 7.0, exibir a mensagem: "Parabéns! Estás Aprovado."

        Se a média estiver entre 5.0 e 6.9 (inclusive), exibir a mensagem: "Estás em Recuperação."

        Se a média for menor que 5.0, exibir a mensagem: "Reprovado."

Exemplo de Execução esperada:

    Digite a nota 1: 6.5
    Digite a nota 2: 4.5
    Média: 5.50
    Status: Estás em Recuperação.*/
#include <stdio.h>
int main(){
    float nota1, nota2, total;
    printf("\tDigite suas notas:\n");
    scanf("%f%f", &nota1,&nota2);
    total = (nota1 + nota2) / 2;
    printf("\nNotas? %.2f\n")
    if (total >= 7.0 ) {
        printf("Parabéns! Estás Aprovado.");
    }
    else if (total >= 5.0 && total <= 6.9){
        printf("Está em recuperação.");
    }
    else {
        printf("Reprovado.");
    }
    return 0;
}