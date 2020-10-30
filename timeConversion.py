def timeConversion(s):
    amPm = s[-2:]
    hour = s[:2]
    minutes = s[3:5]
    seconds = s[6:8]

    if int(hour) == 12 and amPm == 'AM':
        zerohour = '00'
        return zerohour + ':' + minutes + ':' + seconds

    if amPm == 'AM':
        return s[:-2]
    elif int(hour) == 12 and amPm == 'PM':
        return hour + ':' + minutes + ':' + seconds
    else:
        miltaryhour = str(int(hour) + 12)
        return miltaryhour + ':' + minutes + ':' + seconds
    



    # print(amPm)
    # print(hour)
    # print(minutes)
    # print(seconds)



time = '12:05:45AM'

print(timeConversion(time))