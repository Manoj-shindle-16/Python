year = int(input("enter the year "))
leap_year = False
if year%4==0 and year%100!=0:
    leap_year = True
if year%400==0:
    leap_year = True
print(leap_year)

