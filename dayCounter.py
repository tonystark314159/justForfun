# This is a python program that counts how many days have elapsed since the beginning of the year, decade, century or millenium

nMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dictMonths = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

def isLeap(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        return False
    elif y % 4 == 0:
        return True
    return False

def fetchInputData():
    imonth, iday, iyear = tuple(map(int, input("MM DD YYYY :: ").split()))
    return imonth, iday, iyear

def judgeInput(imonth, iday, iyear):
    global dictMonths, nMonths, lMonths
    isValid = False
    if imonth <= 0 or iday <= 0 or iyear < 0:
        print("ValueError :: should be non-negative ::")
    elif imonth > 12:
        print("MonthOverflow :: A month value should not exceed 12 ::")
    elif iday > 31:
        print("DayOverflow :: A day value should not exceed 31 ::")
    elif (not isLeap(iyear)) and (iday > nMonths[imonth - 1]):
        print(f"DayOverflow :: {dictMonths[imonth]} has only a maximum of {nMonths[imonth - 1]} days ::")
    elif (isLeap(iyear)) and (iday > lMonths[imonth - 1]):
        print(f"DayOverflow :: {dictMonths[imonth]} has only a maximum of {lMonths[imonth - 1]} days ::")
    else:
        isValid = True
    return isValid

def daysStartingfromYear(imonth, iday, iyear):
    totalDays = sum(nMonths[:imonth - 1])
    totalDays += iday
    if isLeap(iyear) and imonth > 2:
        totalDays += 1
    return totalDays

def daysStartingfromSpecify(imonth, iday, iyear, start):
    if start.lower() == "decade":
        yearsElapsed = iyear % 10
    elif start.lower() == "century":
        yearsElapsed = iyear % 100
    elif start.lower() == "millenia":
        yearsElapsed = iyear % 1000
    elif start.lower() == "0":
        yearsElapsed = iyear
    else:
        print("TypeError :: cannot identify :: decade as default ::")
        yearsElapsed = iyear % 10
    totalDays = 365 * yearsElapsed
    for elapsed in range(iyear - yearsElapsed, iyear):
        if isLeap(elapsed):
            totalDays += 1
    totalDays += daysStartingfromYear(imonth, iday, iyear)
    return totalDays

if __name__ == '__main__':
    while True:
        M, D, Y = fetchInputData()
        if judgeInput(M, D, Y):
            startFrom = input("Start from the beginning of :: ")
            if startFrom.lower() == "year":
                days = daysStartingfromYear(M, D, Y)
                print(f"Days elapsed since beginning of the year: {days}")
            else:
                days = daysStartingfromSpecify(M, D, Y, startFrom)
                print(f"Days elapsed since beginning of the {startFrom.lower()}: {days}")
        else:
            ask = input("Do you want to terminate this program (1 or 0) ? ")
            if ask == 1:
                break
            else:
                continue
    print("Program terminated !!!")
    pass
