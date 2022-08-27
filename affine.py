import math


def modInverse(k, a):
    for x in range(1, a):
        if ((k % a) * (x % a)) % a == 1:
            return x
    return -1


def encrypt(text, k1, k2, n):
    c = ""
    if n == 1:
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                c += chr(((ord(char) - 65) * k1 + k2) % 26 + 65)

            else:
                c += chr(((ord(char) - 97) * k1 + k2) % 26 + 97)
        return c
    else:
        if k1.isupper():
            k1 = ord(k1) - 65
            k2 = ord(k2) - 65
            for i in range(len(text)):
                char = text[i]
                if (char.isupper()):
                    c += chr(((ord(char) - 65) * k1 + k2) % 26 + 65)
                else:
                    c += chr(((ord(char) - 97) * k1 + k2) % 26 + 97)
            return c
        else:
            k1 = ord(k1) - 97
            k2 = ord(k2) - 97
            for i in range(len(text)):
                char = text[i]
                if char.isupper():
                    c += chr(((ord(char) - 65) * k1 + k2) % 26 + 65)
                else:
                    c += chr(((ord(char) - 97) * k1 + k2) % 26 + 97)
            return c


def decrypt(c, k1, k2, n, a):
    p = ""
    if n == 1:
        invk1 = modInverse(k1, a)
        print("modInverse : " + str(invk1))
        for i in range(len(c)):
            char = c[i]
            if char.isupper():
                p += chr((((ord(char) - 65) - k2) * invk1) % 26 + 65)
            else:
                p += chr((((ord(char) - 97) - k2) * invk1) % 26 + 97)
        return p
    else:
        if k1.isupper():
            k1 = ord(k1) - 65
            k2 = ord(k2) - 65
            invk1 = modInverse(k1, a)
            print("modInverse : " + str(invk1))
            for i in range(len(c)):
                char = c[i]
                if char.isupper():
                    p += chr((((ord(char) - 65) - k2) * invk1) % 26 + 65)
                else:
                    p += chr((((ord(char) - 97) - k2) * invk1) % 26 + 97)
            return p
        else:
            k1 = ord(k1) - 97
            invk1 = modInverse(k1, a)
            k2 = ord(k2) - 97
            print("modInverse : " + str(invk1))
            for i in range(len(c)):
                char = c[i]
                if char.isupper():
                    p += chr((((ord(char) - 65) - k2) * invk1) % 26 + 65)
                else:
                    p += chr((((ord(char) - 97) - k2) * invk1) % 26 + 97)
            return p


text = input("Enter a plain text : ")
a = 26
n = int(input("press 1 if key is int or other for string : "))
if n == 1:
    k1 = int(input("Enter 1st key : "))
    k2 = int(input("Enter 2nd key : "))
    print("text : " + text)
    print("Shift : " + str(k1))
    print("Shift : " + str(k2))
    print("Cipher : " + encrypt(text, k1, k2, n))
    if math.gcd(a, k1) == 1:
        c = input("Enter a Cipher code : ")
        print("Cipher code : " + c)
        print("Shift : " + str(k1))
        print("Shift : " + str(k2))
        print("PT : " + decrypt(c, k1, k2, n, a))
    else:
        print("decryption not possible")

else:
    k1 = input("Enter 1st key : ")
    k2 = input("Enter 2nd key : ")
    print("text : " + text)
    print("Shift : " + k1)
    print("Shift : " + k2)
    print("Cipher : " + encrypt(text, k1, k2, n))
    if k1.isupper():
        if math.gcd(a, (ord(k1) - 65)) == 1:
            c = input("Enter a Cipher code : ")
            print("Cipher code : " + c)
            print("Shift : " + k1)
            print("Shift : " + k2)
            print("PT : " + decrypt(c, k1, k2, n, a))
        else:
            print("decryption not possible")
    else:
        if math.gcd(a, (ord(k1) - 97)) == 1:
            c = input("Enter a Cipher code : ")
            print("Cipher code : " + c)
            print("Shift : " + k1)
            print("Shift : " + k2)
            print("PT : " + decrypt(c, k1, k2, n, a))
        else:
            print("decryption not possible")
