#Ques2

year=int(input("Enter a year: "))

if year%100==0:
    if year%400==0:
        print("The given year is a Leap Year.")
    else:
        print("The given year is not a Leap Year.")
elif year%4==0:
    print("The given year is a Leap Year.")
else:
    print("The given year is not a Leap Year.")