fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break

for x in range(6):
    print(x)
print("------------------------------")
for i in range(1,7):
    print(i)
print("------------------------------")

for i in range(1,11,2):
    print(i)

for x in range(6):
    print(x)
else:
    print("Finally Finished")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

for x in adj:
    pass