def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num1
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2!=0:
        return num1/num2
    else:
        print("cannot be divided by zero")

def calculator():
    print("simple calculator")
    print("operations:")
    print("1. addition")
    print("2.substraction")
    print("3.miltiplication")
    print("4.divide")
    print("5.exit calculator")

    while True:
        choice=int(input("enter the operation(1-5):"))

        if choice==5:
            print("exiting calculator...")
            break
        num1=int(input("enter the 1st number:"))
        num2=int(input("enter the 2nd number:"))

        if choice==1:
            result=add(num1,num2)
            print(result)
        elif choice==2:
            result=sub(num1,num2)
            print(result)
        elif choice==3:
            result=mul(num1,num2)
            print(result)
        elif choice==4:
            result=div(num1,num2)
            print(result)
        else:
            print("invalid operation. enter the operation(1-5):" )


calculator()
