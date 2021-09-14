#(this made me cry)

import collections

def nonDivisibleSubset(k, s):
    c = collections.Counter((i % k for i in s)) #loops through and makes the value the key and then the count of that value as the value. 
    count = 0
    newSubset = set()

    print(c)

    for x, y in c.most_common():
        if x == k / 2 or x == 0:
            count += 1
        elif k - x not in newSubset:
            count += y
            newSubset.add(x)

    return count

array = [1,7,4,2,4,3,6,5,578]
arr1 = [19,10,12,10,24,25,22,345,56,545,4,3,22,221]
arr2 = [1,7,4,2]
arr3 = [2,4,6,8,10,12,3]
num = 3

print(nonDivisibleSubset(num, arr2))