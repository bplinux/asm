#include <stdio.h>

#define BUFFSIZE 30

void return_input() {
	char array[BUFFSIZE];
	gets(array);
	printf("%s\n",array);
}

int main() {
	return_input();

	return 0;
}
