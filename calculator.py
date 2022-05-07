print("Hello friends i am making today basic calculator")
print("\n")
print("Enter the first no.")
a=int(input())
print("Enter the second no.")
b=int(input())
print("Enter which operation you want in mid of these two no.")
operation=input()
if operation == '+':
        print("Addition :",a+b)
elif operation =='*':
        print("multiplication :",a*b)
elif operation =='-':
        print("substraction :",a-b)
elif operation =='/':
        print("division :",a/b)
elif operation =='%':
        print("reminder :",a%b)
else:
    print("Given operation can't perform on these no.")
