a=int(input("Enter no. of row in which you want star"))
k=a-1
for i in range(0,a):
    #for j in range(k,0):
    #    print(end=" ")
     #   k=k-1
    for j in range(0,a-i):
        print("*",end="")
    print()