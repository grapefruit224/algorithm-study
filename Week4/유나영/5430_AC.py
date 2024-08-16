from collections import deque

for _ in range(int(input())):
    ops = input()
    op_len = len(ops)
    num_len = int(input())
    number_input = list(map(int, input().strip('[]').replace(',', ' ').split()))
    numbers = deque(number_input)
    errored = False
    is_reversed = False

    i = 0
    while i < op_len:
        if i < op_len - 1 and ops[i] == ops[i + 1] == 'R':
            i += 2
            continue
        elif ops[i] == 'R':
            is_reversed = False if is_reversed else True
        else:
            try:
                if is_reversed:
                    numbers.pop()
                    print("reversed pop: ", numbers)
                else:
                    print("not reversed: ", numbers)
                    numbers.popleft()
            except IndexError:
                print("error")
                errored = True
                break
        i += 1

    if not errored:
        if is_reversed:
            numbers.reverse()
        print('[', end='')
        for j in range(len(numbers)):
            if j < len(numbers) - 1:
                print(f"{numbers[j]},", end='')
            else:
                print(f"{numbers[j]}", end='')
        print(']')
