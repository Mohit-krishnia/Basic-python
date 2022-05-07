print("enter any character to check wheather its digit,alphabate or special")
x=input()
if x.isalpha():
    if x.isupper():
      print("its big alphabates")
    else:
        print("its lower alphabates")
elif x.isdigit():
    print("its digit")
else:
    print("its a special symbol")
print()

print("enter any character to know its vowel or consonant ")
l=input()[0]
if l.isalpha():
    if l.upper() in 'AEIOU':
        print("vowel")
    elif l.lower() in 'aeiou':
        print("vowel")
    else:
        print("its consonant")
else:
    print("enter the character")