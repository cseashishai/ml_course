# num = int(input("enter the number"))

# if num%4==0:
#     if num%100==0:
#         if num%400==0:
#             print("year are not leep")
#         else:
#             print("is this leap year")
#     else:
#         print("is leep year")

# else:
#     print("if not leep year")    


# num1=float(input("enter the first  num  "))
# num2 =float(input("enter the second num  "))
# operation =input("enter the operator (+ ,- ,* , / ):  ")

# if operation =='+':
#     result =num1+num2
# elif operation == '-':
#     result=num1-num2
# elif operation =='*':
#     result =num1*num2
# elif operation =='/':
#     if num2!=0:
#         result =num1/num2
#     else:
#         result="error ! when devide by zero"        
# else:
#     result ="invalid output"

# print("result",result)


age =int(input("enter your age  "))
if_student = input("Are you a studen('yes/no')").lower()

if age<=5:
    price = "free"
elif age<= 12:
    price ='10$'
elif age <=17:
    if if_student =='yes':
        price ='$12'
    else:
        price ='$15'
elif age<=64:
    price  ='$25'
    if if_student =='yes':
        price = '$22'
    else:
        price= '$31'
else: 
    price='$20'
print("Price" ,price)           
     


                
               

    
