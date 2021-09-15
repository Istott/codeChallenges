#create a slanted transposition cipher. encode string into cipher and return encoded string. Then create a decoder, to decode the encoded string. return decoded string.
# [t,_,w,d,_,_]
# [_,h,i,e,_,_]
# [_,_,i,s,i,_]
# [_,_,_,s,_,r]


def encoder(strToEncode, numRows):
    #each row will be a list
    rowArr = [[] for _ in range(numRows)]

    #create a list of the strToEncode broken down into characters
    newStr = strToEncode.replace(' ', '_')
    strArr = [x for x in newStr]
    # print(strArr)
    rowCounter = 0
    loop = 1

    #create a loop that takes a character and adds it to the appropriate row and location.
    for char in range(len(strArr)):
        rowArr[rowCounter].append(strArr[char])
        
        if loop == 1:
            insideCounter = rowCounter + 1
            for x in range(len(rowArr) - rowCounter - 1):
                rowArr[insideCounter].append('_')
                insideCounter += 1
            
        
        if rowCounter == len(rowArr) - 1:
            rowCounter = 0
            loop += 1
        else:
            rowCounter += 1
        
        # insideCounter = 0

    #combine characters in the rows into strings and then combine the strings.
    #return encoded string
    combinedArr = [x for x in rowArr]
    print(combinedArr)
    # final = ''
    # return (final.join(combinedArr))


line = 'this is weird'
line2 = 'my name is'
rows = 3

print(encoder(line2, rows))

