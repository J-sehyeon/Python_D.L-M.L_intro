import sys
input = sys.stdin.readline

N = int(input())
deque = []

def leng():
    return len(deque)

def fro(x):
    deque.append(x)

def bac(x):
    deque.insert(0, x)

def pop_x(x):
    return deque.pop(x)

def pri(x):
    print(deque[x])

for i in range(N):
    t = input().rstrip()
    if t in '3478':
        if not leng():
            print(-1)
        else:
            if t == '3':
                print(pop_x(-1))
            elif t == '4':
                print(pop_x(0))
            elif t == '7':
                pri(-1)
            else:
                pri(0)
    elif t == '5':
        print(leng())
    elif t == '6':
        if leng():
            print(0)
        else:
            print(1)
    elif t[0] == '2':
        bac(int(t[2:]))
    else:
        fro(int(t[2:]))



