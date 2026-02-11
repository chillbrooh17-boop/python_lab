


# Student Marks Program

m1 = int(input("Enter marks of english 1: "))
m2 = int(input("Enter marks of maths 2: "))
m3 = int(input("Enter marks of python 3: "))
m4 = int(input("Enter marks of data science 4: "))
m5 = int(input("Enter marks of rdbms 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("Total Marks =", total)
print("Average =", average)

# Grade Calculation
if average >= 90:
    print("Grade: A+")
elif average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
    
    #vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
    #positive negative
num=int(input("enter a number:"))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero")
    
     # Odd Even Program

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
    #Driving Licence Eligibility Program
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for a Driving Licence.")
else:
    print("You are not eligible for a Driving Licence.")
    print("You can apply after", 18)

