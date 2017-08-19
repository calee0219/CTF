import sys

problem = bytearray(open('./new.bmp', 'rb').read())
origin = bytearray(open('./lena.bmp', 'rb').read())

size = (len(problem) if problem > origin else len(origin))
xord_byte_array = bytearray(size)

for i in range(size):
    xord_byte_array[i] = problem[i] ^ origin[i]


open('./test.txt', 'w').write(xord_byte_array)
