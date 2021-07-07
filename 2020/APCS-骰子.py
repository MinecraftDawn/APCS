n, m = map(int, input().split())

dice = [[5,1,2,6,4,3] for _ in range(n)]

def forward(dice):
     new = [0] * 6
     new[0] = dice[0]
     new[1] = dice[5]
     new[2] = dice[2]
     new[3] = dice[4]
     new[4] = dice[1]
     new[5] = dice[3]
     return new

def right(dice):
     new = [0] * 6
     new[0] = dice[3]
     new[1] = dice[0]
     new[2] = dice[1]
     new[3] = dice[2]
     new[4] = dice[4]
     new[5] = dice[5]
     return new

for _ in range(m):
     a, b = map(int, input().split())
     if b > 0:
          a -= 1
          b -= 1
          dice[a],dice[b] = dice[b],dice[a]
     elif b == -1:
          a -= 1
          dice[a] = forward(dice[a])
     elif b == -2:
          a -= 1
          dice[a] = right(dice[a])

xxx = []
for i in range(n):
     xxx.append(str(dice[i][1]))
print(" ".join(xxx))
