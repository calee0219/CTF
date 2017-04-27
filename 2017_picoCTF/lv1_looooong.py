#!/usr/bin/env python
from pwn import *
import re

n = remote('shell2017.picoctf.com', 41123)

n.recvuntil('\'')
string = n.recv()

char = string[0]
num = string[14:17]
last = string[-60]

ans = ''
for i in range(eval(num)):
    ans += char
ans += last

n.sendline(ans)

print(n.recv())

n.close()
