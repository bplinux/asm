#include <string.h>

int main(int argc, char *argv[]) {
	char array[512];

	if(argc > 1)
		strcpy(array, argv[1]);

	return 0;
}
