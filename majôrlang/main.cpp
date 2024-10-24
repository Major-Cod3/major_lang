#include <stdio.h>
#include <stdlib.h>
class tui {
public:
tui() {

};
};

int main() {
		
printf("olá\n");

int number = 0;
char hello_world[] = "\nHello, World!";
float pi = 3.141592653589793;
while ( number<10)
{
if ( number==9)
{
printf("acabou\n");

}
else{
printf("ainda não...\n");

}
number = number+1;
}
printf("%f",pi);

printf("%s",hello_world);

}