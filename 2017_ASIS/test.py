import requests
import re


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
    print(p)
    ans = 1
    n = int(n)
    p = int(p)
    print(n)
    while n % p == 0:
        ans *= p
        n /= p
        print(ans,n, ans*n)
    return (ans, n)

num = '490183956356148144964150956013968347914133929241670142030157362395882364980208063702194692039482581634956707872673375170663232070283707860465855070613956390381025754200776859'
fac = checkFactorDB(num)
print(fac)
print(num)
print(fac[0]*fac[1])

