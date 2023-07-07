n = int(input("Enter the upper limit of the range: "))
a=[]
for num in range(1, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                a.append(num)
                print(a)
                break

                
