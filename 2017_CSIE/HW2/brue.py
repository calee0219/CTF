import os
import string
import binascii

ans = '4b240000f3270000632f0000b3460000f3bc000033fe0000332c03003353070047270000432700007731000033440000a380000073de0000735a0100338b030033e8070033970700fc260000ab2d00005b43000043510000a380000033fe0000736e01003344050033ba050033130b00212b0000ab3200000b470000338e0000d3fd000073f30000b3aa02003369050033bf0f00333f2500'

flag = ''

while True:
    for i in string.ascii_lowercase + string.digits + string.ascii_uppercase + '{}':
        test = flag + i
        print(test)
        os.system('echo ' + test + ' | ./hw1')
        with open('flag', "rb") as f:
            hexdata = binascii.hexlify(f.read())
            if hexdata == ans[:len(hexdata)]:
                flag = flag + i
