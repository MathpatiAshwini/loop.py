# for letter in 'Flexi ple': 
#     if letter =='p': 
#         continue 
#     print ('Letters: ', letter)


# for letter in 'Flexi ple': 
#     if letter == '': 
#         continue
#     print ('Letters: ', letter) 

n=int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()