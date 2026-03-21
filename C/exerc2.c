#include <stdio.h>
#include <stdlib.h>
 //2 - Faça um algoritmo para receber um número qualquer 
 // e imprimir na tela se o número é par ou ímpar,
 //  positivo ou negativo.


int main()
{
	int a;
	printf("Digite um número\n");
	scanf("%d", &a);

	
	if ( a % 2 == 0 ) {
	
			printf("\tPar!\n");
	}
	else  {
		printf("\tÍmpar!\n");
	}
	 if (a < 0){
		printf("\tNegativo!\n");
	}
	else {
		printf("\tPositivo!\n");
	}
	
	return 0;
}
