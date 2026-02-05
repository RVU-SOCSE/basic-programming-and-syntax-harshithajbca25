#Program for temperature convertor
#1RUA25BCA0041
#Harshitha J
print("1.Celsius to fahrenheit")
print("2.Fahrenheit to celsius")
ch=int(input("Enter your choice"))
match ch:
    case 1:
        c=float(input("Enter temperature in celsius"))
        fah=(c*9/5)+32
        print("Temperature in fahrenheit is :",fah)
    case 2:
        f=float(input("Enter temperature in fahrenheit"))
        cel=(f-32)*5/9
        print("Temperature in celsius is :",cel)
    case _:
        print("Invalid choice")
    
