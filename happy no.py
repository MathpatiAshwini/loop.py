i=int(input("enter the number"))
x=i
while x>=10:
    sum=0
    while x>0:
        p=x%10
        sum=sum+(p**2)
        x=x//10
        print("sum",sum)
    x=sum
if sum==1:
    print(i,"is a happy number")
else:
    print(i,"is a unhappy numbr")