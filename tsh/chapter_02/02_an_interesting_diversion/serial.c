#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int valid_serial(const char* serial) {

	size_t len = strlen(serial);
	size_t i;
	unsigned int checksum=0;
	
	if(len != 10)
		return 0;

	for(i = 0; i<10; i++) {
		checksum+=(unsigned int)(serial[i]);
		/*printf("%d\n", checksum);*/
	}
	if((checksum%720)==0)
		return 1;
	else
		return 0;
}

int validate_serial() {
	char serial[24];
	fscanf(stdin, "%s", serial);

	if(valid_serial(serial))
		return 1;
	else
		return 0;
}

void do_valid_stuff() {
	printf("Key is valid. This is a protected area!\n");
	exit(EXIT_SUCCESS);
}

void do_invalid_stuff() {
	printf("Key is wrong stupid. 0x90 and chill..\n");
	exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) {
	
	if(validate_serial())
		do_valid_stuff();
	else
		do_invalid_stuff();

	exit(EXIT_SUCCESS);
}
