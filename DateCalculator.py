days_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                      9: 30, 10: 31, 11: 30, 12: 31}


def GetDateFromUser():
    print('Input a date like the following format, DD.MM.YYYY')
    current_date = input()

    split_current_date = current_date.split('.')
    current_day = int(split_current_date[0])
    current_month = int(split_current_date[1])
    current_year = int(split_current_date[2])
    return current_year, current_month, current_day


def GetDeltaFromUser():
    print('Input a number of days to add')
    days_number = int(input())
    return days_number


def GetDaysInMonth(current_month, current_year):
    if current_month == 2 and (current_year % 4 == 0 and current_year % 100 == 0 and current_year % 400 == 0):
        return 29
    else:
        return days_in_months[current_month]


def ValidateInput(current_year, current_month, current_day, days_number):
    if current_month not in days_in_months.keys():
        raise ValueError("month must be in 1..12 {}".format(current_month))
    if current_day > GetDaysInMonth(current_month, current_year) or current_day < 1:
        raise ValueError("day is out of range for month {}".format(current_day))



def JumpToNextMonth(current_month, current_year):
    if current_month == 12:
        current_month = 1
        current_year += 1
    else:
        current_month += 1
    return current_month, current_year


def JumpToPrevMonth(current_month, current_year):
    if current_month == 1:
        current_month = 12
        current_year -= 1
    else:
        current_month -= 1
    return current_month, current_year

def DayNumberInYear(current_day, current_month, current_year):
    month=1
    DayInYear = 0  
    while month < current_month:
        DayInYear += GetDaysInMonth(month, current_year)
        month +=1
    DayInYear += current_day
    return DayInYear

def GetDaysInYear(yearNumber):
    if yearNumber % 4 == 0 and yearNumber % 100 == 0 and yearNumber % 400 == 0:
        return 366
    return 365


try:
    current_year, current_month, current_day = GetDateFromUser()
    days_number = GetDeltaFromUser()
    try:
        ValidateInput(current_year, current_month, current_day, days_number)
    except ValueError as error:
        print(error)
        exit()
except BaseException as e:
    print("Wrong input:{}".format(e))
    exit()


if days_number > 0:
    days_left = days_number
    while DayNumberInYear(current_day, current_month, current_year) + days_left > GetDaysInYear(current_year):
        days_left -= GetDaysInYear(current_year) - DayNumberInYear(current_day, current_month, current_year)
        current_year += 1
        current_month = 1
        current_day = 0

    while current_day + days_left > GetDaysInMonth(current_month, current_year):
        days_left -= GetDaysInMonth(current_month, current_year) - current_day
        current_month, current_year = JumpToNextMonth(current_month, current_year)
        current_day = 0

    current_day += days_left

else:
    days_left = abs(days_number)
    while DayNumberInYear(current_day, current_month, current_year) - days_left  < 0 :
        days_left -= GetDaysInYear(current_year)
        current_year -= 1
        current_month = 12
        current_day = 31

    while current_day - days_left <= 0:
        days_left -= current_day
        current_month, current_year = JumpToPrevMonth(current_month, current_year)
        current_day = GetDaysInMonth(current_month, current_year)
    current_day -= days_left

print("Target date is {}.{}.{}".format(current_day,current_month,current_year))



