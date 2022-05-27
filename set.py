import this


set1 = {"abc", 34, True, 40, "male"}
print(set1)

myset = {"apple", "banana", "cherry"}
print(type(myset))

for x in myset:
    print(x)

print("banana" in myset)

myset.add("orange")
myset.add("orange")
print(myset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset.update(["mil","ton"])
print(thisset)

thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

