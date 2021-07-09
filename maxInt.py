#given a array of ints and a number for the lenth of subarrays, 
# so you divide the array into subarrays of whatever the length is, 
# and then find the minimum value per subarray, and return the maximum of those results

# my first approach was to create sub arrays and then pull the lowest value from them into a new array. 
# from there I would return the max number from that list.
# That approach had 3 loops and my space time was bloated. 

# I decided to create counters representing the subarray indices and subarray number.
# from there I created a cache that would hold the lowest value
# when done with one sub array, I would append the cache to the new array and reset cache for next sub array. 
# This made it so I was only looping through the array once. 

# for loop that iterates through the array.
# modulos the x against the num input
# store highest low value stored
# store current low value stored
# when modulos hits 0, compare highest low to current low and keep/change highest low to highest low cache
import time
start_time = time.time()

# def maxInt(arr, num):
#     highestLow = 0
#     currentLow = None
#     for i in range(len(arr)):
#         if currentLow == None or arr[1] < currentLow:
#             currentLow = arr[i]
#         if i % num == 0 or i == len(arr)-1:
#             if highestLow < currentLow:
#                 highestLow = currentLow
#             currentLow = None
#     return highestLow

def maxInt(arr, num): #solved in 
    highestLow = 0
    currentLow = arr[0]

    for i in range(len(arr)):
        if (i + 1) % num == 0: #checks at end of each subarray
            if currentLow > arr[i]:
                currentLow = arr[i]

            if highestLow < currentLow:
                highestLow = currentLow
            
            if len(arr) - 1 != i:
                currentLow = arr[i + 1]
        else: #main check
            if currentLow > arr[i]:
                currentLow = arr[i]
    
    if currentLow > highestLow:
        return currentLow
    else:
        return highestLow


arr1 = [2,1,3,5,243,5,6,7]
number = 2

print(maxInt(arr1, number))

#########################
# num = 4
# arr = [1,2,3,4,5,6,7,8,9]
# [[1,2,3,4], [5,6,7,8], [9]]
# 1, 5, 9
# result 9
#######################

# end_time = time.time()
# print (f"runtime: {end_time - start_time} seconds")











#######################################
# def maxInt(arr, num): #solved in 52 mins
#     maxValue = max(arr)

#     subArrNumCounter = 1
#     subArrCounter = 1

#     newArr = []
#     lowestCache = maxValue

#     # loop through arr and find the lowest integer within that sub array

#     for x in range(len(arr)):
#         if subArrCounter < num:
#             if len(arr) - 1 == x:
#                 if lowestCache > arr[x]:
#                     newArr.append(arr[x])
#                     break
#                 else:
#                     newArr.append(lowestCache)
#             else:
#                 if lowestCache <= arr[x]:
#                     subArrCounter += 1
#                 else:
#                     lowestCache = arr[x]
#                     subArrCounter += 1
#         elif subArrCounter == num:
#             if len(arr) - 1 == x:
#                 if lowestCache > arr[x]:
#                     newArr.append(arr[x])
#                     break
#                 else:
#                     newArr.append(lowestCache)
#             else:
#                 if lowestCache <= arr[x]:
#                     subArrCounter = 1
#                     subArrNumCounter += 1
#                     newArr.append(lowestCache)
#                     lowestCache = maxValue
#                 else:
#                     lowestCache = x
#                     subArrCounter = 1
#                     subArrNumCounter += 1
#                     newArr.append(arr[x])
#                     lowestCache = maxValue  
#     print(newArr)
#     return max(newArr)

# arr1 = [2,1,3,5,243,5,6,7]
# number = 4

# print(maxInt(arr1, number))


end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")