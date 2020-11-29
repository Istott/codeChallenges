#given a array of ints and a number for the lenth of subarrays, 
# so you divide the array into subarrays of whatever the length is, 
# and then find the minimum value per subarray, and return the maximum of those results
# import math

def maxInt(arr, num):
    # Divide the length of arr by num and assign that to subArrCounter ceil()
    # subArrNum = math.ceil(len(arr) / num)
    subArrNumCounter = 1
    subArrCounter = 1

    newArr = []
    lowestCache = max(arr)

    # loop through arr and find the lowest integer within that sub array

    for x in range(len(arr)):
        if subArrCounter < num:
            if len(arr) - 1 == x:
                if lowestCache > arr[x]:
                    newArr.append(arr[x])
                    break
                else:
                    newArr.append(lowestCache)
            else:
                if lowestCache <= arr[x]:
                    subArrCounter += 1
                else:
                    lowestCache = arr[x]
                    subArrCounter += 1
        elif subArrCounter == num:
            if len(arr) - 1 == x:
                if lowestCache > arr[x]:
                    newArr.append(arr[x])
                    break
                else:
                    newArr.append(lowestCache)
            else:
                if lowestCache <= arr[x]:
                    subArrCounter = 1
                    subArrNumCounter += 1
                    newArr.append(lowestCache)
                    lowestCache = max(arr)
                else:
                    lowestCache = x
                    subArrCounter = 1
                    subArrNumCounter += 1
                    newArr.append(arr[x])
                    lowestCache = max(arr)  
    print(newArr)
    return max(newArr)

arr1 = [2,1,2,43,345,7,8,9,93232,10000]
number = 2

print(maxInt(arr1, number))

#########################
# [1,2,3,4,5,6,7,8,9]
# [[1,2,3,4], [5,6,7,8], [9]]
# 1, 5, 9
# result 9
#######################