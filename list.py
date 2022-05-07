var=["hello","hi","good morning","welcome","good night",54,1200]
print(var)      # -> print all the value in string
print(var[2])   # -> print specific string at index 2 starting from 0
print()

num=[23,54,1,76,34,6,22]  # for shorting the given list we use var_name.short()
num.sort()
print(num)
num.reverse()         # and to reverse it we only use var_name.reverse()
print(num)
print()

print(min(num))       # to find minimum no. in a list we use min(var_name) and for maximum we use max(var_name)
print(max(num))
print()

var.append(5)         # to add no. in last we use append(value) which add in last
print(var)
print()

num.insert(2,44)      # to insert value at anywhere we use var_name.insert(index,value)
print(num)
print()

num.remove(44)        # to delete any no. from list we use var_name.remove(value)
print(num)
num.pop()             # and to delete only last digit as stack we use var_name.pop()
print(num)
print()

num[2]=321            # to change the value in list we   // in place of replace
print(num)
print()

print("to remove duplicate in list we convert it into set by type casting  set(type(lis)")
lis=[1,2,3,4,5,6,1,2,33,4,3,22]
print(lis)
k=set(lis)
print(k)
print()
