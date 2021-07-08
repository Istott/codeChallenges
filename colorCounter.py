# every number represents a color. count the numbers to find sum of colors. 

def colorCounter(nums):
    if not nums:
        return "i hate you"

    numbersArr = [(0) for x in range(max(nums))]

    for i in range(len(nums)):
        numbersArr[nums[i] - 1] += 1

    return numbersArr

numArr = [,2,3,55,6,6,77,2]

print(colorCounter(numArr))