def miniMaxSum(arr):
    table = {
        'cur': 0, 
        'tallymax': 0, 
        'tallymin': 0,
        'max': max(arr),
        'min': min(arr)
    }

    if table['max'] == table['min']:
        table['tallymax'] = table['max'] * 4
        table['tallymin'] = table['min'] * 4

    for x in range(len(arr)):
        if table['cur'] != 0:
            if arr[x] != table['max']:
                table['tallymin'] += arr[x]
                table['cur'] = arr[x]
        else:
            if table['max'] != arr[x]:
                table['cur'] = arr[x]
                table['tallymin'] = arr[x]
        
    table['cur'] = 0

    for x in range(len(arr)):
        if table['cur'] != 0:
            if arr[x] != table['min']:
                table['tallymax'] += arr[x]
                table['cur'] = arr[x]
        else:
            if table['min'] != arr[x]:
                table['cur'] = arr[x]
                table['tallymax'] = arr[x]


    print(table['tallymin'], table['tallymax'])


newArr = [1,5,5,5,25]

print(miniMaxSum(newArr))