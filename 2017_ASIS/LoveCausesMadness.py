from pwn import *
from bs4 import BeautifulSoup
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
    #chk = clear[-4:]
    rechk = hashlib.sha256(ori).digest()
    rechk = hashlib.sha256(rechk).digest()
    #a = list()
    #for i in rechk:
    #    a.append(ord(i))
    checksum = rechk[:4]
    final = ori+checksum
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
    num = len(ids)-2
    print(ids)
    print(num)
    if num < 2: return 0
    else: return num * (num-1) / 2


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
    if 'Sorry' in message: break
    num = message.split('\n')[0][6:]
    fac = checkFactorDB(num)
    print(fac)
    r.sendline(str(fac))
r.interactive()
