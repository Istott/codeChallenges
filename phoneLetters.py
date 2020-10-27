# def phoneLetters(digits):
#     numLetters = {
#         2: ['a', 'b', 'c'],
#         3: ['d', 'e', 'f'],
#         4: ['g', 'h', 'i'],
#         5: ['j', 'k', 'l'],
#         6: ['m', 'n', 'o'],
#         7: ['p', 'q', 'r', 's'],
#         8: ['t', 'u', 'v'],
#         9: ['w', 'x', 'y', 'z']
#     }

#     final = []

#     nums = [int(x) for x in digits]

#     if len(nums) == 1:
#         return numLetters[nums[0]]

#     if len(nums) == 2:
#         first = numLetters[nums[0]]
#         second = numLetters[nums[1]]
#         for x in first:
#             for j in second:
#                 final.append(x + j)

    

#     return final





# print(phoneLetters('93'))


def phoneLetters(digits):
    '''
    :type digits: str
    :rtype: List[str]
    '''
    phone = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}    
    result = []
    
    def helpCombine(current, leftoverDigits):
        if not leftoverDigits:
            result.append(current)
            return 
        else:
            for char in phone[leftoverDigits[0]]:
                helpCombine(current + char, leftoverDigits[1:])
    
    if not digits:
        return []
    else: 
        helpCombine("", digits)
        return result


print(phoneLetters('293'))