n=int(input("enetr the rows:-"))
i=n
while i>0:
    j=0
    while j<=n-1:
        print(" ",end=" ")
        j=j+1
    if i%2==0:
        print("*",end=" ")
    # else:
    #     print(i)
    i=i+1
    print()
    