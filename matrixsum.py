def diagonalDifference(arr):
    firstsum = 0
    secondsum = 0
    lines = arr[0][0]
    del(arr[0])
    print(lines)

    for i in range(0, lines):
        firstsum += arr[i][i]
        secondsum += arr[i][lines - i - 1]
    
    print(firstsum)
    print(secondsum)
    
    return abs(firstsum - secondsum)


  
arr = [[3],
       [11, 2, 4], 
       [4 , 5, 6], 
       [10, 8, -12]] 
  
print(diagonalDifference(arr))