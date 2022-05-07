print("hello today we work on dictionary ::")
print()

di={1:"Hello",2:"Mohit",3:"Krishnia",4:"Engineer"}
print(di)
print()

print("Key are unique so immutable but value change")
print("To add new element at dictionary")
di["dictionary"]="program"
print(di)
print()

print("to delete there are 4 option 1->pop()  2->popitem()  3->clear()  4->del ")
print()
print("Pop(key) delete that whole key ")
s=di.pop(4)
print(di)
print()
print("popitem() will delete from dictionary from last but it store key and value simultaneously")
l=di.popitem()
print(di,l)
print()
print("clear delete the whole data of dictionary and del delete the dictionary")
print()

print("to add two dictionary we use update(dic_name) function")
m={"i":"am","mohit":"krishnia","from":"sikar"}
di.update(m)   # we can also add any element to dictionary by using update like -> di.update({"hobby":"to know new tech"})
di.update({"hobby":"to know new tech"})
print(di)
print()

print("to print the key value we use get(key)")
print(di.get("mohit"))
print("we use setdefault(key) to output if key exist it show value else it make it key and set none to value ")
print(di.setdefault("age"))
print(di)
di["age"]=19 # we can also use -> di.setdefault("age",19)
print(di)
print()

print("printing key and values of dictionary by for loop ")
for key in di:
    print(key," ",di[key])

print()
l={}
print("printing square from 1 to 10 by dictionary")
for x in range(1,11):
    l[x]=x*x

print(l)
print()

print("to print only value to dic_name.keys() and same as values()")
print(l.keys())
print(l.values())
print()

print("if we have two list and we want to merge and make it dictionary so we do typecast  -> dict(zip(l1,l2)) ")
l1=[1,2,3,4,5,6,7,8]
l2=[1,4,9,16,25,36,49,64]
s=dict(zip(l1,l2))
print(s)
print()

print("making a dictionary key from list ")
lis=[9,8,7,6,5,4]
q=dict.fromkeys(lis)    # make a dictionary key form list and set all values to -none else we can give the default value for all ->fromkeys(lis,20) -> 9:20,8:20,7:20,6:20 likewise
print(q)
print()
