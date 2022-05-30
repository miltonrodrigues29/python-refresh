class Operation:
    def factorial(n):
        temp =1;
        for i in range(1,n+1):
            temp = temp*i

        return temp


# t = Operation
# n = int(input("Enter Number: "))
# print(t.factorial(n))
# print(t.fact(n))


def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)


n = int(input("Enter Number: "))
print(n, "Factorial is: ", fact(n))