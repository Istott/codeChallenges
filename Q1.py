def findNumber(arr, k):

    for x in arr:
        if x == k or int(x) == int(k):
            return 'YES'
        else:
            return 'NO'