a=int(input("enter the number"))
p=len(str(a))
while a>0:
    digit=a%10
    digit=digit**2
    a//=10
    print(digit,end=" ")
    