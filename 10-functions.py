# Create a function called days_in_month() which will take a year and a month as inputs
# and will use this informantion to return the number of days in the month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
                print("No leap year :(")
        else: 
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    if is_leap(year):
        month_days[1] += 1

    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

days = days_in_month(year, month)

print(days)