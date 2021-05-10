gcc overflow.c -fno-stack-protector -z execstack -masm=intel -no-pie -fno-pic -o overflow

./control_eip.py > payload

rarun2 stdin=./payload program=./overflow

