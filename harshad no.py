# (harshad number or not 12,9 126 )
num=int(input("enter the number:"))
k= 1
sum=0
n=num
while(num>0):
    k=num%10
    sum=sum+k
    num=num//10
if n%sum==0:
    print(str(n)+ "is a harashad number")
else:
    print(str(n)+ "is not a harshad number")


