# (output:-
# 1
# 121
# 12321
# 1234321
# 123454321)

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,i-1,end=" ")
#         j=j+1
#     i=i+1
#     print()  
# k=35
# p=42
# i=1
# while i<=6:
#     j=1
# if  j<=i:
#     print(chr(k),j,end=" ")
# else:
#     print(i,end=" ")
#     j=j+1
# i=i+1
# print()

n=int(input("enter the number:"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end=" ")
        k=k+1
        j=i
        while j>=i:
            print(j,end=" ")
            j=j+1
        m=2
        while m<=i:
            print(m,end=" ")
            m=m+1
        i=i+1
        print()