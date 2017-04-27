#!/usr/bin/env pythone3
import base64
from Crypto.Cipher import AES

key = base64.b64decode('/7uAbKC7hfINLcSZE+Y9AA==')
cyp = base64.b64decode('rvn6zLZS4arY+yWNwZ5YlbLAv/gjwM7gZJnqyQjhRZVCC5jxaBvfkRapPBoyxu4e')

aes = AES.new(key, AES.MODE_ECB)
print(aes.decrypt(cyp))
