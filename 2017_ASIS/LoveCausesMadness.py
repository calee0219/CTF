from pwn import *
import requests
import time
import urllib2
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


def checkFactorDB(n):
    """See if the modulus is already factored on factordb.com,
     and if so get the factors"""
    # Factordb gives id's of numbers, which act as links for full number
    # follow the id's and get the actual numbers

    r = requests.get('http://www.factordb.com/index.php?query=%s' % str(n))
    regex = re.compile("index\.php\?id\=([0-9]+)", re.IGNORECASE)
    ids = regex.findall(r.text)
    # These give you ID's to the actual number
    p_id = ids[1]
    q_id = ids[2]
    # follow ID's
    regex = re.compile("value=\"([0-9]+)\"", re.IGNORECASE)
    r_1 = requests.get('http://www.factordb.com/index.php?id=%s' % p_id)
    r_2 = requests.get('http://www.factordb.com/index.php?id=%s' % q_id)
    # Get numbers
    p = int(regex.findall(r_1.text)[0])
    ans = 1
    n = int(n)
    p = int(p)
    while n % p == 0:
        ans *= p
        n /= p
    return (ans, n)


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
print r.recv()
while True:
    message = r.recv()
    print message
    num = message.split('\n')[0][6:]
    print num
    fac = checkFactorDB(num)
    print('('+str(fac[0])+', '+str(fac[1])+')')
    r.sendline('('+str(fac[0])+','+str(fac[1])+')')
r.interactive()
