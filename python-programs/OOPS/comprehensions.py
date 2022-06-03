my_list = [2,3,5,7,11]
squared_list =[x*x for x in my_list if x%2 ==0]
print(squared_list)


squared_dict = {x:x*x for x in my_list}
print(squared_dict)


a =[1,2,3,4,5,6]
b = [7,8,9]

print([(a+b) for (a,b) in zip(a,b)])



my_list = [[10,20,30],[40,50,60],[70,80,90]]
flattened=[x for temp in my_list for x in temp]
print(flattened)


mul = lambda x: x*2
mul(1)
print(mul(2))


def myWrapper(n):
    return lambda n: n+2

mulFive = myWrapper(5)
print(mulFive(2))
