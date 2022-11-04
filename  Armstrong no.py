i=int(input("enter the no:"))
a=i
sum=0
p=len(str(i))
while a>0:
    remander=a%10
    a=a//10
    sum+=remander**p
if sum==i:
    print(i," is armstrong no")
else:
    print(i," is not armstrong no")


