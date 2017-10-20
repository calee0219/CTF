st = '8A808D8BB794FCBE93B8A3938FBEF8AFA79381FFB1'.decode('hex')
xor = 'CC'

new = ''

for i in st:
    new += chr(ord(i)^0xCC)
print(new)
