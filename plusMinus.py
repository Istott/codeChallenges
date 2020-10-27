def plusMinus(arr):
    table = {
        'positive': 0,
        'negative': 0,
        'zero': 0
    }
    
    length = len(arr)

    for x in arr:
        if x > 0:
            table['positive'] += 1
        elif x < 0:
            table['negative'] += 1
        else:
            table['zero'] += 1

    pos = format(table['positive'] / length, '.6f')
    neg = format(table['negative'] / length, '.6f')
    zer = format(table['zero'] / length, '.6f')

    print(pos)
    print(neg)
    print(zer)


arr = [1,1,0,-1,-1]

print(plusMinus(arr))