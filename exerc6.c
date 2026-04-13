//exerc 6  
#include <stdio.h>
#include <stdlib.h>


//6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.




int main()
{
	int a,calc,reaju;
	printf("Valor:\n");
	scanf("%d", &a);
    
	calc = (a * 5/100);
	reaju = a + calc;
	
	printf("\nReajuste: %d\n ", calc);
	printf("O valor com o reajuste agora é: %d reais\n", reaju);
	return 0;
}
