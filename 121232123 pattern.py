# n=int(input("enter the rows:-"))
# i=1
# while i<=n:
#     k=1
#     while k<=n-i:
#         print(" ",end=" ")
#         k=k+1
#     j=i
#     while j>=1:
#         print(j,end=" ")
#         j=j-1
#     m=2
#     while m<=i:
#         print(m,end=" ")
#         m=m+1
#     i=i+1
#     print()

n=int(input("enter the rows:-"))
i=1
p=ord("A")
m=ord("A")
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=1:
        print(chr(p),end=" ")
        p=p+1
        j=j-1
    n=i
    while n>=1:
        print(chr(m),end=" ")
        m=m+1
        n-=1
    i=i+1
    print()