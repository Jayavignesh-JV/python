num=int(input("Enter any number:"))
if num>2:
    for i in range(2,num):
        if num%i==0:
            flag=0
        else:
            flag=1
if flag==0:
    print("Its not a prime.")
else:
    print("Its a prime.")
