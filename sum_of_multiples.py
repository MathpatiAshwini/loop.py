n=int(input("enter the number"))
m=int(input("enter the number"))
i=0
sum=0
while i<m:
    if i%n==0:
        sum=sum+i
    i+=1
print(sum)

