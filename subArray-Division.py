#find the sum of d consisting of the length of integers equal to m in array called s.
#count how many of these instances occur. 

def subArrDivision(s, d, m):
    count = 0

    for i in range(len(s) - m + 1): #subtracting m from the length of the array because we will be summing ahead. 
        if sum(s[i : i + m]) == d: #summing the m number of integers starting at i.
            count += 1

    return count

arr1 = [1,2,1,3,2]

day = 3
month = 2

print(subArrDivision(arr1, day, month)) #2


