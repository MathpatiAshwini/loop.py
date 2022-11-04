b=int(input("enter the number:"))
a=0
while b!=0:
    r=b%10
    a=a*10+r
    b=b//10
print("reverse number is:",a)