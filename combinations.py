def combinations(*items):
	stuff = []
	cur = 1
	
	for x in items:
		stuff.append(x)
		
	for i in range(len(stuff)):
		if stuff[i] != 0:
			j = stuff[i] * cur
			cur = j
	
	return cur

# print(combinations(1, 3, 4))
# print(combinations(2,3,6,7,8,0))


########################################

def reverse(x):
	y = str(x)
	revNum = []
	negative = False

	for i in y:
		if i == '-':
			negative = True
		else:
			revNum.insert(0, i)
	
	result = int(''.join(revNum))
	revResult = result - result * 2

	if result > 2147483647 or revResult < -2147483647:
		return 0

	if negative == False:
		return result
	else:
		return revResult



number1 = -123
number2 = 123
print(reverse(number1))
print(2 ** 32)