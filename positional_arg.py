#1.basic positional argument
def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b 

result =add(2,5)
print("sum=",result)

#2.student details
def student_info(name,roll,marks):
    print("Name=",name)
    print("Roll=",roll)
    print("Marks=",marks)
    
    student_info("John",101,85)\
        
#3.error with wrong number of arguments
#simple interest
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("Simple Interest=",si)
    simple_interest(1000,5) #error: missing one argument
    simple_interest(1000,5,2) #error: too many arguments 
    
    #AREA OF CIRCLE 
    def area_of_circle(radius):
        area=3.14*radius*radius
        print("Area of Circle=",area)
        
        area_of_circle(5) 
        area_of_circle(5) 
        area_of_circle(10) 
        
        
        #check number positive, negative or zero
        def check_number(num):
            if num>0:
                print("Positive number")
            elif num<0:
                print("Negative number")
            else:
                print("Zero")
                
                check_number(10) #positive
                check_number(-5) #negative
                check_number(0) #zero
                
                
                
#odd or even
def odd_even(num):
    if (num%2==0):
        print(f"value {num}if even")
    else:
        print(f"value {num} is odd")
        odd_even(4) 
        odd_even(7)
        

#multiplication and division
def addition(a,b):
    add=a+b
    print("addition of two values",add)
    