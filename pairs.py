def pairs(k, arr):
    mymap = set(arr)
    counter = 0

    for item in arr:
        if item + k in mymap:
            counter += 1
    
    return counter

######################################
#binary search solution

#     arr.sort()
#     counter = 0

#     for item in arr:
#         to_search = item - k

#         is_found = binary_search(arr, to_search)

#         if is_found:
#             counter += 1
    
#     return counter


# def binary_search(arr, target): #binary search is recursive
#     if len(arr) == 0:
#         return False

#     mid_point = len(arr) // 2

#     if arr[mid_point] < target:
#         return binary_search(arr[mid_point + 1:], target)
#     elif arr[mid_point] > target:
#         return binary_search(arr[:mid_point], target)
#     else:
#         return True

