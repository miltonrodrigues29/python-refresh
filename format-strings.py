age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

final_string = txt.format(age)
print(final_string)
quantity = 3
itemno = 567
price = 49.95
check = "Iam {}, I was {} ,  Now iam {}"
print(check.format(quantity,itemno,price))

t = "We are so \t called \"Vikings\" "
print(t)


h = "miltoN"
print(h.capitalize())
print(h.casefold())
print(h.endswith("N",0,6))
print(h.find("l"))
print(h.find("o",0,1))
print(h.index("m"))

txt = "Hello , Welcome to my world."
y="mil"
try:
    print(txt.index("z"))
except:
    print("Error")

print(y.isalnum())

x="Hello"
y=15

print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))