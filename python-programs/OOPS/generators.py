def print_list(list1):
    for i in list1:
        yield i

# x = print_list([1,2,3,4])


for i in print_list([1,2,3,4]):
    print(i)
