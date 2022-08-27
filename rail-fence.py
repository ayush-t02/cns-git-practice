s = input("Enter string: ")
pt = s.replace(" ", "")
k = int(input("Enter key: "))
enc = [[" " for i in range(len(pt))] for j in range(k)]

row = 0
for i in range(len(pt)):
    enc[row][i] = pt[i]
    if row == 0:
        flag = 0
    elif row == k - 1:
        flag = 1
    if flag == 0:
        row += 1
    else:
        row -= 1

for i in range(k):
    print("".join(enc[i]))

ct = []
for i in range(k):
    for j in range(len(pt)):
        if enc[i][j] != ' ':
            ct.append(enc[i][j])
cipher = "".join(ct)
print("Cipher Text: ", cipher)
