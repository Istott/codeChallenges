def getBattery(events):
    charge = 50

    for i in events:
        if i < 0:
            charge += i
        else:
            charge += i
            if charge > 100:
                charge = 100
    
    return charge

eventArr = [10,-20,61,-15]

print(getBattery(eventArr))