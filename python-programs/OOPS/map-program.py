from functools import reduce

a = [1,2,3,4,5,6,7]
list1 = list(filter(lambda x:x%2==0,a))
print(list1)

double = list(map(lambda x:x*2,list1))
print(double)



sum = reduce(lambda a,b:a+b,double)
print(sum)

