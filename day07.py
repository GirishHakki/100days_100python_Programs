year = int(input("Enter the year to be checked : "))
if year % 100 == 0:
    if year % 400 == 0:
        print(year, " is a Leap Year")
    else:
        print(year, " is not a leap year")
else:
    if year % 4 ==0:
        print(year, " is a Leap Year")
    else:
        print(year, " is not a leap year")
