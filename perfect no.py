a=int(input("enetr the number:"))
i=1
sum=0
while a>0:
    if a%i==0:
        sum=sum+i
    i=i+1
    if a==sum :
        print(a,"is perfect number")
    else:
        print(a,"is not perfect number")