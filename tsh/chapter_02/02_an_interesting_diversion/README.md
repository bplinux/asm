gcc serial.c -fno-stack-protector -z execstack -masm=intel -no-pie -fno-pic -o serial

./control_eip.py > payload

for example: cat payload | ./serial
