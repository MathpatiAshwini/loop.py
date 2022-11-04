r=6
c=5
i=1
while i<=r:
    j=1
    while j<=c:
        if (i==1) or (j==3) or (j==1 and i>=4 and i<=6) or (j<1 and j>=3 ) or  (i==6 and j==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()