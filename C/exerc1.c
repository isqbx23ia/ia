#include <stdio.h>
#include <stdlib.h>
 //1 - Faça um algoritmo que leia os valores de A, B, C 
 // e em seguida imprima na tela a soma entre A e B
 //  é mostre se a soma é menor que C.


int main()
{
	int a,b,c;
	scanf("%d %d %d", &a, &b, &c);
	int soma;
	soma = a + b;
	if (soma < c) {
		printf("Soma é menor que C\n");

	} else {
		printf("Soma é maior que C\n");
	}
	
	return 0;
}
