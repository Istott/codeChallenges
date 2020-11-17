# [1,2,3,4,5,6] list of intergers
# threshold number
# find the minimal divsior.
import math

def minimalDivisor(nums, threshold):
    resultCounter = 1000
    prevCounter = 0
    right = 0
    left = 0


    while True:
        sumList = []
        for x in nums:
            sumList.append(math.ceil(x / resultCounter))
        
        sumOfNum = sum(sumList)

        if sumOfNum <= threshold:
            right = resultCounter
            left = prevCounter
            break
        else:
            prevCounter = resultCounter
            resultCounter *= 2

    while True:
        if right == 1:
            return 1

        middle = left + ((right - left) // 2)
        sumList = []

        for x in nums:
            sumList.append(math.ceil(x / middle))
        
        sumOfNum = sum(sumList)

        if right == left:
            return right

        if sumOfNum <= threshold:
            right = middle
        else:
            left = middle + 1



# we going to double our increment every time until sumOfNum <= threshold.
# resultCounter -= 1 until sumOfNum > threshold
# return prevSum

# if resultCounter > threshold:
#     return False

# print(sumOfNum)

num1 = [1,2,5,9]
num2 = [962551,933661,905225,923035,990560]
num3 = [1,2,3]
num4 = [] #solution 11
thresh = 6

print(minimalDivisor(num1, thresh))