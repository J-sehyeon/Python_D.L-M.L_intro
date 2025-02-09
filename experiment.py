N = int(input())
A = list(map(int, input().split()))

res = []
for i in A:
    res.append([i])
for i in range(1, N):
    t = i
    for j in range(i):
        if A[j] < A[i] and len(res[t]) <= len(res[j]):
            t = j
    if t != i:
        res[i] = res[t] + res[i]
res.sort(key=len)
print(len(res[-1]))
print(*res[-1])

     
            

