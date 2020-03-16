number = int(input())
scores = list(map(int, input().split()))

worst = float('inf')
best = float('-inf')

for score in scores:
    if score >= 60:
        worst = min(worst, score)
    else:
        best = max(best, score)
        
print(" ".join(map(str, sorted(scores))))
print(best if best != float('-inf') else "best case")
print(worst if worst != float('inf') else "worst case")