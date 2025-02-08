N = int(input())
A = list(map(int, input().split()))
arr = [0] * 1001

for i in A:
    t = 0
    for j in range(1000, i, -1):
        t = max(t, arr[j])
    arr[i] = t + 1
print(max(arr))