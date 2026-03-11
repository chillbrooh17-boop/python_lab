#positional arguments
#1.basic positional arguments
def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(2,5)
print("sum=",result)

#2.student information
def student_info(name,roll,marks):
    print("Name:",name)
    print("roll no:",roll)
    print("Marks:",marks)
student_info("ravi",101,15)

#3.error with wrong number of arguments
#simple interest
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("Simple Interest:",si)
    simple_interest(1000,2,2)
    simple_interest(50000,1.2,3)
    
    #area of circle 
    def ar_circle(r):
        a_circle=3.14*r*r
        print("Area of circle:",a_circle) 
        ar_circle(1.5)
        ar_circle(4)
        
        #check number positive or zero 
        def check_value(no):
            if no>0:
                print("positive",no)
            elif (no<0):
                print("negative",no)
            else:
                print("zero",no)
            check_value(10)
            check_value(-5) 
            
            odd or even
            def odd_even(no):
                if no%2==0:
                    print("even",no)
                else:
                    print("odd",no)
                odd_even(7)
                odd_even(12)
                
#arithmatic operation substraction
def addition(a,b):
    add=a+b
print("addition of two values",add)
addition(10,20,50)
addition(100,200)
