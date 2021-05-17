#!/bin/sh

output=$(echo $1 | cut -f1 -d".")

nasm -f elf64 $1
ld $output.o -o $output

nasm $1 -o $output.pure
