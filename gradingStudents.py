def gradingStudents(grades):
    students = grades[0]
    del(grades[0])
    results = []

    for x in range(students):
        strgrade = [i for i in str(grades[x])]
        # print(x)
        # print(strgrade)

        if grades[x] > 37:
            if 10 - int(strgrade[-1]) < 3:
                if int(strgrade[-1]) <= 9 and int(strgrade[-1]) >= 6:
                    results.append(int(str(int(strgrade[0]) + 1) + '0'))

            elif 5 - int(strgrade[-1]) < 3 and 5 - int(strgrade[-1]) >= 1:
                if int(strgrade[-1]) <= 4 and int(strgrade[-1]) >= 1:
                    del(strgrade[-1])
                    strgrade.append('5')
                    results.append(int(''.join(strgrade)))
            
            else:
                results.append(grades[x])
        else:
            results.append(grades[x])
    
    return results


arr = [5, 80, 73, 29, 38, 57]
print(gradingStudents(arr))