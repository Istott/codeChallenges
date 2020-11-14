#return the name of the student(s) with the second lowest grade
#if the students tie for the second lowest grade. print them out in alphabetical order

def grades(name): 
    names = []
    doubleSecLow = []

    lowest = 0
    lowestCounter = 0

    secondLowest = 0
    secondLowestCounter = 0
    

    for x in name:
        if lowest == 0:
            lowest = x[1]
            lowestCounter += 1
            secondLowest = x[1] 
            secondLowestCounter += 1
            names.insert(0, x[0])
        elif x[1] < lowest:
            if lowestCounter > 1:
                secondLowestCounter = lowestCounter

            secondLowest = lowest
            lowest = x[1]
            lowestCounter = 1
            names.insert(0, x[0])
        elif x[1] == lowest:
            lowestCounter += 1
            names.insert(0, x[0])
        else:
            if x[1] == secondLowest:
                secondLowestCounter += 1
                secondLowest = x[1]
                names.insert(1, x[0])
            elif x[1] < secondLowest:
                if lowestCounter > 1:
                    secondLowestCounter = 1
                    secondLowest = x[1]
                    names.insert(lowestCounter, x[0])
                else:
                    secondLowestCounter = 1
                    secondLowest = x[1]
                    names.insert(1, x[0])
            else:
                print(len(names) + 1 // 2)
                if lowestCounter == len(names) + 1 // 2:
                    secondLowestCounter = 1
                    secondLowest = x[1]
                    names.append(x[0])
                else:
                    names.append(x[0])

    print(lowest)
    print(lowestCounter)
    print(secondLowest)
    print(secondLowestCounter)
    print(names)
    

    if lowestCounter > 1:
        if secondLowestCounter > 1:
            for x in range(lowestCounter, secondLowestCounter + lowestCounter):
                doubleSecLow.append(names[x])

            doubleSecLow.sort()

            return doubleSecLow[0] + '\n' + doubleSecLow[1]
        else:
            return names[lowestCounter]
    else:
        if secondLowestCounter > 1:
            for x in range(1, secondLowestCounter + 1):
                doubleSecLow.append(names[x])

            doubleSecLow.sort()

            return doubleSecLow[0] + '\n' + doubleSecLow[1]
        else:
            return names[1]

students = [['Harry',37.21], ['Berry',37.21], ['Tina', 37.2], ['akriti', 41], ['harsh', 39]]
students1 = [['Harry',-37.21], ['Berry',-37.21], ['Tina', -37.21], ['akriti', 41]]

print(grades(students1))