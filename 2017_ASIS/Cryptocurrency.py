from pwn import *
import time
import base58
import hashlib
import string

number = 1
cry = '18zLFQ3Q8JGVNZrpkun5QBkYiXk2hGQYhS'
#     '15nQ5pMLEVAAVTRQ415LtwNbciyxLooHUR'

def solve(x):
    base58char = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    for i in range(len(x)):
        for char in base58char:
            cry = x[:i]+char+x[i+1:]
            print cry
            clear = base58.b58decode(str(cry))
            ori = clear[:-4]
            chk = clear[-4:]
            rechk = hashlib.sha256(hashlib.sha256(ori).digest()).digest()
            if chk == rechk[:4]: return cry
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j: continue
            for charI in base58char:
                for charJ in base58char:
                    cry = x[:i]+charI+x[i+1:]
                    cry = cry[:j]+charJ+cry[j+1:]
                    print cry
                    clear = base58.b58decode(str(cry))
                    ori = clear[:-4]
                    chk = clear[-4:]
                    rechk = hashlib.sha256(hashlib.sha256(ori).digest()).digest()
                    if chk == rechk[:4]: return cry
    '''
    clear = base58.b58decode(str(cry))
    #li = list()
    #for i in clear:
    #    li.append(ord(i))
    ori = clear[:-4]
    chk = clear[-4:]
    rechk = hashlib.sha256(hashlib.sha256(ori).digest()).digest()
    checksum = rechk[:4]
    final = ori+checksum
    return base58.b58encode(final)
    '''


#print solve(cry)
#print solve('15GJF8Do1NDSMy4eV8H82dfFtTvKaqYyhg')

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
    print '==========start=========='
    message = r.recv()
    print message
    if 'Good' in message: break
    if 'Oops' in message: break
    damaged = message.split('\n')[0].split(':')[1].strip()
    print(damaged)
    print(len(damaged))
    ss = solve(damaged)
    #print('-------')
    print(ss)
    #print('-------')
    r.sendline(ss)
r.interactive()
'''
