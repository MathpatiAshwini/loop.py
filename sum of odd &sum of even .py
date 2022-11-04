a=int(input("enter the number:"))
i=1
sum=0
sum2=0
while i<=a:
    if i%2==0:
        sum=sum+i
        print(i,end=" ")
    else:
        sum2=sum2+i
        print(i)
    i=i+1
print("sum of even:",sum,"sum of odd:",sum2)

