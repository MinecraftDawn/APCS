length = int(input())
string = input()

tmp = []
for char in string:
    if 65 <= ord(char) <= 90:
        tmp.append(True)
    else:
        tmp.append(False)

conti = []
switch = tmp[0]
count = 0
for boolean in tmp:
    if boolean == switch:
        count += 1
    else:
        conti.append(count)
        count = 1
        switch = not switch
conti.append(count)

ans = 0
for i in range(len(conti)):
    count = 0
    if conti[i] >= length:
        count += length
        for j in range(i+1, len(conti)):
            if conti[j] == length:
                count += length
            elif conti[j] > length:
                count += length
                break
            else:
                break
        ans = max(ans, count)

print(ans)
