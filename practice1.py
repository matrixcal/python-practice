number1=7
if number1>0:
    print "Number is positive"
else:
    if number1==0:
        print "Number is 0"
    else:
        print "Number is Negative"
##Find factorial of the number
num=num1=7
fact=1
while(num1>0):
    fact=fact*num1
    print fact,num1
    num1=num1-1
print "Factorial of ",num, "is", fact
#Check if number is even or odd
num2=10
if num2%2==0:
    print "Number is even"
else:
    print "Number is Odd"

#check if year is leap year or not
#if year is divisible by 400 then is_leap_year
#else if year is divisible by 100 then not_leap_year
#else if year is divisible by 4 then is_leap_year
#else not_leap_year

year=1992
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Year",year,"is leap year")
        else:
            print("Year", year, "is NOT leap year")
    else:
        print("Year", year, "is leap year")
else:
    print("Year", year, "is NOT leap year")

#find the largest number among three numbers
number1=10
number2=12
number3=15
if number1>number2 and number1>number3:
    print(number1,"is largest number")
if number2>number1 and number2>number3:
    print(number2, "is largest number")
if number3>number1 and number3>number2:
    print(number3, "is largest number")