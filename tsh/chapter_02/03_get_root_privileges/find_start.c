#include <stdio.h>

unsigned long find_start(void) {
	__asm__("mov rax, rsp");
}

int main() {
	printf("0x%lx\n", find_start());
}
