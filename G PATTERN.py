c=5
r=6
i=1
while i<=r:
    j=1
    while j<=c:
        if (j==1 and i!=1 and i!=6) or (i==1 and j!=1) or (j==2  and i!=1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print(