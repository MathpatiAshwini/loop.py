a=int(input("enter the frist number:"))
b=int(input("enter the second the number:"))
i=a
while i<b:
    if i%8==0 and i!=a:
        print(i)
    i=i+1
