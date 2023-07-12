year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")

elif year % 4 != 0 and year % 400 != 0:
    print("This is a common year")
elif year % 100 != 0:
    print("This is a leap year")
else:
    print("This is a leap year")
