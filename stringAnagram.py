def stringAnagram(dictionary, query): #sort the lists and then compare!!!! must try
    dictTab = {}
    queryTab = {}
    result = []

    for x in range(len(dictionary)):
            dictTab[x] = {}
            for j in dictionary[x]:
                if j in dictTab[x]:
                    dictTab[x][j] += 1
                else:
                    dictTab[x][j] = 1
    
    for x in range(len(query)):
            queryTab[x] = {}
            for j in query[x]:
                if j in queryTab[x]:
                    queryTab[x][j] += 1
                else:
                    queryTab[x][j] = 1

    for x in queryTab:
        counter = 0
        for j in dictTab:
            if queryTab[x] == dictTab[j]:
                counter += 1
            
        result.append(counter)

    print(dictTab)
    # print(queryTab)

    return result


q = ['a', 'nark', 'bs', 'hack', 'stair']
dic = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']

print(stringAnagram(dic, q))