a = int(input("enter the no. of rows you want"))

for i in range(0,a):
    for j in range(0,a-i):
        print("*",end="")
    print()