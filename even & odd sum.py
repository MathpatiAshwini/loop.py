a=int(input("enter the no:"))        
b=int(input("enter the no:"))
i=1
sum=0
sum2=0
while i<=b:
    if i%2==0:
        sum=sum+i
    else:
        sum2=sum2+i
    i=i+1
print(sum,sum2)