a = int(input("enter no. of rows you want in star"))

for i in range(0,a):
    for j in range(0,i):
        print("* ",end="")
    print()
for x in range(0,a):
    for y in range(0,a-x):
        print("* ",end="")
    print()