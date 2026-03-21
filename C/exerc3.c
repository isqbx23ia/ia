//exerc 3
#include <stdio.h>
#include <stdlib.h>


//3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 
//caso contrário devera multiplicar A por B.
//  Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C 
// e
// imprimir seu valor na tela.




int main()
{
	int a,b,c,soma;
	printf("Valores:\n");
	scanf("%d %d", &a,&b);
    
	if (a == b) {
		soma = a + b;
		c = soma;
		printf("Soma: %d", c);

	}
	else if (a != b) {
		soma =  a * b;
		c = soma;
		printf("Soma: %d", c);
	}

	
	
	return 0;
}

