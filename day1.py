#largest of 2 numbers
a=45
b=72
if a>b:
    print("a is greater")
elif a<b:
    print("b is greater")
else:
    print("both are equal")

#largest of 3 numbers
a=25
b=100
c=105
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
elif c > a and c > b:
    print("c is greater")
else:
    print("some values are equal")

#Smallest of 3 Numbers
a=25
b=78
c=13
if a<b and a<c:
    print("a is smallest")
elif b<c and b<a:
    print("b is smallest")
elif c<a and c<b:
    print("c is smallest")
else:
    print("all are equal")

#Write a program to check whether a number is divisible by 5.
a=67
if a%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

#Write a program to check whether a number is divisible by both 3 and 5.
a=20
if a%3==0 and (a%5==0):
    print("divisible by both 3 and 5")
elif a%3==0:
    print("the number is only divisible by 3")
elif a%5==0:
    print("the number is only divisible by 5")
else:
    print("the number is not divisible by both 3 and 5")

#Write a program to check whether a given year is a leap year or not.
a=2023
if a%4==0:
    print("leap year")
else:
    print("not a leap year")

#Write a program to check whether a given alphabet is a Vowel or Consonant.
a="e"
if a in ['a','e','i','o','u']:
    print("vowel")
else:
    print("consonant")

#Write a program to check whether a student has passed or failed.
marks=78
if marks>=45:
    print("pass")
else:
    print("fail")

#Find the largest of 3 numbers, including the possibility that two numbers are equal.
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
elif c>a and c>b:
    print("c is largest")
else:
    print("some are equal") 

#Write a program to check whether a number is Positive, Negative, or Zero.
n=int(input("enter a number: "))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")

#Write a Python program that takes a student's marks and prints the grade.
marks=int(input("enter your marks: "))
if marks <0 or marks >100:
    print("invalid")
elif marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=60:
    print("grade C")
elif marks>=40:
    print("grade D")
else:
    print("fail")

#Electricity Bill
#Write a Python program based on the total units used:
#Units             Rate
#0–100             ₹2 per unit
#101–200           ₹3 per unit
#201–300           ₹5 per unit
#Above 300         ₹7 per unit

units=int(input("enter the units of elecrticity used:"))
amount=0
if units <=100:
    amount=units*2
elif units <=200:
    amount=100*2+(units-100)*3
elif units <=300:
    amount=100*2+100*3+(units-200)*5
else:
    amount=100*2+100*3+100*5+(units-300)*7
print("the total electricity bill is:",amount)


#Shopping Discount
#Write a Python program to calculate the discount amount and final amount.
#₹0 – ₹1000             0%
#₹1001 – ₹5000          10%
#₹5001 – ₹10000         20%
#Above ₹10000           30%

amount=int(input("enter the total amount"))
if amount <=1000:
    discount=0
elif amount<=5000:
    discount=amount*10//100
elif amount<=10000:
    discount=amount*20//100
else:
    discount=amount*30//100
final_amount=amount-discount
print(discount)
print(final_amount)

#Write a program that takes 3 sides of a triangle and determines whether it is:
#All 3 sides equal       → Equilateral
#Any 2 sides equal       → Isosceles
#All 3 sides different   → Scalene
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a+b<=c or a+c<=b or b+c<=a:
    print("the given sides do not form a valid triangle")
elif a==b and b==c:
    print("equilateral")
elif b==c or a==b or a==c:
    print("isosceles")
else:
    print("scalene")

#Write a Python program that takes age and prints:
#Age < 0        → Invalid age
#0–12           → Child
#13–17          → Teenager
#18–59          → Adult
#60 and above   → Senior Citizen
age=int(input("enter the number:"))
if age<0:
    print("invalid age")
elif age<=12:
    print("child")
elif age<=17:
    print("teenager")
elif age<=59:
    print("adult")
else:
    print("above senior citizen")

#Write a Python program that takes:
#balance
#withdrawal amount
#withdrawal <= 0       → Invalid withdrawal
#withdrawal > balance  → Insufficient balance
#otherwise             → Withdrawal successful
amount=int(input("enter the balance:"))
withdrawal=int(input("enter the withdrawal amount:"))
if withdrawal <=0:
    print("Invalid withdrawal")
elif withdrawal > amount:
    print("insufficient balance")
else:
    remaining = amount - withdrawal
    print("Withdrawal successful")
    print("Remaining balance =", remaining)

#Take:
#username
#password
#Rules:username == "admin" AND password == "1234"
#Login successful
#Otherwise
#Invalid username or password
username=input("enter the username:")
password=input("enter the password:")
if username=="admin" and password=="1234":
    print("login successfully")
else:
    print("invalid username or password")