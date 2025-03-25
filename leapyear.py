year=int(input("enter a year:"))

leap_year="leap year" if (year%4==0 and year%100!=0) or (year%400==0)else" not a leap year"

print(f"{year}is a{leap_year}")
