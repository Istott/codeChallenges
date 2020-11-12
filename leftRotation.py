def rotateLeft(d, arr):

    for x in range(d):
        arr.append(arr[x])
    
    del(arr[0:d])
    
    return arr



rotate = 4
arr1 = [1,2,3,4,5]

print(rotateLeft(rotate, arr1))