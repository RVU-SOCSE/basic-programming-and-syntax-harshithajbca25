#Program for simple calculator
#1RUA25BCA0041
#Harshitha J
a=int(input("Enter first number"))
b=int(input("Enter second number"))
ch=input("Enter your choice")
match ch:
    case '+':
        print("Result : ",a+b)
    case '-':
        print("Result : ",a-b)
    case '*':
        print("Result : ",a*b)
    case '/':
        print("Result : ",a/b)
    case '%':
        print("Result : ",a%b)
    case '//':
        print("Result : ",a//b)
    case _:
        print("Invalid choice")
        
