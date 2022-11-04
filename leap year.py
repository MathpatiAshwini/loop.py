# a=int(input("enter the year:-"))
# i=1
# while i<=3:
#     if a%4==0:
#         print(a,end=" ")
#         a=a-4
#     else:
#         print(a,end=" ")
#         a=a+4
#     i=i+1
#     print()
 
a=int(input("enetr the number:-"))
i=1
while i<=a:
    j=1
    while j<=i:
        if j==2:
            print("*",end=" ")
        elif j==4:
            print("*",end=" ")
        else:
            print(i,end=" ")
        j=j+1
    i=i+1
    print()