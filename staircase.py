def staircase(n):
    counter = n - 1

    for x in range(1, n + 1):
        print((' ' * counter) + ('#' * x))
        counter -= 1

num = 5
print(staircase(num))