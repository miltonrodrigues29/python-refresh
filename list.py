from hashlib import new
import this


thislist = ["apple","banana","cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
if "apple" in thislist:
    print("Apple present in the list")
else:
    print("Apple is not present in the list")


thislist[1:3]=["milton","Milton"]
thislist.append("hi")
thislist.insert(2,"Christon")
newlist =["new"]
thislist.extend(newlist)
thistuple = ("milton","rodrigues")
thislist.extend(thistuple)
print(thislist)
try:
    thislist.remove("milton")
except:
    print("Element Does not exist in the list");

thislist.pop(4)

thislist.pop() #removes the last element
# for x in thislist:
#     print(x)
print(thislist)
for i in range(len(thislist)):
    print(i)
newlist =[]
newlist=[x for x in thislist if "a" in x]
print(newlist)

