def birthdayCakeCandles(candles):
    largest = 0
    counter = 0

    for x in range(len(candles)):
        #if x is greater than largest, replace with x and start counter at 1
        #if x is equal to largest, +1 to counter
        if candles[x] > largest:
            largest = candles[x]
            counter = 1
        elif candles[x] == largest:
            counter += 1
    
    print(largest)
    print(counter)

    return counter

candleList = [3,2,1,3,6,9,3,4,6,6,9,9,9,9,9]
print(birthdayCakeCandles(candleList))