# in python index always start from 0
var="hello world"
print(var[4])    # -> print char at index 4 =o
print(var[0:4])  # -> print char upto 4 starting from 0     these is known as slicing
print(var)       # -> print full string  ==[o:]==[0:0]==[::1]
# if there are 3 parameter given in [a:b:c] then it skip digit upto c in mid of a-b
print(var[0:7:2])# -> print value from 0-7 but it skip 1 value each time bcoz we apply last 2 for skip

# if -(negative) no. is given in [] then it start from reverse form index 0
print(var[-4:])  # -> start from reverse
# and to reverse the string we give the third parameter as -1
print(var[::-1])

# in this also use function endswith("var_name")
print(var.endswith("ld"))

# to count the char repeating in string we use count("char_name/string_name/int_value")
print(var.count('o'))

# to find something in program as string or char or int we use find("var_name")
print(var.find("w"))

# to make the first letter of line capital we use var_name.capitalize()
print(var.capitalize())

# to convert full string in CAPITAL  we use upper()
print(var.upper())

# to convert full string in lower case so use lower()
print(var.lower())

# to replace a char or a string  then we use this replace("var_exist","var_new")
print(var.replace("d","D"))

# to know the length of the string we use len(var_name)
print(len(var))
