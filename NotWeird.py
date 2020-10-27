def notWeird(n):
    if n % 2 == 1 or n == 1:
        print('Weird')
    elif n % 2 == 0 and n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and n > 5 and n <= 20:
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')
    else:
        print('im happy')


n1 = 3
n2 = 4
n3 = 24
n4 = 5
n5 = 13

# print(notWeird(n1))
# print(notWeird(n2))
# print(notWeird(n3))
# print(notWeird(n4))
print(notWeird(n5))