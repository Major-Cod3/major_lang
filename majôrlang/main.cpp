#include <stdio.h>
#include <stdlib.h>
int helo(){
printf("Teste de funções\n");

}
int main(){
void *boffer =  malloc(34);
int *number0 =  (int*) malloc(1); *number0 = 5;
int *number1 =  (int*) malloc(2); *number1 = 5;
int *number2 =  (int*) malloc(4); *number2 = 5;
int *number3 =  (int*) malloc(4); *number3 = 5;
printf("%d",*number0);

char *hello_world =  (char*) malloc(sizeof(char)*15);
snprintf(hello_world, 15, "\nHello, World!");
float *pi =  (float*) malloc(8); *pi = 3.141592653589793;
printf("ola");
scanf("%s",hello_world);
while ( *number0 < 16)
{
if ( *number0 == 9)
{
printf("acabou\n");

}
else{
printf("ainda não...\n");

}
 *number0 = *number0 + 1;
}
free(number0);
helo();
printf("%f",*pi);

printf("%s",hello_world);

free(number1);
free(number2);
free(number3);
free(hello_world);
free(pi);
free(boffer);
}