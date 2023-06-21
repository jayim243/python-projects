def isValid(month, day, year):  # complete
    listday31 = [i for i in range(1, 32)]
    listday30 = [i for i in range(1, 31)]
    listday29 = [i for i in range(1, 30)]
    listday28 = [i for i in range(1, 29)]
    months31 = [1, 3, 5, 7, 8, 10, 12]
    months30 = [4, 6, 9, 11]

    if isValidMonth(month):
        if month == 2:
            if isLeapYear(year):
                if day in listday29:
                    return True
                return False
            else:
                if day in listday28:
                    return True
                return False
        elif month in months31:
            if day in listday31:
                return True
            return False
        elif month in months30:
            if day in listday30:
                return True
            return False
    else:
        return False


def isLeapYear(year):  # complete
    x = False
    if year > 0:
        if year % 4 == 0:
            x = True
            if year % 100 == 0:
                x = False
                if year % 400 == 0:
                    x = True
                else:
                    x = False
            else:
                x = True
        else:
            x = False
        if x:
            return True
        else:
            return False
    else:
        return False


def isValidMonth(month):  # complete
    if 1 <= month <= 12:
        return True
    else:
        return False


def getDayOfWeek(month, day, year):  # complete
    months31 = [1, 3, 5, 7, 8, 10, 12]
    months30 = [4, 6, 9, 11]
    weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    totaldays = 0

    totaldays += year * 365
    if isLeapYear(year):
        y = month - 1
        while y > 0:
            if y in months31:
                totaldays += 31
            elif y in months30:
                totaldays += 30
            elif y == 2:
                totaldays += 29
            y -= 1
    else:
        y = month - 1
        while y > 0:
            if y in months31:
                totaldays += 31
            elif y in months30:
                totaldays += 30
            elif y == 2:
                totaldays += 28
            y -= 1
    totaldays += day
    totaldays += (((year - 1) // 4) - ((year - 1) // 100) + ((year - 1 ) // 400))
    return weekdays[totaldays % 7]


def getThanksgivingDate(year):  # complete
    counter = 0
    for i in range(1, 31):
        x = getDayOfWeek(11, i, year)
        if x == 'Thursday':
            counter += 1
            if counter == 4:
                return i
