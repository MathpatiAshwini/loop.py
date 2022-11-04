a="python"
len=len(str(a))
i=0
while i<=len:
    b=0
    while b<=i:
        print( a[b] , end=" ")
        b=b+1
    i=i+1
    print()
    
    
    
a=input("enter the word:-")
len=len(str(a))
i=0
while i<=len:
    b=0
    while b<=i:
        print( a[i] , end=" ")
        b=b+1
    i=i+1
    print()
    
a=input("enter the word:-")
len=len(a)
i=0
while i<=len:
    b=i
    while b>=0:
        print(a[b],end=" ")
        b=b-1
    i=i+1
    print()