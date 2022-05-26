a= " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","M"))

l = a.split(",")
n=[]
for i in l:
    n.append(i.strip())
print(n)