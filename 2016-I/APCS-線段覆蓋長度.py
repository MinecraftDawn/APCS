count = int(input())
lines = []
ans = 0

for _ in range(count):
    line = list(map(int,input().split()))
    lines.append(line)

lines.sort()

index = 1
while index < len(lines):
    pre = lines[index-1]
    cur = lines[index]
    
    if pre[1] >= cur[0]:
        if pre[1] >= cur[1]:
            lines.pop(index)
        else:
            pre[1] = cur[1]
            lines.pop(index)
    else:
        index += 1
        
for start,end in lines:
    ans += end - start
    
print(ans)