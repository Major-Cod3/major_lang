#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(){
int8_t b = 15;
int8_t i = 7;
while ( i >= 0)
{
printf("%d",(b >> i) & 1);

i = i - 1;
}
}