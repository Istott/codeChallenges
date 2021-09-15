

def repeatedString(s, n):
    if len(s) == 1 and s == 'a':
        return n

    newStr = s
    count = 0
    loopCounter = 0
    divCount = n // len(s)
    moduloCount = n % len(s)

    for x in s:
        loopCounter += 1
        if x == 'a':
            count += 1
        
        if loopCounter == n:
            break
    
    if divCount >= 1:
        count = count * divCount
        if moduloCount != 0: #loop with a count of remainder
            for x in range(moduloCount):
                if newStr[x] == 'a':
                    count += 1

    return count

print(repeatedString('babfasdfwwea', 20))