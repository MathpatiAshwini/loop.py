   
# n=int(input("enter the rows:"))
# r=0
# k=chr(65)
# while r<=n:
#     j=0
#     while j<=r:
#         print(chr(k),end=" ")
#         j=j+1
#     k=k+1
#     print()
#     r=r+1
    
    
n=int(input("enter the rows:"))
r=n
while r>0:
    k=ord("E")
    j=0
    while j<r:
        print(chr(k),end=" ")
        j=j+1
        k=k-1
    print()
    r=r-1