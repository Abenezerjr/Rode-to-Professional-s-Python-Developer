def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def dayInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # if not is_leap(year):
    #     return monthDays[month - 1]
    # else:
    #     monthDays[1] = 29
    #     return monthDays[month - 1]
    if is_leap(year) and month == 2:
        return 29
    return monthDays[month - 1]


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
days = dayInMonth(year, month)
print(days)
