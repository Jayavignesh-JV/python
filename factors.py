a=int(input("enter the number "))
list=[1,a]
for i in range(1,a+1):
    b= a%i
    if b==0:
        print(i)
