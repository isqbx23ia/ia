//exerc 4  
#include <stdio.h>
#include <stdlib.h>


//4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.





int main()
{
	int a,soma,soma1;
	printf("Valor:\n");
	scanf("%d", &a);
    
	
		soma = a - 1;
		printf("\tAntecessor: %d\n", soma);

		soma1 = a + 1;
		printf("\tAntecessor: %d\n", soma1);
	
	return 0;
}
