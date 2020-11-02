# def stuff(head, k):
#     values = head

#     del values[-k]

    # for x in range(len(values)):
    # while values:
    #     values.pop(0)

#     return values

# arr = [1,2,3,4,5,6]
# tar = 4

# print(stuff(arr, tar))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_kth_from_end(head: Node, k):
    values = []
    
    cur = head
    while cur is not None:
        values.append(cur.value)
        cur = cur.next
    
    if k <= len(values):
        del values[-k]
        
    for x in range(len(values)):
        head.value = values[0]
        head = head.next
    
    return head


arr = [1,2,3,4,5,6]
tar = 4

print(remove_kth_from_end(arr, tar))


# def first_not_repeating_character(s):
#     newArr = []
#     stuff = [x for x in s]
#     repeating = [stuff.count(i) > 1 for i in stuff]

#     for x in range(len(repeating)):
#         if repeating[x] == False:
#             newArr.append(stuff[x])
#             return newArr[0]
    
#     return '_'

    


    
    # for x in range(len(stuff)):
    #     if stuff[x] not in newArr:
    #         newArr.append(stuff[x])

    #     if stuff[x] in newArr:
    #         repeating.append(stuff[x])

    #     for x in range(len(stringSplit)):
    #     if x in newArr:
    #         repeating.append(x)
    #     else:
    #         newArr.append(x)
            
    # if not repeating:
    #     return '_'
    # else:
    #     return repeating[0]

            

#     print(newArr)
#     print(repeating)
            
#     # if not repeating:
#     #     return '_'
#     # else:
#     #     return repeating[0]


# string = 'asdabasdfff'

# print(first_not_repeating_character(string))