# Check if a given year is a leap year.
# If the year is divisible by 4, it's a leap year unless it's also divisible by 100. But if it's also divisible by 400, then it's a leap year.

year = int(input("Introduce a year.\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else: 
            print("No leap year :(")
    else: 
        print("Leap year!")
else:
    print("No leap year")