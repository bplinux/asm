[BITS 64]

EXIT_GROUP 	equ 231
EXIT		equ 60

segment .text
	global _start

_start:	xor rax, rax
	mov al, EXIT_GROUP
	xor rdi, rdi
	syscall
	xor rax, rax
	mov al, EXIT
	xor rdi, rdi
	syscall

