import time
start_time = time.time()

def twoSum(nums, target):
    # newNums = []

    # for i in nums:
    #     if i >= target:
    #         newNums.append(i)

    indexCounter = 0

    for i in range(len(nums)):
        if i != indexCounter:
           if nums[i] + nums[indexCounter] == target:
               print(nums[i] + nums[indexCounter]) 
               return i, indexCounter
        
        if indexCounter >= len(nums) - 1:
            return 'no match'

        indexCounter += 1

    
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i != j and nums[i] + nums[j] == target:
    #             print(nums[i], nums[j])
    #             return i, j
    
    # return '-1, 1'



nums1 = [2, 11, 1323, 2, 3, 1, 1, 2, 1, 7, 11, 3, 15, 4]
target1 = 7

print(twoSum(nums1, target1))


end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")