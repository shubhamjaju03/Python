year = int(input("Enter the year"))
if year % 4 ==0:
    if year % 400 == 0 or year % 100 !=0:
        print(year,"The year is leap year")
    else:
        print(year,"The year is not leap year")
else:
    print(year,"The year is not leap year")
