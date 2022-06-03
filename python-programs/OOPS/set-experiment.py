set1 = {1,6,7,5}


l = list(set1)
print(l)

l.sort()
if len(l)%2==0:
    num1 = l[int(len(l)/2)]
    num2 = l[(int(len(l)/2))-1]
    median = (num1+num2)/2
    print(median)
else:
    print(len[int(len(l)/2)])