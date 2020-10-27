def twoSum(nums, target):
    newArr = {}
    indices = []

    if len(nums) == 2:
        idx = [0, 1]
        return idx

    for i in range(len(nums)):
        newArr[i] = nums[i]
        if i != 0:
            if nums[i] + nums[i - 1] == target:
                indices.append(i)
                indices.append(i - 1)

    for x in newArr:
        for j in newArr:
            if len(indices) == 2:
                return indices
            elif newArr[x] + newArr[j] == target and x != j:
                indices.append(x)
                indices.append(j)

    return 'no two values equal target'



arr = [2,4,5,5,9,8,9,8,9,7]
arr1 = [3,3,6]
arr2 = [-6,4,6,90]
tar = 6

print(twoSum(arr, tar))




    # if len(nums) > 5000:  
    #     prevIndex = 0          
    #     for i in range(len(nums)):
    #         if i != prevIndex:
    #             if nums[i] + nums[i - 1] == target:
    #                 indices.append(i)
    #                 indices.append(prevIndex)
    #                 return indices
    #         prevIndex += 1

    # newArr = {}
    # indices = []

    # for i in range(len(nums)):
    #         newArr[i] = nums[i]

    # for x in newArr:
    #     for j in newArr:
    #         if len(indices) == 2:
    #             return indices
    #         elif newArr[x] + newArr[j] == target and x != j:
    #             indices.append(x)
    #             indices.append(j)



        # lowdict = {}
        # tooHigh = {}
        # indices = []
        
        # for i in range(len(nums)):
        #     if nums[i] <= target:
        #         lowdict[i] = nums[i]
        #     else:
        #         tooHigh[i] = nums[i]
                
        # for x in lowdict:
        #     for j in lowdict:
        #         if len(indices) == 2:
        #             return indices
        #         elif lowdict[x] + lowdict[j] == target and x != j:
        #                 indices.append(x)
        #                 indices.append(j)





    # prevIndex = 0
    # indices = []

    # for i in range(len(nums)):

    #     if i != prevIndex:
    #         if nums[i] + nums[prevIndex] == target:
    #             indices.append(nums.index(nums[i]))
    #             indices.append(nums.index(nums[prevIndex]))
    #             return indices

    #     if nums.index(nums[i]) == prevIndex:
    #         prevIndex = i
    #     else:
    #         prevIndex += 1

    # return 'no two values equal that.'





# def constainsDuplicate(nums):
#         if len(nums) == 1: #check to see if array is 1. 
#             return False
        
#         duplicates = False
        
#         while duplicates == False:
#             dups = []
            
#             if len(nums) > 9900: #condition for large data sets
#                 if nums[0] < nums[1] and nums[-1] > nums[-2]:
#                     duplicates = False
#                 else:
#                     duplicates = True
#             else: # loop through and pull out duplicates. compare for duplicates.
#                 for i in range(len(nums)):
#                     if nums[i] not in dups:
#                         dups.append(nums[i])
#                     else:
#                         duplicates = True

#             if duplicates == True:
#                 return True #if there are duplicates
#             else:
#                 return False # if there are no duplicates

# arr = [0,0,5,1,3,5,6,7]
# arr1 = [1,2,3,4,5,6]
# arr2 = [0]
# arr3 = [3,3]
# arr4 = [3,1]
# print(constainsDuplicate(arr))
# print(len(arr))
