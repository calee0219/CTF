from pwn import *
import time
import base58
import hashlib

#     '15nQ5pMLEVAAVTRQ415LtwNbciyxLooHUR'

def solve(x):
    cry = x 
    clear = base58.b58decode(cry)
    li = list()
    for i in clear:
        li.append(ord(i))
    ori = clear[:-4]
    chk = clear[-4:]

    rechk = hashlib.sha256(ori).digest()
    rechk = hashlib.sha256(rechk).digest()
    a = list()
    for i in rechk:
        a.append(ord(i))

    checksum = rechk[:4]
    #print(a[:4])
    #print(li[-4:])
    final = ori+checksum
    #print(final)
    #print(base58.b58encode(final))
    return base58.b58encode(final)


#print solve(cry)
#print solve('1ELuX8Do1NDSMy4eV8H82dfFtTvKaqYyhg')

r = remote("178.62.22.245", 41662)
print r.recvuntil(':')
r.sendline('Y')
r.recv()
msg = r.recv()
print msg
he = msg[-7:-2]
print he
r.sendline(solve(he+'pMLEVAAVTRQ415LtwNbciyxLooHUR'))
r.recv()
while True:
    message = r.recv()
    num = message.split('\n')[0][6:]
    print num
r.interactive()
