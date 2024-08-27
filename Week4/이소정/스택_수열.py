import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
find = True
now = 1
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append("+")
        now += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        find = False
        break

if find:
    for a in ans:
        print(a)
else:
    print("NO")