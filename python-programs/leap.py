n = int(input("Enter the year"))
if((n%400==0) or (n%100!=0) and (n%4==0)):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")

