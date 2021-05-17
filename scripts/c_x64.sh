#!/bin/bash

input=$1
output_weak=$(echo $1 | cut -f 1 -d".")_weak
output_mid=$(echo $1 | cut -f 1 -d".")_mid
output_strong=$(echo $1 | cut -f 1 -d".")_strong

gcc -fno-stack-protector -no-pie -fno-pic -z execstack $input -o $output_weak
gcc -fno-stack-protector -no-pie -fno-pic $input -o $output_mid
gcc $input -o $output_strong

