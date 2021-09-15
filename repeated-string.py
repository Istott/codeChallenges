

def repeatedString(s, n):
    if len(s) == 1:
        return n

    newStr = s
    count = 0
    divCount = n // len(s)
    moduloCount = n % len(s)

    for x in s:
        if x == 'a':
            count += 1
    
    if divCount >= 1:
        count = count * divCount
        if moduloCount != 0: #loop with a count of remainder
            for x in range(moduloCount):
                if newStr[x] == 'a':
                    count += 1

    return count

print(repeatedString('babfasdfwwea', 20))