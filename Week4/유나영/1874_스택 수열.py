n = int(input())
numbers = [int(input()) for _ in range(n)]
# stack과 result에 1, +를 넣고 시작
stack, result = [1], ['+']
# 스택에 넣을 수
j = 2


for i in range(n):
    # 현재 뽑을 수가 j보다 크거나 같으면 stack에 j를 넣음
    if numbers[i] >= j:
        stack.append(j)
        result.append("+")
        j += 1

    # stack의 마지막 값이 현재 뽑을 값과 다른 동안
    while stack[len(stack)-1] != numbers[i]:
        last = stack[len(stack) - 1]
        # 현재 뽑을 수와 스택의 마지막 값이 다른데 j가 이미 커져버렸으면 fail
        if numbers[i] != last and j > last + 1:
            break
        # 현재 뽑을 수가 stack의 마지막 값보다 크다면 stack에 push
        elif numbers[i] > last:
            stack.append(j)
            result.append('+')
            j += 1
        # 현재 뽑을 수가 stack의 마지막 값보다 작거나 같으면 pop
        else:
            stack.pop()
            result.append('-')
    # stack의 마지막 값이 현재 뽑을 숫자와 같다면 pop
    if stack[-1] == numbers[i]:
        stack.pop()
        result.append('-')
# 수열의 끝까지 확인했는데 stack에 값이 남아있으면 fail
if stack:
    print("NO")
    exit(0)
print('\n'.join(result))
