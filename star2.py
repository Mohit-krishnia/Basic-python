a = int(input("enter no. of rows you want star - "))

for i in range(0,a):
    for j in range(0,a-i):
        print(end=" ")
    for j in range(0,i+1):
        print("* ",end="")
    print()