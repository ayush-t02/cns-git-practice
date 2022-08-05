# multiplicative cipher
import math

L = "abcdefghijklmnopqrstuvwxyz"


def encryptMult(key, pt):
    res = ""
    for i in pt.lower():
        temp = (L.index(i) * key) % 26
        res += L[temp]
    return res.lower()


a = input('Enter plain text: ')
key = input('Enter Key: ')
b = ord(key) - 97

mCt = encryptMult(b, a)

print("Encrypted text: ", mCt)

if math.gcd(b, 26) == 1:

    r1 = 26
    r2 = b
    t1 = 0
    t2 = 1
    while r2 != 0 or r1 > 1:
        q, mod = divmod(r1, r2)
        t = t1 - (q * t2)
        r1 = r2
        r2 = mod
        t1 = t2
        t2 = t
    k = t1 + t2


    def decryptMult(key, ct):
        res = ""
        for i in ct.lower():
            temp = (L.index(i) * key) % 26
            res += L[temp]
        return res.lower()


    dct = decryptMult(k, mCt)
    print("Deciphered text: ", dct)

else:
    print("Decryption not possible as gcd not equal to 1")
