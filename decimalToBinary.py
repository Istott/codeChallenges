def decToBin(decimal):
    # binary = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    # return bin(decimal).replace("0b", "") 
    if decimal >= 1:
        decToBin(decimal // 2)
    print(decimal % 2, end = '')
    return f' == {decimal}'



num1 = 56
print(decToBin(num1))

#binary = 256, 128, 64, 32, 16, 8, 4, 2, 1