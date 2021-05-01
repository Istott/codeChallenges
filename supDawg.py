#Print out all of the strings in the following array in alphabetical order, each on a separate line.

# arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# arr.sort()

# for i in arr:
#     print(i)




# Add up and print the sum of the all of the minimum elements of each inner array:
# arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# go through each list and pull out the min number and then add all the mins together to get one sum. 

# arr1 = [min(n) for n in arr]

# arr1 = []

# for n in arr:
#     arr1.append(min(n))

# print(arr1)

# print(sum(arr1))


# Print out all of the numbers in the following array that are divisible by 3:

# arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

# we need to loop through the array and find all that are divisible by 3.

# newArr = [print(n) for n in arr if n % 3 == 0]



# #we got a list of strings, integers and floats. 

# # Print out each element of the following array on a separate line:

# array = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]

# #for loop that prints out each element in the array individually.

# for el in array:
#     print(el)



##########################################


# def anagram(a, b):
#     if len(a) != len(b):
#         return False, 'Word length doesnt match'

#     arrA = [x for x in a]
#     arrB = [x for x in b]

#     arrA.sort()
#     arrB.sort()

#     if arrA == arrB:
#         return True
#     else:
#         return False, 'not an anagram'

# a = 'bobe'
# b = 'bboe'

# print(anagram(a, b))


# function anagram(a, b){s
# 	const arr1 = []
# 	const arr2 = []

# 	if(a.length !== b.length){
# 		return 'length dont match' 
# 	}
# 	for(i = 0; i < a.length; i++){
# 		arr1.unshift(a.charAt(i))
# 		arr2.unshift(b.charAt(i))
# 	}
# 	arr1.sort()
# 	arr2.sort()
# 	return Array.isArray(arr1) && 
# 		Array.isArray(arr2) &&
# 		arr1.every((val, index) => val === arr2[index])
# }

# let arrA = 'bob'
# let arrB = 'bbow'

# console.log(anagram(arrA, arrB))


def capRev(x):
    arr = [i for i in x]
    newArr = []

    for x in range(len(arr)):
        if x == 0:
            newArr.insert(0, arr[x].capitalize())
        else:
            newArr.insert(0, arr[x])
        
    return ''.join(newArr)

string1 = 'string'
print(capRev(string1))