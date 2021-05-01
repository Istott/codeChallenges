# [1,2,3,4,5,6] list of intergers
# threshold number
# find the minimal divsior.
import math

# def minimalDivisor(nums, threshold):
    # if the length of nums arr is the same as the threshold number
    #   and if the largest integer is greater than the threshold number
    #   then it lowest divisor is the highest integer. return that number. 
    # maxNum = max(nums)
    # print(maxNum, len(nums))

#     if len(nums) == threshold:
#         if maxNum >= threshold:
#             return maxNum
#     compute_sum = lambda x : sum([math.ceil(n / x) for n in nums])
#     d = 1
#     while compute_sum(d) > threshold:
#         d += 1
    
#     return d

# num1 = [1,2,5,6,2,2]
# num2 = [962551,933661,905225,923035,990560]
# num3 = [1,2,3]
# num4 = [] #solution 11
# thresh = 6

# print(minimalDivisor(num2, thresh))


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

num1 = [1,2,5,6,2,2]
num2 = [962551,933661,905225,923035,990560]
num3 = [1,2,3]
num4 = [] #solution 11
num5 = [
    375573263,
    59333571,
    562028259,
    455630792,
    532695257,
    361432625,
    68658860,
    392460904,
    910623262,
    615691527,
    198346354,
    100318375,
    779932561,
    524248095,
    153265973,
    378799108,
    464696497,
    873899067,
    375171632,
    417657982,
    949459694,
    178888264,
    186787346,
    642993166,
    814543853,
    283283757,
    9162092,
    726749516,
    476107159,
    197138068,
    102190267,
    472825862,
    176706111,
    513839600,
    587123109,
    592896468,
    242554032,
    54034729,
    158615363,
    759343917,
    793855442,
    520632381,
    95972977,
    853439047,
    503493493,
    239150342,
    400399464,
    826909716,
    369127487,
    442206126,
    125325658,
    922019377,
    408904217,
    331226615,
    972790181,
    196685000,
    872546226,
    919035093,
    641086940,
    249411501,
    352270534,
    341909345,
    916353746,
    713485194,
    513501260,
    725520492,
    923612265,
    266092962,
    937124986,
    560369505,
    136245076,
    410661769,
    715283705,
    615827715,
    623802541,
    428827314,
    82915288,
    333348299,
    139499673,
    575393511,
    882884294,
    182252376,
    357622029,
    33901033,
    71812410,
    180170891,
    63921646,
    845479496,
    541049420,
    390438110,
    720350243,
    323518940,
    412947790,
    909203863,
    407073384,
    451946098,
    604278636,
    382487783,
    339937787,
    777973001,
    315538078,
    134306503,
    889784731
]
thresh = 7776

print(minimalDivisor(num5, thresh))