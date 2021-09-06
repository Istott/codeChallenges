# analyze the number given by taking each digit and seeing if it is divisible by the whole number. 
#count how many are divisible and return that number.

def findDigits(nums): #with an array of nums being passed in
    countArr = []
    memoDic = {}

    def individualNum(indexCounter):
        sepNum = [int(x) for x in str(nums[indexCounter])]
        count = 0

        for i in sepNum:
            if(i != 0 and nums[indexCounter] % i == 0):
                count += 1

        return countArr.append(count)

    for k in range(len(nums)):
        if nums[k] not in memoDic:
            memoDic[k] = nums[k]
            individualNum(k)
        else:
            countArr.append(memoDic[k])

    return countArr    


def findDigit(n): #with a number being passed in one at a time.
    sepNum = [int(x) for x in str(n)]
    count = 0

    for i in sepNum:
        if(i != 0 and n % i == 0):
            count += 1

    return count

  


numsArr = [234, 40, 12]
numStr = 20

print(findDigits(numsArr))
print(findDigit(numStr))