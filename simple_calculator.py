num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
if operation=='+':
    print("add:",num1+num2)
elif operation=='-':
    print("sub:",num1-num2)
elif operation=='*':
    print("mul:",num1*num2)
elif operation=='/':
    if num2!=0:
        print("div:",num1/num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")