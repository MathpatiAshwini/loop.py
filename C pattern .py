r=5
c=4
i=1
while i<=r:
    j=1
    while j<=c:
        if (j==1 and i!=1 and i!=5) or (i==1 and j>1 and j<5) or (i==5 and j!=1 and j<=5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
        
