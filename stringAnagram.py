def stringAnagram(dictionary, query):
    # compare length of every string, if equal, then compare for anagram. 

    #sort by length. 
    #nested loop that compares length. if equal, sort string and compare for anagram.

    dictTab = sorted(dictionary, key=len)
    queryTab = sorted(query, key=len)
    result = []
    sortedLen = {}
    looping = True
    dictIndex = 0
    queryIndex = 0
    counter = 0 #we need a counter that we can append to our results arr and then refresh again. 

    #   - if queryTab value length is that same as prev:
    #       - we want to decrement dictIndex until len(dictTab[dictIndex]) < len(queryTab[queryIndex])

    while looping:
        if len(queryTab) <= queryIndex:
            looping = False

        if len(dictTab[dictIndex]) < len(queryTab[queryIndex]):
            dictIndex += 1
            continue
        elif len(dictTab[dictIndex]) > len(queryTab[queryIndex]): 
            result.append(counter)
            counter = 0
            queryIndex += 1
            continue
        else:
            if dictTab[dictIndex] in sortedLen:
                #sort queryTab[]
                if ''.join(sorted(dictTab[dictIndex])) == ''.join(sorted(queryTab[queryIndex])):
                    counter += 1
            else:
                sortedLen[len(dictTab[dictIndex])] = len(dictTab[dictIndex])

        





    # print(dictTab)
    # print(queryTab)

    return result



q = ['a', 'nark', 'bs', 'hack', 'stair']
dic = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']

print(stringAnagram(dic, q))


###############################


    # dictTab = [''.join(sorted(x)) for x in dictionary]
    # queryTab = [''.join(sorted(x)) for x in query]

    # # result = [dictTab.count(x) for x in queryTab]
    # result = []

    # for x in queryTab:
    #     counter = 0
    #     for j in dictTab:
    #         if x == j:
    #             counter += 1
            
    #     result.append(counter)


#######################################
    # dictTab = {}
    # queryTab = {}
    # result = []

    # for x in range(len(dictionary)):
    #         dictTab[x] = sorted(dictionary[x])

    # for x in range(len(query)):
    #         queryTab[x] = sorted(query[x])

    # for x in queryTab:
    #     counter = 0
    #     for j in dictTab:
    #         if queryTab[x] == dictTab[j]:
    #             counter += 1
            
    #     result.append(counter)

    # # print(dictTab)
    # # print(queryTab)

    # return result

#####################################


# def stringAnagram(dictionary, query): #sort the lists and then compare!!!! must try
#     dictTab = {}
#     queryTab = {}
#     result = []

#     for x in range(len(dictionary)):
#             dictTab[x] = {}
#             for j in dictionary[x]:
#                 if j in dictTab[x]:
#                     dictTab[x][j] += 1
#                 else:
#                     dictTab[x][j] = 1
    
#     for x in range(len(query)):
#             queryTab[x] = {}
#             for j in query[x]:
#                 if j in queryTab[x]:
#                     queryTab[x][j] += 1
#                 else:
#                     queryTab[x][j] = 1

#     for x in queryTab:
#         counter = 0
#         for j in dictTab:
#             if queryTab[x] == dictTab[j]:
#                 counter += 1
            
#         result.append(counter)

#     print(dictTab)
#     # print(queryTab)

#     return result

# q = ['a', 'nark', 'bs', 'hack', 'stair']
# dic = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']

# print(stringAnagram(dic, q))