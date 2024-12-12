#include <stdio.h>
#include <stdlib.h>
int main(){
char *b =  (char*) malloc(8); *b = 15;
int *i =  (int*) malloc(sizeof(int)); *i = 0;
while ( *i < 9)
{
printf("%d",(*b & (1<< IDENTIFIER(i)))>=1);

 *i = *i + 1;
}
free(b);
free(i);
}