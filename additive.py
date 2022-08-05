plaintext = input("Enter plain text : ")
key = int(input("Enter the key value : "))
ciphertext = ""

def enc(pt,k):
    ct = ""
    for i in range(len(pt)):
        letter = pt[i]
        if letter.isupper():
            ct += chr(((ord(letter)-65+k)%26)+65)
        elif letter.isspace():
            ct += chr(32)
        elif letter.islower():
            ct += chr(((ord(letter)-97+k)%26)+97)
        else:
            pass

    print("Cipher Text is :", ct)
    return ct

ciphertext = enc(plaintext, key)

def dec(cit, k):
    ct = ""
    for i in range(len(cit)):
        letter = cit[i]
        if letter.isupper():
            ct += chr(((ord(letter) - 65 - k) % 26) + 65)
        elif letter.isspace():
            ct += chr(32)
        elif letter.islower():
            ct += chr(((ord(letter) - 97 - k) % 26) + 97)
        else:
            pass

    print("Decrpyted message: ", ct)

dec(ciphertext, key)