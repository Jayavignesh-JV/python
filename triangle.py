n=int(input("enter the number "))
for i in range(0,n+1):
    for j in range(1,(n+1)-i):
        print(" ",end="")
    for k in range(0,i+1):
        print(i,end=" ")
    print()
