def maximalPalindrome(s):
    newObj = {}
    string = '' #insert all evens on sides and a 1 or 3 in the middle.
    
    for x in range(len(s)):
        if s[x] not in newObj:
            newObj[s[x]] = 1
        else:
            newObj[s[x]] += 1
    
    for x in newObj:
        # print(x)
        if newObj[x] % 2 == 0:
            if len(string) > 0:
                string = string[:len(string) // 2] + x * newObj[x] + string[len(string) // 2:]
            else:
                string = x * newObj[x]   

    for x in newObj:
        if newObj[x] == 3:
            string = string[:len(string) // 2] + x * newObj[x] + string[len(string) // 2:]
            return string
    
    for x in newObj:
        if newObj[x] == 1:
            string = string[:len(string) // 2] + x + string[len(string) // 2:]
            return string
    
    return string


arr = 'aabbozzz'

print(maximalPalindrome(arr))

####################################

def validTime(time):
    hours = []
    minutes = []
    
    for x in range(len(time)):
        if x < 2:
            hours.append(time[x])
        elif x > 2:
            minutes.append(time[x])
            
    combinehours = int("".join(hours))
    combineminutes = int("".join(minutes))
    
    if combinehours >= 24 or combineminutes >= 60:
        return False
    else:
        return True

    if int(time[:2]) >= 24 or int(time[3:]) >= 60:
        return False
    else:
        return True


time = '24:54'
print(validTime(time))

#######################################

# def readingVertically(arr):
#     string = []
#     longest = []

#     for x in range(len(arr)):
#         if x > 0:
#             if len(longest[0]) < len(arr[x]):
#                 longest.insert(0, arr[x])
#         else:
#             longest.append(arr[x])

#     for x in range(len(longest[0])):
#         for j in range(len(arr)):
#             if x <= len(arr[j]) - 1:
#                 string.append(arr[j][x])

#     return "".join(string)

# arr = ["Daisy", "Rose", "Hyacinth", "Poppy", "SummerBlossom"]
# print(readingVertically(arr))
