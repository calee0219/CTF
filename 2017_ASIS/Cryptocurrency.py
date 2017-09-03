from pwn import *
import time
import base58
import hashlib

number = 1
cry = '18zLFQ3Q8JGVNZrpkun5QBkYiXk2hGQYhS'
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

'''
r = remote("178.62.22.245", 58901)
print r.recvuntil(':')
r.sendline('Y')
r.recv()
msg = r.recv()
print msg
he = msg[-7:-2]
print he
r.sendline(solve(he+'pMLEVAAVTRQ415LtwNbciyxLooHUR'))
r.recv()
'''
while True:
    ss = raw_input()
    print(len(ss))
    if len(ss) == 6: print(solve(ss[:5]+'pMLEVAAVTRQ415LtwNbciyxLooHUR'))
    else: print(solve(ss[:-1]))
    '''
    message = r.recv()
    print message
    if 'Good' in message: break
    if 'Oops' in message: break
    damaged = message.split('\n')[0].split(':')[1].strip()
    #print damaged
    #ss = solve(damaged)
    #print('-------')
    #print(ss)
    #print('-------')
    r.sendline(solve(damaged))
    '''
r.interactive()
