import this


print("Hi")

t = ("apple",1,True)
print(t)
print(type(t))
print(t[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


if "apple" in thistuple:
    print("Yes");


#tuples are immutable, but you can workaround. convert tuple into list. add element into the list and convert it back to tuple

x =("apple","orange","cherry")
y = list(x)
y[1]="Kiwi"
x= tuple(y)
print(x)


# Adding Items to tuple work around

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("carrot")
thistuple = tuple(y)
print(thistuple)



#you can add tuple to a tuple

thistuple = ("apple","banana","cherry")
y = ("orange",)
thistuple+=y
print(thistuple)

# removing Items to tuple work around

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
y.pop(1)
thistuple = tuple(y)
print(thistuple)

#unpack tuples

fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits
print(green)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
green, yellow ,*red = fruits
print(red)
#red will contains rest element as a list


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
print("oi")
print(green)
print(tropic)
print(red)

for i in fruits:
    print(i)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

print(mytuple.count("apple"))
print(mytuple.count("banana"))