#include <string.h>

#define BUFFSIZE 512

int main(int argc, char *argv[])
{
	char array[BUFFSIZE];
	if (argc < 2) {
		return -1;
	}
	strcpy(array, argv[1]);

	return 0;
}
