# There is a string, s, of lowercase English letters that is repeated infinitely many times. 
# Given an integer, n, find and print the number of letter a's in the first  letters of the infinite string.

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
        if moduloCount != 0: #loop with the count of remainder
            for x in range(moduloCount):
                if newStr[x] == 'a':
                    count += 1

    return count

print(repeatedString('babfasdfwwea', 20))